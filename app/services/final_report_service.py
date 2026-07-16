from app.ai.prompts.final_report_prompt import (
    FINAL_REPORT_PROMPT
)

from app.ai.providers.gemini_provider import (
    GeminiProvider
)

from app.ai.schemas.final_report_schema import (
    FinalReportSchema
)

# class FinalReportService:

#     @staticmethod
#     def analyze(
#         resume_analysis,
#         job_analysis,
#         match_score,
#         skill_gap
#     ):

#         prompt = FINAL_REPORT_PROMPT.format(
#             resume_analysis=resume_analysis,
#             job_analysis=job_analysis,
#             match_score=match_score,
#             skill_gap=skill_gap
#         )

#         return GeminiProvider.generate_structured(
#             prompt=prompt,
#             schema=FinalReportSchema
#         )

class FinalReportService:

    @staticmethod
    def analyze(
        resume_analysis,
        job_analysis,
        match_score,
        skill_gap,
        company_intelligence,
        ats_analysis
    ):

        prompt = FINAL_REPORT_PROMPT.format(

            resume_analysis=resume_analysis,

            job_analysis=job_analysis,

            match_score=match_score,

            skill_gap=skill_gap,

            company_intelligence=company_intelligence,

            ats_analysis=ats_analysis
        )

        return GeminiProvider.generate_structured(
            prompt=prompt,
            schema=FinalReportSchema,
        )