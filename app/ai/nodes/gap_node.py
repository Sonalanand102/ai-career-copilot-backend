from app.ai.workflows.report_state import (
    ReportState,
)

from app.services.skill_gap_service import (
    SkillGapService,
)


def gap_node(state: ReportState) -> dict:
    """
    Identify the skill gap between the resume and the job.
    """

    skill_gap = SkillGapService.analyze(
        state["resume_analysis"].model_dump(),
        state["job_analysis"].model_dump(),
    )

    return {
        "skill_gap": skill_gap
    }