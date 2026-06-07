"""create resumes table

Revision ID: 62e444931a7f
Revises: b7650e545bee
Create Date: 2026-06-06 01:37:18.675694

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "62e444931a7f"
down_revision: Union[str, Sequence[str], None] = "b7650e545bee"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    resume_status = postgresql.ENUM(
        "UPLOADED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
        name="resume_status",
    )

    resume_status.create(
        op.get_bind(),
        checkfirst=True,
    )

    op.add_column(
        "resumes",
        sa.Column(
            "original_filename",
            sa.String(length=255),
            nullable=False,
        ),
    )

    op.add_column(
        "resumes",
        sa.Column(
            "status",
            resume_status,
            nullable=False,
            server_default="UPLOADED",
        ),
    )

    op.add_column(
        "resumes",
        sa.Column(
            "error_message",
            sa.Text(),
            nullable=True,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column("resumes", "error_message")
    op.drop_column("resumes", "status")
    op.drop_column("resumes", "original_filename")

    resume_status = postgresql.ENUM(
        "UPLOADED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
        name="resume_status",
    )

    resume_status.drop(
        op.get_bind(),
        checkfirst=True,
    )