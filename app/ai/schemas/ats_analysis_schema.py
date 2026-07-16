from pydantic import BaseModel


class ATSAnalysisSchema(BaseModel):

    ats_score: int

    grade: str

    ats_pass_probability: int

    keyword_match_percentage: int

    matched_keywords: list[str]

    missing_keywords: list[str]

    additional_keywords: list[str]

    keyword_density: dict[str, dict]

    section_scores: dict[str, int]

    formatting_score: int

    experience_score: int

    skills_score: int

    strengths: list[str]

    recommendations: list[str]

    section_recommendations: dict[str, list[str]]