# # from langgraph.graph import (
# #     StateGraph,
# #     START,
# #     END
# # )

# # from app.ai.workflows.report_state import (
# #     ReportState
# # )

# # from app.services.resume_analysis_service import (
# #     ResumeAnalysisService
# # )

# # from app.services.job_analysis_service import (
# #     JobAnalysisService
# # )

# # from app.services.match_score_service import (
# #     MatchScoreService
# # )

# # from app.services.skill_gap_service import (
# #     SkillGapService
# # )

# # from app.services.final_report_service import (
# #     FinalReportService
# # )

# # def resume_node(state: ReportState):
# #     result = ResumeAnalysisService.analyze(
# #         state["resume"].parsed_content
# #     )

# #     return {
# #         "resume_analysis": result
# #     }

# # def job_node(state: ReportState):

# #     result = JobAnalysisService.analyze(
# #         state["job_description"]
# #     )

# #     return {
# #         "job_analysis": result
# #     }

# # def match_node(state: ReportState):

# #     result = MatchScoreService.analyze(
# #         state["resume_analysis"].model_dump(),
# #         state["job_analysis"].model_dump()
# #     )

# #     return {
# #         "match_score": result
# #     }

# # def gap_node(state: ReportState):

# #     result = SkillGapService.analyze(
# #         state["resume_analysis"].model_dump(),
# #         state["job_analysis"].model_dump()
# #     )

# #     return {
# #         "skill_gap": result
# #     }

# # def report_node(state: ReportState):

# #     result = FinalReportService.analyze(    
# #         state["resume_analysis"].model_dump(),
# #         state["job_analysis"].model_dump(),
# #         state["match_score"].model_dump(),
# #         state["skill_gap"].model_dump()
# #     )

# #     return {
# #         "final_report": result
# #     }

# # workflow = StateGraph(
# #         ReportState
# # )

# # workflow.add_node(
# #     "resume",
# #     resume_node
# # )

# # workflow.add_node(
# #     "job",
# #     job_node
# # )

# # workflow.add_node(
# #     "match",
# #     match_node
# # )

# # workflow.add_node(
# #     "gap",
# #     gap_node
# # )

# # workflow.add_node(
# #     "report",
# #     report_node
# # )

# # workflow.add_edge(
# #     START,
# #     "resume"
# # )

# # workflow.add_edge(
# #     "resume",
# #     "job"
# # )

# # workflow.add_edge(
# #     "job",
# #     "match"
# # )

# # workflow.add_edge(
# #     "match",
# #     "gap"
# # )

# # workflow.add_edge(
# #     "gap",
# #     "report"
# # )

# # workflow.add_edge(
# #     "report",
# #     END
# # )

# # report_graph = workflow.compile()
    
# from langgraph.graph import (
#     StateGraph,
#     START,
#     END
# )

# from app.ai.workflows.report_state import (
#     ReportState
# )

# from app.services.resume_analysis_service import (
#     ResumeAnalysisService
# )

# from app.services.job_analysis_service import (
#     JobAnalysisService
# )

# from app.services.match_score_service import (
#     MatchScoreService
# )

# from app.services.skill_gap_service import (
#     SkillGapService
# )

# from app.services.final_report_service import (
#     FinalReportService
# )


# def resume_node(state: ReportState):

#     result = ResumeAnalysisService.analyze(
#         state["resume"].parsed_content
#     )

#     return {
#         "resume_analysis": result
#     }


# def job_node(state: ReportState):

#     result = JobAnalysisService.analyze(
#         state["job_description"]
#     )

#     return {
#         "job_analysis": result
#     }


# def match_node(state: ReportState):

#     result = MatchScoreService.analyze(
#         state["resume_analysis"].model_dump(),
#         state["job_analysis"].model_dump()
#     )

#     return {
#         "match_score": result
#     }


# def gap_node(state: ReportState):

#     result = SkillGapService.analyze(
#         state["resume_analysis"].model_dump(),
#         state["job_analysis"].model_dump()
#     )

#     return {
#         "skill_gap": result
#     }


# def report_node(state: ReportState):

#     result = FinalReportService.analyze(
#         state["resume_analysis"].model_dump(),
#         state["job_analysis"].model_dump(),
#         state["match_score"].model_dump(),
#         state["skill_gap"].model_dump()
#     )

#     return {
#         "final_report": result
#     }


# workflow = StateGraph(ReportState)

# # Nodes

# workflow.add_node(
#     "resume",
#     resume_node
# )

# workflow.add_node(
#     "job",
#     job_node
# )

# workflow.add_node(
#     "match",
#     match_node
# )

# workflow.add_node(
#     "gap",
#     gap_node
# )

# workflow.add_node(
#     "report",
#     report_node
# )

# # START

# workflow.add_edge(
#     START,
#     "resume"
# )

# workflow.add_edge(
#     START,
#     "job"
# )

# # Resume + Job -> Match

# workflow.add_edge(
#     "resume",
#     "match"
# )

# workflow.add_edge(
#     "job",
#     "match"
# )

# # Resume + Job -> Gap

# workflow.add_edge(
#     "resume",
#     "gap"
# )

# workflow.add_edge(
#     "job",
#     "gap"
# )

# # Match + Gap -> Report

# workflow.add_edge(
#     "match",
#     "report"
# )

# workflow.add_edge(
#     "gap",
#     "report"
# )

# # END

# workflow.add_edge(
#     "report",
#     END
# )

# report_graph = workflow.compile()

from langgraph.graph import (
    END,
    START,
    StateGraph,
)

from app.ai.workflows.report_state import (
    ReportState,
)

from app.ai.nodes.resume_node import (
    resume_node,
)

from app.ai.nodes.job_node import (
    job_node,
)

from app.ai.nodes.match_node import (
    match_node,
)

from app.ai.nodes.gap_node import (
    gap_node,
)

from app.ai.nodes.report_node import (
    report_node,
)

from app.ai.nodes.company_node import (
    company_node,
)

def build_report_graph():

    workflow = StateGraph(
        ReportState
    )

    # Nodes

    workflow.add_node(
        "resume",
        resume_node
    )

    workflow.add_node(
        "job",
        job_node
    )

    workflow.add_node(
        "match",
        match_node
    )

    workflow.add_node(
        "gap",
        gap_node
    )

    workflow.add_node(
        "report",
        report_node
    )

    workflow.add_node(
        "company",
        company_node,
    )

    # START

    workflow.add_edge(
        START,
        "resume"
    )

    workflow.add_edge(
        START,
        "job"
    )

    # Resume + Job → Match

    workflow.add_edge(
        "resume",
        "match"
    )

    workflow.add_edge(
        "resume",
        "gap"
    )

    workflow.add_edge(
        "job",
        "match"
    )

    workflow.add_edge(
        "job",
        "gap"
    )


    workflow.add_edge(
        "job",
        "company"
    )


    # Match + Gap + Company → Final Report

    workflow.add_edge(
        "match",
        "report"
    )

    workflow.add_edge(
        "gap",
        "report"
    )

    workflow.add_edge(
        "company",
        "report"
    )

    # END

    workflow.add_edge(
        "report",
        END
    )

    return workflow.compile()


report_graph = build_report_graph()