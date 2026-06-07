from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends

from app.db.session import get_db
from app.repositories.resume_repository import ResumeRepository
from app.services.resume_service import ResumeService

router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"]
)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    db=Depends(get_db)
):

    repository = ResumeRepository(db)

    service = ResumeService(
        repository
    )

    resume = await service.upload_resume(
        file=file,
        user_id="00000000-0000-0000-0000-000000000001"
    )

    return {
        "resume_id": str(resume.id),
        "status": resume.status
    }