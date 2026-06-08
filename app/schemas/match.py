from pydantic import BaseModel
from uuid import UUID


class MatchRequest(BaseModel):

    resume_id: UUID

    job_description: str