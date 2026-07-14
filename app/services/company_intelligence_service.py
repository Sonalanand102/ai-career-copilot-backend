import json
import logging

from app.ai.prompts.company_intelligence_prompt import (
    COMPANY_INTELLIGENCE_PROMPT,
)

from app.ai.providers.gemini_provider import (
    GeminiProvider,
)

from app.ai.providers.tavily_provider import (
    TavilyProvider,
)

from app.ai.schemas.company_intelligence_schema import (
    CompanyIntelligenceSchema,
)


logger = logging.getLogger(__name__)


class CompanyIntelligenceService:

    @staticmethod
    def analyze(
        job_analysis,
    ) -> CompanyIntelligenceSchema:

        logger.info("=" * 80)
        logger.info("Starting Company Intelligence")

        try:

            company_name = job_analysis.company_name
            job_title = job_analysis.job_title
            required_skills = job_analysis.required_skills

            logger.info(
                f"Company      : {company_name}"
            )

            logger.info(
                f"Job Title    : {job_title}"
            )

            logger.info(
                f"Skills       : {required_skills}"
            )

            logger.info(
                "Searching Tavily..."
            )

            search_results = (
                TavilyProvider.search_role_context(
                    company_name=company_name,
                    job_title=job_title,
                    required_skills=required_skills,
                )
            )

            logger.info(
                f"Found {len(search_results.get('results', []))} search results"
            )

            formatted_results = {
                "answer": search_results.get(
                    "answer",
                    "",
                ),
                "results": [
                    {
                        "title": result.get("title"),
                        "url": result.get("url"),
                        "content": result.get("content"),
                        "raw_content": result.get("raw_content"),
                    }
                    for result in search_results.get(
                        "results",
                        [],
                    )
                ],
            }

            logger.info(
                "Creating prompt..."
            )

            prompt = COMPANY_INTELLIGENCE_PROMPT.format(
                company_name=company_name,
                job_title=job_title,
                required_skills=", ".join(
                    required_skills
                ),
                search_results=json.dumps(
                    formatted_results,
                    indent=2,
                ),
            )

            logger.info(
                "Prompt created successfully."
            )

            logger.info(
                "Calling Gemini..."
            )

            response = (
                GeminiProvider.generate_structured(
                    prompt=prompt,
                    schema=CompanyIntelligenceSchema,
                )
            )

            logger.info(
                "Company Intelligence generated successfully."
            )

            return response

        except Exception as e:

            logger.exception(
                "Company Intelligence failed."
            )

            raise RuntimeError(
                f"Company Intelligence failed: {e}"
            ) from e