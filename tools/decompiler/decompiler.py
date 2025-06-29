import zipfile
import subprocess
from pathlib import Path
import shutil
import re
from tempfile import TemporaryDirectory


def extract_package(
    apk_path: Path | str,
    dex_name: str,
    final_output_dir: Path | str,
    package: Path | str,
    endpoint_file_pattern: str | re.Pattern[str] = R"^\w+V\d\.java$"
) -> Path:
    if isinstance(apk_path, str):
        apk_path = Path(apk_path)
    if isinstance(final_output_dir, str):
        final_output_dir = Path(final_output_dir)
    if isinstance(package, str):
        package = Path(package)

    with TemporaryDirectory() as dex_dir, TemporaryDirectory() as jadx_dir:
        # 1. Extract classes3.dex
        with zipfile.ZipFile(apk_path, "r") as zipf:
            zipf.extract(dex_name, path=dex_dir)

        # 2. Run jadx on just classes3.dex
        subprocess.run(
            [
                R"C:\Users\vajkh\Downloads\jadx-1.5.1\bin\jadx.bat",
                "-d",
                jadx_dir,
                "--no-res",
                "--show-bad-code",
                str(Path(dex_dir) / dex_name),
            ],
            check=True,
        )

        target_dir = Path(jadx_dir) / "sources" / package

        # remove unwanted files
        for file in target_dir.rglob("*"):
            if file.is_file() and file.suffix != ".java":
                file.unlink()

        for category in target_dir.glob("*"):
            if category.is_file():
                category.unlink()
                continue

            for file in category.glob("*.java"):
                if not re.match(endpoint_file_pattern, file.name):
                    file.unlink()

            try:
                Dtos = next(p for p in category.iterdir() if p.is_dir())
            except StopIteration:
                continue

            for Dto in Dtos.glob("*"):
                if not Dto.name.endswith("Dto.java"):
                    Dto.unlink()
                    continue
            Dtos.rename(category / "Dtos")
            try:
                shutil.rmtree(Dtos)
            except FileNotFoundError:
                pass


        # 3. Copy only hu/ekreta/ellenorzo/data/remote
        if target_dir.exists():
            shutil.copytree(target_dir, final_output_dir, dirs_exist_ok=True)
            print(f"✅ Extracted to: {final_output_dir}")

        else:
            raise Exception("❌ Target package not found.")
    return final_output_dir


if __name__ == "__main__":
    apk_path = Path(__file__).parent / "base.apk"
    dex_name = "classes3.dex"
    final_output_dir = Path(__file__).parent / "kreta_partial"

    extract_package(apk_path, dex_name, final_output_dir, "hu/ekreta/ellenorzo/data/remote")