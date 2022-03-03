from datetime import datetime
import os
from pathlib import Path, PosixPath
from zipfile import ZipFile

TMP = Path(os.getenv("TMP", "/tmp"))
LOG_DIR = TMP / 'logs'
ZIP_FILE = 'logs.zip'


def zip_last_n_files(directory: PosixPath = LOG_DIR, zip_file: str = ZIP_FILE, n: int = 3):
    for file_path in directory.iterdir():
        file_creation_date = datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d')
        file_path_stem, file_path_suffix = file_path.stem, file_path.suffix
        os.rename(file_path, f"{file_path.parent}/{file_path_stem}_{file_creation_date}{file_path_suffix}")

    with ZipFile(zip_file, "w") as archive:
        for i, file_path in enumerate(sorted(directory.iterdir(), reverse=True)):
            if i < n:
                archive.write(file_path, arcname=file_path.name)


# if __name__ == "__main__":
#     zip_last_n_files()