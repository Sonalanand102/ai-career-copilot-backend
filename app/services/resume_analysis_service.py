from app.ai.prompts.resume_analysis_prompt import (
    RESUME_ANALYSIS_PROMPT
)

from app.ai.providers.gemini_provider import (
    GeminiProvider
)

from app.ai.schemas.resume_analysis_schema import (
    ResumeAnalysisSchema
)


class ResumeAnalysisService:

    @staticmethod
    def analyze(
        parsed_resume: dict
    ) -> ResumeAnalysisSchema:

        prompt = RESUME_ANALYSIS_PROMPT.format(
            parsed_resume=parsed_resume
        )

        return GeminiProvider.generate_structured(
            prompt=prompt,
            schema=ResumeAnalysisSchema
        )