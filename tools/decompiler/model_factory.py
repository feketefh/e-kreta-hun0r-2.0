from decompiler import extract_package
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil
import re


def convert_type(
    collection: str,
    type_: str,
) -> str:
    type_map = {
        "int": "int",
        "Integer": "int",
        "long": "int",
        "Long": "int",
        "float": "float",
        "Float": "float",
        "double": "float",
        "Double": "float",
        "BigDecimal": "float",
        "boolean": "bool",
        "Boolean": "bool",
        "String": "str",
    }
    type_ = type_map.get(type_, type_)
    if collection:
        type_ = f"list[{type_}]"
    return type_


def make_models(
    apk_path: Path | str,
    dex_name: str,
    final_output_dir: Path | str,
    package: Path | str,
    endpoint_file_pattern: str | re.Pattern[str] = R"^\w+V\d\.java$",
) -> None:
    if isinstance(apk_path, str):
        apk_path = Path(apk_path)
    if isinstance(final_output_dir, str):
        final_output_dir = Path(final_output_dir)
    if isinstance(package, str):
        package = Path(package)

    package_path = extract_package(apk_path, dex_name, final_output_dir, package, endpoint_file_pattern)
    for dir in package_path.iterdir():
        if not dir.is_dir():
            continue

        dtos = dir / "Dtos"
        if not dtos.exists():
            continue

        imports: dict[str, list[str]] = {}
        for dto in dtos.iterdir():
            _, names = make_dto(dto)
            imports[dto.stem] = names

        __init__ = dtos / "__init__.py"
        with open(__init__, "w") as f:
            f.write(
                "\n".join(
                    f"from .{file.removesuffix('Dto')} import {names[0]}"
                    for file, names in imports.items()
                )
                + "\n__all__ = [\n    "
                + ", ".join(i[0] for i in imports.values())
                + "\n]"
            )
        meta_data = dtos / "MetaData"
        with open(meta_data, "w") as f:
            f.write(", ".join(i[0] for i in imports.values()))


def make_dto_file(path: Path | str) -> Path | None:
    if isinstance(path, str):
        path = Path(path)

    with open(path / "models.py", "w") as f1:
        f1.write(
            """from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field

"""
        )

    with open(path / "models.py", "a") as f1:
        dtos = path / "Dtos"
        if not dtos.exists():
            return None

        for file in dtos.iterdir():
            fields = re.findall(
                R"@Metadata[\s\S]*?class (\w+?)(?:Dto)? |@SerializedName\(\"(\w+)\"\)[\s\n]*\w+ \w+ (?:(\w+)<)?(\w+?)(?:Dto)?>? (\w+?)(?:Dto)?;",
                file.read_text("utf-8"),
            )
            for class_name, alias, collection, type_, name in fields:
                if class_name == "Companion":
                    continue
                elif class_name:
                    f1.write(f"\nclass {class_name}(BaseModel):\n")
                else:
                    f1.write(
                        f'    {name}: Optional[{convert_type(collection, type_)}] = Field(alias="{alias}", default=None, frozen=True)\n'
                    )
    return path / "models.py"


def make_dto(path: str | Path) -> tuple[Path, list[str]]:
    if isinstance(path, Path):
        path = str(path)
    names: list[str] = []
    with open(path[:-8] + ".py", "w") as f1, open(path, "r", encoding="utf-8") as f2:
        f1.write(
            """from typing import Optional
from pydantic import BaseModel, Field

"""
        )
        fields = re.findall(
            R"@Metadata[\s\S]*?class (\w+?)(?:Dto)? |@SerializedName\(\"(\w+)\"\)[\s\n]*\w+ \w+ (?:(\w+)<)?(\w+?)(?:Dto)?>? (\w+?)(?:Dto)?;",
            f2.read(),
        )
        for class_name, alias, collection, type_, name in fields:
            if class_name == "Companion":
                continue
            elif class_name:
                f1.write(f"\nclass {class_name}(BaseModel):\n")
                names.append(class_name)
            else:
                f1.write(
                    f'    {name}: Optional[{convert_type(collection, type_)}] = Field(alias="{alias}", default=None, frozen=True)\n'
                )
    Path(path).unlink()
    return Path(path[:-8] + ".py"), names


if __name__ == "__main__":
    kreta_partial = Path(__file__).parent / "kreta_partial"
    apk_path = Path(__file__).parent / "base.apk"
    with TemporaryDirectory() as output_dir:
        make_models(
            apk_path, "classes3.dex", output_dir, "hu/ekreta/ellenorzo/data/remote"
        )
        shutil.copytree(output_dir, kreta_partial, dirs_exist_ok=True)
