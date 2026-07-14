import uuid

from app.models.resume import Resume
from app.models.resume import ResumeStatus
from app.repositories.resume_repository import ResumeRepository
from storage.file_storage import FileStorageService
from app.tasks.queue import resume_queue
from app.tasks.resume_tasks import process_resume

class ResumeService:

    def __init__(
        self,
        repository: ResumeRepository
    ):
        self.repository = repository
        self.storage = FileStorageService()

    async def upload_resume(
        self,
        file,
        user_id,
    ):

        file_url = await self.storage.save_resume(
            file
        )

        resume = Resume(
            user_id=user_id,
            title=file.filename,
            original_filename=file.filename,
            file_url=file_url,
            status=ResumeStatus.UPLOADED,
        )

        resume = self.repository.create(
            resume
        )

        # resume_queue.enqueue(
        #     "app.tasks.resume_tasks.process_resume",
        #     str(resume.id)
        # )

        process_resume(str(resume.id))

        return resume