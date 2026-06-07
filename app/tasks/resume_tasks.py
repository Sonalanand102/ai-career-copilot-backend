from uuid import UUID

from app.db.session import SessionLocal
from app.models.resume import ResumeStatus
from app.parsers.pdf_parser import PDFParser
from app.repositories.resume_repository import ResumeRepository
from app.ai.agents.resume_parser_agent import ResumeParserAgent


def process_resume(resume_id: str):

    db = SessionLocal()

    try:
        repository = ResumeRepository(db)

        resume = repository.get_by_id(
            UUID(resume_id)
        )

        if not resume:
            return

        repository.update_status(
            resume,
            ResumeStatus.PROCESSING
        )

        raw_text = PDFParser.extract_text(
            resume.file_url
        )

        repository.update_raw_text(
            resume,
            raw_text,
        )

        parsed_content = (
            ResumeParserAgent
            .parse(raw_text)
            .model_dump()
        )

        repository.update_parsed_content(
            resume,
            raw_text,
            parsed_content
        )

    except Exception as e:

        if resume:
            repository.update_status(
                resume,
                ResumeStatus.FAILED,
                str(e)
            )

        raise

    finally:
        db.close()