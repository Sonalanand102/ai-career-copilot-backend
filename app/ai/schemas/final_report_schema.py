# from pydantic import BaseModel


# class FinalReportSchema(BaseModel):

#     match_score: int

#     classification: str

#     recommendation: str

#     matching_skills: list[str]

#     missing_skills: list[str]

#     strengths: list[str]

#     next_steps: list[str]

from pydantic import BaseModel
from pydantic import Field


class FinalReportSchema(BaseModel):

    match_score: int

    classification: str

    recommendation: str

    matching_skills: list[str] = Field(
        default_factory=list
    )

    missing_skills: list[str] = Field(
        default_factory=list
    )

    strengths: list[str] = Field(
        default_factory=list
    )

    company_summary: str

    engineering_culture: str

    role_tech_stack: list[str] = Field(
        default_factory=list
    )

    interview_topics: list[str] = Field(
        default_factory=list
    )

    next_steps: list[str] = Field(
        default_factory=list
    )