from app.ai.prompts.match_score_prompt import (
    MATCH_SCORE_PROMPT
)

from app.ai.providers.gemini_provider import (
    GeminiProvider
)

from app.ai.schemas.match_score_schema import (
    MatchScoreSchema
)


class MatchScoreService:

    @staticmethod
    def analyze(
        resume_analysis,
        job_analysis
    ):

        prompt = MATCH_SCORE_PROMPT.format(
            resume_analysis=resume_analysis,
            job_analysis=job_analysis
        )

        return GeminiProvider.generate_structured(
            prompt=prompt,
            schema=MatchScoreSchema
        )