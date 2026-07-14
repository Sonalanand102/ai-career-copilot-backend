from app.ai.workflows.report_state import (
    ReportState,
)

from app.services.resume_analysis_service import (
    ResumeAnalysisService,
)


def resume_node(state: ReportState) -> dict:
    """
    Analyze the parsed resume and add the result to the graph state.
    """

    resume_analysis = ResumeAnalysisService.analyze(
        state["parsed_resume"]
    )

    return {
        "resume_analysis": resume_analysis
    }