from pydantic import BaseModel


class SkillGapSchema(BaseModel):

    matching_skills: list[str]

    missing_skills: list[str]

    additional_skills: list[str]

    gap_severity: str