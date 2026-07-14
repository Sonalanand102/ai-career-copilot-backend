from pydantic import BaseModel
from pydantic import Field


class CompanyIntelligenceSchema(BaseModel):

    company_name: str

    website: str

    industry: str

    company_summary: str

    engineering_culture: str

    role_tech_stack: list[str] = Field(
        default_factory=list
    )

    hiring_focus: list[str] = Field(
        default_factory=list
    )

    interview_topics: list[str] = Field(
        default_factory=list
    )

    recent_news: list[str] = Field(
        default_factory=list
    )