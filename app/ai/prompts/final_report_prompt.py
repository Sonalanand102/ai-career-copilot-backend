FINAL_REPORT_PROMPT = """
You are an expert recruiter.

Using the provided analyses, generate a final candidate assessment report.

Return ONLY valid JSON.

Expected format:

{{
  "match_score":85,
  "classification":"Strong Match",
  "recommendation":"Apply",

  "matching_skills":[
    "Python"
  ],

  "missing_skills":[
    "AWS"
  ],

  "strengths":[
    "Strong backend experience"
  ],

  "company_summary":"Stripe builds financial infrastructure...",

  "engineering_culture":"Ownership, scalability and engineering excellence.",

  "role_tech_stack":[
    "Python",
    "Kafka",
    "Docker"
  ],

  "interview_topics":[
    "System Design",
    "Distributed Systems",
    "REST APIs"
  ],

  "next_steps":[
    "Learn Kafka",
    "Practice System Design"
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

Company Intelligence

This information was collected from external web sources and summarizes the company's engineering organization, hiring priorities and technologies relevant to this role.

{company_intelligence}
"""