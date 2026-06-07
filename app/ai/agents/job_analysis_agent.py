from app.ai.prompts.job_analysis_prompt import (
    JOB_ANALYSIS_PROMPT
)

from app.ai.providers.gemini_provider import (
    GeminiProvider
)

from app.ai.schemas.job_analysis_schema import (
    JobAnalysisSchema
)


class JobAnalysisAgent:

    @staticmethod
    def analyze(
        job_description: str
    ) -> JobAnalysisSchema:

        prompt = JOB_ANALYSIS_PROMPT.format(
            job_description=job_description
        )

        return GeminiProvider.generate_structured(
            prompt=prompt,
            schema=JobAnalysisSchema
        )