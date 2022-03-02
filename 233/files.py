from datetime import datetime
import os
from pathlib import Path, PosixPath
from zipfile import ZipFile

TMP = Path(os.getenv("TMP", "/com.docker.devenvironments.code/233/tmp"))
LOG_DIR = TMP / 'logs'
ZIP_FILE = 'logs.zip'


def zip_last_n_files(directory: PosixPath = LOG_DIR, zip_file: str = ZIP_FILE, n: int = 3):
    for file in directory.iterdir():
        print(file)


if __name__ == "__main__":
    zip_last_n_files()