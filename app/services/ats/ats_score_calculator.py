class ATSScoreCalculator:

    KEYWORD_WEIGHT = 0.50
    DENSITY_WEIGHT = 0.30
    SECTION_WEIGHT = 0.20

    @classmethod
    def calculate(
        cls,
        keyword_match_percentage: int,
        average_density: float,
        section_scores: dict[str, int],
    ) -> dict:

        section_average = (
            sum(section_scores.values())
            / len(section_scores)
            if section_scores
            else 100
        )

        ats_score = round(

            keyword_match_percentage * cls.KEYWORD_WEIGHT +

            average_density * cls.DENSITY_WEIGHT +

            section_average * cls.SECTION_WEIGHT

        )

        ats_score = max(
            0,
            min(
                ats_score,
                100,
            ),
        )

        if ats_score >= 90:
            grade = "Excellent"

        elif ats_score >= 80:
            grade = "Strong"

        elif ats_score >= 70:
            grade = "Good"

        elif ats_score >= 60:
            grade = "Average"

        else:
            grade = "Poor"

        ats_pass_probability = min(
            ats_score + 5,
            100,
        )

        return {
            "ats_score": ats_score,
            "ats_pass_probability": ats_pass_probability,
            "grade": grade,
            "section_average": round(
                section_average,
                2,
            ),
        }