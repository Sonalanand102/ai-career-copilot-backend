JOB_ANALYSIS_PROMPT = """
You are an expert technical recruiter.

Analyze the following job description and extract:

1. Job Title
2. Company Name
2. Required Skills
3. Preferred Skills
4. Experience Required
5. Important ATS Keywords

IMPORTANT RULES:

- Return ONLY a valid JSON object.
- Do NOT wrap the JSON in markdown.
- Do NOT use ```json.
- Do NOT include explanations.
- Do NOT include notes.
- Do NOT include any text before or after the JSON.
- All skills must be returned as arrays of strings.
- If the company name is not mentioned in the job description, return an empty string ("") for the company name. DO NOT guess or hallucinate the company name.

Expected JSON format:

{{
  "company_name": "Tech Solutions Inc.",
  "job_title": "Backend Engineer",
  "required_skills": [
    "Python",
    "FastAPI"
  ],
  "preferred_skills": [
    "Docker",
    "AWS"
  ],
  "experience_required": "2+ years",
  "keywords": [
    "REST API",
    "Microservices"
  ]
}}

Job Description:

{job_description}
"""