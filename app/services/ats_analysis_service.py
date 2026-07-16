from app.ai.schemas.ats_analysis_schema import (
    ATSAnalysisSchema,
)

from app.services.ats.keyword_matcher import (
    KeywordMatcher,
)

from app.services.ats.density_analyzer import (
    DensityAnalyzer,
)

from app.services.ats.ats_score_calculator import (
    ATSScoreCalculator,
)

from app.services.ats.section_analyzer import (
    SectionAnalyzer,
)

class ATSAnalysisService:

    @staticmethod
    def analyze(
        resume_analysis,
        job_analysis,
    ) -> ATSAnalysisSchema:

        # ----------------------------------------
        # Candidate & Job Skills
        # ----------------------------------------

        candidate_skills = (
            resume_analysis.candidate_skills
        )

        required_skills = (
            job_analysis.required_skills
        )

        # ----------------------------------------
        # Keyword Analysis
        # ----------------------------------------

        keyword_analysis = (
            KeywordMatcher.analyze(
                candidate_skills,
                required_skills,
            )
        )

        # ----------------------------------------
        # Density Analysis
        # ----------------------------------------

        density_analysis = (
            DensityAnalyzer.analyze(
                keyword_analysis["candidate_frequency"],
                keyword_analysis["required_frequency"],
            )
        )

        # ----------------------------------------
        # Section Analysis
        # (Temporary - we'll improve later)
        # ----------------------------------------

        section_analysis = SectionAnalyzer.analyze(
            resume_analysis
        )

        # ----------------------------------------
        # ATS Score
        # ----------------------------------------

        score = ATSScoreCalculator.calculate(
            keyword_match_percentage=keyword_analysis[
                "coverage_percentage"
            ],
            average_density=density_analysis[
                "average_density"
            ],
            section_scores=section_analysis["section_scores"],
        )

        # ----------------------------------------
        # Recommendations
        # ----------------------------------------

        recommendations = []

        if keyword_analysis["missing_keywords"]:
            recommendations.append(
                "Include more job-specific keywords."
            )

        if density_analysis[
            "underrepresented_keywords"
        ]:
            recommendations.append(
                "Increase the emphasis on important technical skills."
            )

        recommendations.append(
            "Tailor your resume for each application."
        )

        # ----------------------------------------
        # Strengths
        # ----------------------------------------

        strengths = []

        if (
            keyword_analysis[
                "coverage_percentage"
            ] >= 70
        ):
            strengths.append(
                "Good keyword alignment."
            )

        if (
            score["ats_score"] >= 80
        ):
            strengths.append(
                "Strong ATS compatibility."
            )

        if (
            keyword_analysis[
                "additional_keywords"
            ]
        ):
            strengths.append(
                "Contains additional relevant skills."
            )

        # ----------------------------------------
        # Section Recommendations
        # ----------------------------------------

        section_recommendations = {
            "summary": [
                "Mention years of experience."
            ],
            "skills": [
                "Add missing technical skills."
            ],
            "experience": [
                "Quantify achievements."
            ],
            "projects": [
                "Highlight business impact."
            ],
            "education": [],
        }

        # ----------------------------------------
        # Final Schema
        # ----------------------------------------

        return ATSAnalysisSchema(

            ats_score=score["ats_score"],

            grade=score["grade"],

            ats_pass_probability=score[
                "ats_pass_probability"
            ],

            keyword_match_percentage=keyword_analysis[
                "coverage_percentage"
            ],

            matched_keywords=keyword_analysis[
                "matched_keywords"
            ],

            missing_keywords=keyword_analysis[
                "missing_keywords"
            ],

            additional_keywords=keyword_analysis[
                "additional_keywords"
            ],

            keyword_density=density_analysis[
                "keyword_density"
            ],

            section_scores=section_analysis["section_scores"],

            formatting_score=score[
                "section_average"
            ],

            experience_score=80,

            skills_score=keyword_analysis[
                "coverage_percentage"
            ],

            strengths=strengths,

            recommendations=recommendations,

            section_recommendations=section_analysis["section_recommendations"],
        )