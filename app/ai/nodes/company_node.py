from app.ai.workflows.report_state import ReportState

from app.services.company_intelligence_service import (
    CompanyIntelligenceService,
)


def company_node(
    state: ReportState,
):

    result = CompanyIntelligenceService.analyze(
        state["job_analysis"]
    )

    return {
        "company_intelligence": result
    }