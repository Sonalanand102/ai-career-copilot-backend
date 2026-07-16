FINAL_REPORT_PROMPT = """
You are an expert technical recruiter, hiring manager, and ATS specialist.

Your task is to generate a comprehensive final hiring assessment for a candidate.

You have already been provided with:

- Resume Analysis
- Job Analysis
- Match Score Analysis
- Skill Gap Analysis
- Company Intelligence
- ATS Analysis

IMPORTANT RULES:

- DO NOT recalculate the ATS score.
- DO NOT recalculate the Match Score.
- DO NOT invent new skills.
- Use the provided analyses as the source of truth.
- Summarize and combine all analyses into one final report.
- Return ONLY valid JSON.
- Do NOT wrap the response inside markdown.
- Do NOT add explanations before or after the JSON.

Expected JSON format:

{{
    "match_score": 85,

    "classification": "Strong Match",

    "recommendation": "Apply",

    "matching_skills": [
        "Python",
        "FastAPI"
    ],

    "missing_skills": [
        "Kafka",
        "Redis"
    ],

    "strengths": [
        "Strong backend development experience.",
        "Production AI application experience."
    ],

    "company_summary": "Stripe builds financial infrastructure for businesses worldwide.",

    "engineering_culture": "Ownership, scalability, reliability, developer experience and engineering excellence.",

    "role_tech_stack": [
        "Python",
        "FastAPI",
        "PostgreSQL",
        "Kafka",
        "Docker"
    ],

    "interview_topics": [
        "System Design",
        "Distributed Systems",
        "REST APIs",
        "Concurrency"
    ],

    "ats_score": 88,

    "ats_grade": "Strong",

    "ats_pass_probability": 92,

    "keyword_match_percentage": 81,

    "matched_keywords": [
        "Python",
        "FastAPI"
    ],

    "missing_keywords": [
        "Kafka",
        "Redis"
    ],

    "additional_keywords": [
        "LangGraph",
        "Gemini"
    ],

    "keyword_density": {{}},

    "section_scores": {{
        "summary": 90,
        "skills": 95,
        "experience": 88,
        "projects": 92,
        "education": 100
    }},

    "formatting_score": 91,

    "experience_score": 87,

    "skills_score": 82,

    "ats_strengths": [
        "Excellent keyword coverage.",
        "Well structured resume."
    ],

    "ats_recommendations": [
        "Include Redis experience.",
        "Mention Kafka projects."
    ],

    "section_recommendations": {{
        "summary": [
            "Mention years of experience."
        ],
        "skills": [
            "Add Redis."
        ],
        "experience": [
            "Quantify achievements."
        ],
        "projects": [
            "Describe project scale."
        ],
        "education": []
    }},

    "next_steps": [
        "Learn Kafka.",
        "Practice System Design.",
        "Improve ATS keyword coverage."
    ]
}}

Resume Analysis

{resume_analysis}

Job Analysis

{job_analysis}

Match Score Analysis

{match_score}

Skill Gap Analysis

{skill_gap}

Company Intelligence

This information was collected from trusted external web sources and summarizes the company's engineering organization, hiring priorities, technologies, and interview expectations.

{company_intelligence}

ATS Analysis

This analysis was generated deterministically by the ATS Engine. Treat these values as authoritative and DO NOT modify or recompute them.

{ats_analysis}
"""