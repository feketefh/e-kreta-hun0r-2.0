import model_factory
import translate_endpoints

from tempfile import TemporaryDirectory
import shutil
import re
from pathlib import Path

base_path = Path(__file__).parent / "base.apk"
dex_name = "classes3.dex"
package = "hu/ekreta/ellenorzo/data/remote"
endpoint_file_pattern = re.compile(R"^\w+V\d\.java$")

ignore_list = ["idp"]

final_dir = Path(__file__).parent.parent.parent / "src" / "e_kreta"

with TemporaryDirectory() as output_dir:
    output_dir = Path(output_dir)
    model_factory.make_models(base_path, dex_name, output_dir, package, endpoint_file_pattern)
    for i in output_dir.iterdir():
        if i.name in ignore_list:
            continue
        endpoints = next(j for j in i.iterdir() if j.is_file())
        translate_endpoints.translate_file(endpoints)
        endpoints.unlink()
        try: 
            shutil.rmtree(final_dir / i.name.removesuffix("api"))
        except FileNotFoundError:
            pass
        except Exception:
            print(final_dir / i.name.removesuffix("api"), "could not be cleaned and may have fused with old files")
        shutil.copytree(i, final_dir / i.name.removesuffix("api"), dirs_exist_ok=True)
    shutil.copytree(output_dir, Path(__file__).parent / "kreta_partial", dirs_exist_ok=True)