from tavily import TavilyClient

from app.core.config import settings


class TavilyProvider:

    client = TavilyClient(
        api_key=settings.TAVILY_API_KEY
    )

    @classmethod
    def search_role_context(
        cls,
        company_name: str,
        job_title: str,
        required_skills: list[str]
    ) -> dict:

        skills = " ".join(required_skills)

        query = (
            f"{company_name} "
            f"{job_title} "
            f"{skills} "
            "engineering blog "
            "technology stack "
            "backend engineering "
            "software engineering "
            "recent engineering news "
            "hiring"
        )

        print("=" * 80)
        print(f"Tavily Query:\n{query}")

        try:

            response = cls.client.search(
                query=query,
                search_depth="advanced",
                max_results=5,
                include_answer=True,
                include_raw_content=True
            )

            print(
                f"Results Found : {len(response.get('results', []))}"
            )

            return response

        except Exception as e:

            raise RuntimeError(
                f"Tavily Search Failed : {e}"
            )