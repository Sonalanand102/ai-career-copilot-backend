# # from typing import TypedDict


# # class ReportState(
# #     TypedDict,
# #     total=False
# # ):
# #     resume

# #     job_description

# #     resume_analysis

# #     job_analysis

# #     match_score

# #     skill_gap

# #     final_report

# from typing import Any, TypedDict


# class ReportState(TypedDict, total=False):
#     resume: dict[str, Any]
#     job_description: str
#     resume_analysis: dict[str, Any]
#     job_analysis: dict[str, Any]
#     match_score: float
#     skill_gap: list[str]
#     final_report: dict[str, Any]

from typing import Any
from typing_extensions import TypedDict


from app.ai.schemas.resume_analysis_schema import (
    ResumeAnalysisSchema,
)

from app.ai.schemas.job_analysis_schema import (
    JobAnalysisSchema,
)

from app.ai.schemas.match_score_schema import (
    MatchScoreSchema,
)

from app.ai.schemas.skill_gap_schema import (
    SkillGapSchema,
)

from app.ai.schemas.company_intelligence_schema import (
    CompanyIntelligenceSchema,
)

from app.ai.schemas.final_report_schema import (
    FinalReportSchema,
)


class ReportState(TypedDict, total=False):
    """
    Shared state passed between LangGraph nodes.
    """

    # Input
    parsed_resume: dict[str, Any]
    job_description: str

    # Node Outputs
    resume_analysis: ResumeAnalysisSchema
    job_analysis: JobAnalysisSchema
    match_score: MatchScoreSchema
    skill_gap: SkillGapSchema
    company_intelligence: CompanyIntelligenceSchema
    final_report: FinalReportSchema