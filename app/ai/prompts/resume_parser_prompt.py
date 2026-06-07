PROMPT = """
You are an expert resume parser.

Extract information from the resume.

Return ONLY valid JSON.

Schema:

{{
  "skills": [],
  "projects": [],
  "experience": [],
  "education": [],
  "certifications": [],
  "achievements": []
}}

Resume:

{resume_text}
"""