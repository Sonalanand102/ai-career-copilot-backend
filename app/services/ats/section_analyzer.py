class SectionAnalyzer:

    @staticmethod
    def analyze(
        resume_analysis,
    ) -> dict:

        scores = {}

        recommendations = {}

        # -----------------------------
        # Summary
        # -----------------------------

        summary = (
            resume_analysis.experience_summary or ""
        ).strip()

        if summary:

            scores["summary"] = 100

            recommendations["summary"] = []

        else:

            scores["summary"] = 40

            recommendations["summary"] = [
                "Add a professional summary."
            ]

        # -----------------------------
        # Skills
        # -----------------------------

        skills = (
            resume_analysis.candidate_skills
        )

        if len(skills) >= 10:

            scores["skills"] = 100

            recommendations["skills"] = []

        elif len(skills) >= 5:

            scores["skills"] = 80

            recommendations["skills"] = [
                "Add more relevant technical skills."
            ]

        else:

            scores["skills"] = 50

            recommendations["skills"] = [
                "Expand your skills section."
            ]

        # -----------------------------
        # Experience
        # -----------------------------

        if summary:

            scores["experience"] = 90

            recommendations["experience"] = [
                "Quantify business impact."
            ]

        else:

            scores["experience"] = 50

            recommendations["experience"] = [
                "Improve your work experience descriptions."
            ]

        # -----------------------------
        # Projects
        # -----------------------------

        projects = (
            resume_analysis.projects_summary or ""
        ).strip()

        if projects:

            scores["projects"] = 100

            recommendations["projects"] = []

        else:

            scores["projects"] = 40

            recommendations["projects"] = [
                "Add more project details."
            ]

        # -----------------------------
        # Education
        # -----------------------------

        scores["education"] = 100

        recommendations["education"] = []

        return {

            "section_scores": scores,

            "section_recommendations": recommendations,

        }