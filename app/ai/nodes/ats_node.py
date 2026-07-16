from app.ai.workflows.report_state import (
    ReportState,
)

from app.services.ats_analysis_service import (
    ATSAnalysisService,
)


def ats_node(
    state: ReportState,
) -> dict:
    """
    Perform deterministic ATS analysis.
    """

    ats_analysis = ATSAnalysisService.analyze(
        state["resume_analysis"],
        state["job_analysis"],
    )

    return {
        "ats_analysis": ats_analysis
    }