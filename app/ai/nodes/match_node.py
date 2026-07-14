from app.ai.workflows.report_state import (
    ReportState,
)

from app.services.match_score_service import (
    MatchScoreService,
)


def match_node(state: ReportState) -> dict:
    """
    Calculate the match score between the resume and the job.
    """

    match_score = MatchScoreService.analyze(
        state["resume_analysis"].model_dump(),
        state["job_analysis"].model_dump(),
    )

    return {
        "match_score": match_score
    }