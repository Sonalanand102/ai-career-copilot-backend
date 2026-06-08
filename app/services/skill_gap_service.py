from app.ai.prompts.skill_gap_prompt import (
    SKILL_GAP_PROMPT
)

from app.ai.providers.gemini_provider import (
    GeminiProvider
)

from app.ai.schemas.skill_gap_schema import (
    SkillGapSchema
)


class SkillGapService:

    @staticmethod
    def analyze(
        resume_analysis,
        job_analysis
    ):

        prompt = SKILL_GAP_PROMPT.format(
            resume_analysis=resume_analysis,
            job_analysis=job_analysis
        )

        return GeminiProvider.generate_structured(
            prompt=prompt,
            schema=SkillGapSchema
        )