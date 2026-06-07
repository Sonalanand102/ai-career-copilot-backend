from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.models.resume import ResumeStatus
from typing import Optional

class ResumeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, resume: Resume) -> Resume:
        self.db.add(resume)
        self.db.commit()
        self.db.refresh(resume)
        return resume

    def get_by_id(self, resume_id: UUID) -> Optional[Resume]:
        stmt = select(Resume).where(Resume.id == resume_id)
        return self.db.scalar(stmt)

    def update_status(
        self,
        resume: Resume,
        status: ResumeStatus,
        error_message: Optional[str] = None,
    ) -> Resume:
        resume.status = status
        resume.error_message = error_message

        self.db.commit()
        self.db.refresh(resume)

        return resume

    def update_raw_text(
        self,
        resume: Resume,
        raw_text: str,
    ) -> Resume:
        resume.raw_text = raw_text

        self.db.commit()
        self.db.refresh(resume)

        return resume

    def update_parsed_content(
        self,
        resume: Resume,
        raw_text: str,
        parsed_content: dict,
    ) -> Resume:

        resume.raw_text = raw_text
        resume.parsed_content = parsed_content
        resume.status = ResumeStatus.COMPLETED
        resume.error_message = None

        self.db.commit()
        self.db.refresh(resume)

        return resume