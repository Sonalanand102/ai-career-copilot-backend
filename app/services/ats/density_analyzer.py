from collections import Counter


class DensityAnalyzer:

    @staticmethod
    def analyze(
        candidate_frequency: Counter,
        required_frequency: Counter,
    ) -> dict:

        density = {}

        for keyword, required_count in required_frequency.items():

            candidate_count = candidate_frequency.get(
                keyword,
                0,
            )

            coverage = round(
                (
                    candidate_count
                    / required_count
                ) * 100,
                2,
            )

            density[keyword] = {
                "required_count": required_count,
                "candidate_count": candidate_count,
                "coverage": coverage,
            }

        overused_keywords = []

        underrepresented_keywords = []

        for keyword, values in density.items():

            if values["coverage"] > 150:
                overused_keywords.append(keyword)

            elif values["coverage"] < 50:
                underrepresented_keywords.append(keyword)

        average_density = round(
            sum(
                value["coverage"]
                for value in density.values()
            )
            / len(density),
            2,
        ) if density else 100

        return {
            "average_density": average_density,
            "keyword_density": density,
            "overused_keywords": overused_keywords,
            "underrepresented_keywords": underrepresented_keywords,
        }