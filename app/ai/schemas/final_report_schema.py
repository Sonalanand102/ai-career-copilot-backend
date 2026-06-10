from pydantic import BaseModel


class FinalReportSchema(BaseModel):

    match_score: int

    classification: str

    recommendation: str

    matching_skills: list[str]

    missing_skills: list[str]

    strengths: list[str]

    next_steps: list[str]