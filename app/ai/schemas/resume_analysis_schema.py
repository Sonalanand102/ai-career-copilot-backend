from pydantic import BaseModel


class ResumeAnalysisSchema(BaseModel):

    candidate_skills: list[str]

    years_of_experience: str

    experience_summary: str

    projects_summary: str