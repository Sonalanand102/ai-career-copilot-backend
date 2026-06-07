import json
import re

from app.ai.prompts.resume_parser_prompt import PROMPT
from app.ai.providers.gemini_provider import GeminiProvider
from app.ai.schemas.resume_schema import ResumeSchema


class ResumeParserAgent:

    @staticmethod
    def _extract_json(response: str) -> str:
        text = response.strip()

        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?\s*", "", text)
            text = re.sub(r"\s*```$", "", text)

        return text.strip()

    @classmethod
    def parse(
        cls,
        resume_text: str
    ) -> ResumeSchema:

        prompt = PROMPT.format(
            resume_text=resume_text
        )

        response = GeminiProvider.generate(
            prompt
        )

        data = json.loads(
            cls._extract_json(response)
        )

        return ResumeSchema.model_validate(data)