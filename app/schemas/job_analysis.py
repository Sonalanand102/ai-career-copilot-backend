from pydantic import BaseModel


class JobAnalysisRequest(BaseModel):
    job_description: str