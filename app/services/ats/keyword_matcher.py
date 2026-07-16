from collections import Counter


class KeywordMatcher:

    @staticmethod
    def analyze(
        candidate_skills: list[str],
        required_skills: list[str],
    ) -> dict:

        candidate = [
            skill.strip().lower()
            for skill in candidate_skills
        ]

        required = [
            skill.strip().lower()
            for skill in required_skills
        ]

        candidate_set = set(candidate)
        required_set = set(required)

        matched_keywords = sorted(
            candidate_set & required_set
        )

        missing_keywords = sorted(
            required_set - candidate_set
        )

        additional_keywords = sorted(
            candidate_set - required_set
        )

        coverage_percentage = (
            round(
                len(matched_keywords)
                / len(required_set)
                * 100
            )
            if required_set
            else 100
        )

        return {
            "matched_keywords": matched_keywords,
            "missing_keywords": missing_keywords,
            "additional_keywords": additional_keywords,
            "coverage_percentage": coverage_percentage,
            "candidate_frequency": Counter(candidate),
            "required_frequency": Counter(required),
        }