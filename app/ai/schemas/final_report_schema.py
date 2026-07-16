from pydantic import BaseModel
from pydantic import Field


class FinalReportSchema(BaseModel):

    # ===============================
    # Match Analysis
    # ===============================

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

    # ===============================
    # Company Intelligence
    # ===============================

    company_summary: str

    engineering_culture: str

    role_tech_stack: list[str] = Field(
        default_factory=list
    )

    interview_topics: list[str] = Field(
        default_factory=list
    )

    # ===============================
    # ATS Analysis
    # ===============================

    ats_score: int

    ats_grade: str

    ats_pass_probability: int

    keyword_match_percentage: int

    matched_keywords: list[str] = Field(
        default_factory=list
    )

    missing_keywords: list[str] = Field(
        default_factory=list
    )

    additional_keywords: list[str] = Field(
        default_factory=list
    )

    keyword_density: dict[str, dict] = Field(
        default_factory=dict
    )

    section_scores: dict[str, int] = Field(
        default_factory=dict
    )

    formatting_score: int

    experience_score: int

    skills_score: int

    ats_strengths: list[str] = Field(
        default_factory=list
    )

    ats_recommendations: list[str] = Field(
        default_factory=list
    )

    section_recommendations: dict[str, list[str]] = Field(
        default_factory=dict
    )

    # ===============================
    # Final Action Plan
    # ===============================

    next_steps: list[str] = Field(
        default_factory=list
    )