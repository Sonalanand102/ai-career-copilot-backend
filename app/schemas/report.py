from uuid import UUID

from pydantic import BaseModel


class ReportRequest(BaseModel):

    resume_id: UUID

    job_description: str