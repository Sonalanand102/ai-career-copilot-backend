from fastapi import APIRouter

from app.schemas.job_analysis import (
    JobAnalysisRequest
)

from app.services.job_analysis_service import (
    JobAnalysisService
)
''' ================================'''

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

''' ================================= '''

from app.schemas.match import (
    MatchRequest
)

from app.services.match_score_service import (
    MatchScoreService
)

from app.services.skill_gap_service import (
    SkillGapService
)

''' ================================= '''

from app.schemas.report import (
    ReportRequest
)

from app.models.analysis import Analysis

from app.models.analysis_report import (
    AnalysisReport
)

from app.repositories.analysis_repository import (
    AnalysisRepository
)

from app.repositories.analysis_report_repository import (
    AnalysisReportRepository
)

from app.services.final_report_service import (
    FinalReportService
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

@router.post("/match")
async def match_resume_to_job(
    payload: MatchRequest,
    db: Session = Depends(get_db)
):

    repository = ResumeRepository(
        db
    )

    resume = repository.get_by_id(
        payload.resume_id
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    resume_analysis = ResumeAnalysisService.analyze(
        resume.parsed_content
    )

    job_analysis = JobAnalysisService.analyze(
        payload.job_description
    )

    result = MatchScoreService.analyze(
        resume_analysis.model_dump(),
        job_analysis.model_dump()
    )

    return result

@router.post("/skill-gap")
async def skill_gap_analysis(
    payload: MatchRequest,
    db: Session = Depends(get_db)
):

    repository = ResumeRepository(
        db
    )

    resume = repository.get_by_id(
        payload.resume_id
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    resume_analysis = ResumeAnalysisService.analyze(
        resume.parsed_content
    )

    job_analysis = JobAnalysisService.analyze(
        payload.job_description
    )

    result = SkillGapService.analyze(
        resume_analysis.model_dump(),
        job_analysis.model_dump()
    )

    return result

@router.post("/report")
async def generate_report(
    payload: ReportRequest,
    db: Session = Depends(get_db)
):

    repository = ResumeRepository(
        db
    )

    resume = repository.get_by_id(
        payload.resume_id
    )

    analysis_repository = AnalysisRepository(
        db
    )

    analysis = analysis_repository.create(
        Analysis(
            user_id=resume.user_id,
            resume_id=resume.id,
            job_description=payload.job_description,
            status="COMPLETED"
        )
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    resume_analysis = ResumeAnalysisService.analyze(
        resume.parsed_content
    )

    job_analysis = JobAnalysisService.analyze(
        payload.job_description
    )

    match_score = MatchScoreService.analyze(
        resume_analysis.model_dump(),
        job_analysis.model_dump()
    )

    skill_gap = SkillGapService.analyze(
        resume_analysis.model_dump(),
        job_analysis.model_dump()
    )

    final_report = FinalReportService.analyze(
        resume_analysis.model_dump(),
        job_analysis.model_dump(),
        match_score.model_dump(),
        skill_gap.model_dump()
    )

    report_repository = AnalysisReportRepository(
        db
    )

    report_repository.create(
        AnalysisReport(
            analysis_id=analysis.id,
            report_type="JOB_ANALYSIS",
            report_json=final_report.model_dump()
        )
    )

    report_repository.create(
        AnalysisReport(
            analysis_id=analysis.id,
            report_type="RESUME_ANALYSIS",
            report_json=resume_analysis.model_dump()
        )
    )

    report_repository.create(
        AnalysisReport(
            analysis_id=analysis.id,
            report_type="MATCH_SCORE",
            report_json=match_score.model_dump()
        )
    )

    report_repository.create(
        AnalysisReport(
            analysis_id=analysis.id,
            report_type="SKILL_GAP",
            report_json=skill_gap.model_dump()
        )
    )

    analysis_repository.create(
        AnalysisReport(
            analysis_id=analysis.id,
            report_type="FINAL_REPORT",
            report_json=final_report.model_dump()
        )
    )

    return {
        "analysis_id": analysis.id,
        "report": final_report
    }

@router.get("/analysis/{analysis_id}")
async def get_analysis(
    analysis_id: UUID,
    db: Session = Depends(get_db)
):

    analysis_repository = AnalysisRepository(
        db
    )

    analysis = analysis_repository.get_by_id(analysis_id)

    if not analysis:
        raise HTTPException(
            status_code=404,
            detail="Analysis not found"
        )

    report_repository = AnalysisReportRepository(
        db
    )

    reports = report_repository.get_by_analysis_id(analysis_id)

    if not reports:
        raise HTTPException(
            status_code=404,
            detail="Reports not found"
        )

    return {
        "analysis": analysis,
        "reports": reports
    }