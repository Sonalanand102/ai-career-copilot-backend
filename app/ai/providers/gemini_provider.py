import json
import re

import google.generativeai as genai

from pydantic import BaseModel

from app.core.config import settings


genai.configure(
    api_key=settings.GEMINI_API_KEY
)


class GeminiProvider:

    model = genai.GenerativeModel(
        "gemini-3-flash-preview"
    )

    @classmethod
    def generate(
        cls,
        prompt: str
    ) -> str:

        response = cls.model.generate_content(
            prompt
        )

        return response.text

    @classmethod
    def generate_structured(
        cls,
        prompt: str,
        schema: type[BaseModel]
    ):

        response = cls.model.generate_content(
            prompt
        )

        content = response.text.strip()

        # Remove markdown fences
        content = re.sub(
            r"```json",
            "",
            content,
            flags=re.IGNORECASE
        )

        content = re.sub(
            r"```",
            "",
            content
        )

        # Extract JSON object
        start = content.find("{")
        end = content.rfind("}")

        if start == -1 or end == -1:
            raise ValueError(
                "No JSON object found in Gemini response"
            )

        content = content[start:end + 1]

        data = json.loads(content)

        return schema.model_validate(
            data
        )