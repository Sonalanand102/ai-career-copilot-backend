from app.ai.workflows.report_state import (
    ReportState,
)

from app.services.job_analysis_service import (
    JobAnalysisService,
)


def job_node(state: ReportState) -> dict:
    """
    Analyze the job description and add the result to the graph state.
    """

    job_analysis = JobAnalysisService.analyze(
        state["job_description"]
    )

    return {
        "job_analysis": job_analysis
    }