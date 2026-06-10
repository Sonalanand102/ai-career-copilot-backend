FINAL_REPORT_PROMPT = """
You are an expert recruiter.

Using the provided analyses, generate a final candidate assessment report.

Return ONLY valid JSON.

Expected format:

{{
  "match_score": 85,
  "classification": "Strong Match",
  "recommendation": "Apply",
  "matching_skills": ["Python"],
  "missing_skills": ["AWS"],
  "strengths": [
    "Strong backend experience"
  ],
  "next_steps": [
    "Learn AWS",
    "Learn Docker"
  ]
}}

Resume Analysis:

{resume_analysis}

Job Analysis:

{job_analysis}

Match Score:

{match_score}

Skill Gap:

{skill_gap}
"""