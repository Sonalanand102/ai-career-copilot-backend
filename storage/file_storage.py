from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile


class FileStorageService:

    STORAGE_DIR = Path("storage/resumes")

    def __init__(self):
        self.STORAGE_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

    async def save_resume(
        self,
        file: UploadFile,
    ) -> str:

        extension = Path(file.filename).suffix

        filename = f"{uuid4()}{extension}"

        file_url = self.STORAGE_DIR / filename

        content = await file.read()

        with open(file_url, "wb") as f:
            f.write(content)

        return str(file_url)