from fastapi import APIRouter

from app.schemas.job_analysis import (
    JobAnalysisRequest
)

from app.services.job_analysis_service import (
    JobAnalysisService
)

from uuid import UUID

from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.repositories.resume_repository import (
    ResumeRepository
)

from app.services.resume_analysis_service import (
    ResumeAnalysisService
)

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)


@router.post("/job")
async def analyze_job(
    payload: JobAnalysisRequest
):

    result = JobAnalysisService.analyze(
        payload.job_description
    )

    return result


@router.post("/resume/{resume_id}")
async def analyze_resume(
    resume_id: UUID,
    db: Session = Depends(get_db)
):

    repository = ResumeRepository(
        db
    )

    resume = repository.get_by_id(
        resume_id
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    return ResumeAnalysisService.analyze(
        resume.parsed_content
    )