from fastapi import APIRouter

from app.schemas.job_analysis import (
    JobAnalysisRequest
)

from app.services.job_analysis_service import (
    JobAnalysisService
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