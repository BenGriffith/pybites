from audioop import reverse
from datetime import datetime
import os
from pathlib import Path, PosixPath
from zipfile import ZipFile


TMP = Path(os.getenv("TMP", "/tmp"))
LOG_DIR = TMP / 'logs'
ZIP_FILE = 'logs.zip'


def zip_last_n_files(directory: PosixPath = LOG_DIR, zip_file: str = ZIP_FILE, n: int = 3):
    
    with ZipFile(zip_file, "w") as archive:
        for i, file_path in enumerate(sorted(directory.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True)):

            if i < n:
                file_creation_date = datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d')
                file_renamed_name = f"{file_path.stem}_{file_creation_date}{file_path.suffix}"
                file_renamed_path = f"{file_path.parent}/{file_renamed_name}"

                os.rename(file_path, file_renamed_path)
                archive.write(file_renamed_path, arcname=file_renamed_name)


# if __name__ == "__main__":
#     zip_last_n_files()