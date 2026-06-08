SKILL_GAP_PROMPT = """
You are an expert recruiter.

Compare the resume analysis and the job analysis.

Identify:

1. Matching skills
2. Missing skills
3. Additional candidate skills
4. Gap severity

Gap severity should be one of:

- LOW
- MEDIUM
- HIGH

Return ONLY valid JSON.

Expected format:

{{
  "matching_skills": [
    "Python"
  ],
  "missing_skills": [
    "AWS"
  ],
  "additional_skills": [
    "Android"
  ],
  "gap_severity": "MEDIUM"
}}

Resume Analysis:

{resume_analysis}

Job Analysis:

{job_analysis}
"""