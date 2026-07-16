# from app.ai.workflows.report_state import (
#     ReportState,
# )

# from app.services.final_report_service import (
#     FinalReportService,
# )


# def report_node(state: ReportState) -> dict:
#     """
#     Generate the final report using all previous analysis.
#     """

#     final_report = FinalReportService.analyze(
#         state["resume_analysis"].model_dump(),
#         state["job_analysis"].model_dump(),
#         state["match_score"].model_dump(),
#         state["skill_gap"].model_dump(),
#     )

#     return {
#         "final_report": final_report
#     }

from app.ai.workflows.report_state import ReportState

from app.services.final_report_service import (
    FinalReportService,
)


def report_node(
    state: ReportState,
):

    result = FinalReportService.analyze(

        state["resume_analysis"].model_dump(),

        state["job_analysis"].model_dump(),

        state["match_score"].model_dump(),

        state["skill_gap"].model_dump(),

        state["company_intelligence"].model_dump(),

        state["ats_analysis"].model_dump(),
    )

    return {
        "final_report": result
    }