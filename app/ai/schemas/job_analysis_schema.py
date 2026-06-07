from pydantic import BaseModel


class JobAnalysisSchema(BaseModel):

    job_title: str

    required_skills: list[str]

    preferred_skills: list[str]

    experience_required: str

    keywords: list[str]