from pydantic import BaseModel


class MatchScoreSchema(BaseModel):

    match_score: int

    classification: str

    recommendation: str