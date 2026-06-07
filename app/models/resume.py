import uuid
from enum import Enum as PyEnum

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Enum as SQLEnum

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import Base
from app.models.mixins import TimestampMixin


class ResumeStatus(str, PyEnum):
    UPLOADED = "UPLOADED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Resume(Base, TimestampMixin):

    __tablename__ = "resumes"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    original_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    file_url: Mapped[str] = mapped_column(
        Text
    )

    raw_text: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    parsed_content: Mapped[dict] = mapped_column(
        JSONB,
        nullable=True
    )

    status: Mapped[ResumeStatus] = mapped_column(
        SQLEnum(ResumeStatus, name="resume_status"),
        nullable=False,
        default=ResumeStatus.UPLOADED
    )

    error_message: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )
