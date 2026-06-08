MATCH_SCORE_PROMPT = """
You are an expert recruiter.

Compare the resume analysis and job analysis.

Evaluate:

- Skill alignment
- Experience alignment
- Project relevance

Return ONLY valid JSON.

Expected format:

{{
  "match_score": 85,
  "classification": "Strong Match",
  "recommendation": "Apply"
}}

Resume Analysis:

{resume_analysis}

Job Analysis:

{job_analysis}
"""