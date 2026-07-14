from uuid import UUID

from app.db.session import SessionLocal
from app.models.resume import ResumeStatus
from app.parsers.pdf_parser import PDFParser
from app.repositories.resume_repository import ResumeRepository
from app.ai.agents.resume_parser_agent import ResumeParserAgent


def process_resume(resume_id: str):

    print("=" * 80)
    print(f"Processing resume with ID: {resume_id}")

    db = SessionLocal()

    try:
        repository = ResumeRepository(db)

        resume = repository.get_by_id(
            UUID(resume_id)
        )

        print("Resume Loaded")

        if not resume:
            print("Resume not loaded")
            return

        repository.update_status(
            resume,
            ResumeStatus.PROCESSING
        )

        print("✅ Status Updated -> PROCESSING")

        raw_text = PDFParser.extract_text(
            resume.file_url
        )

        print("✅ PDF Extracted")
        print(f"Raw text length: {len(raw_text)}")
        print(raw_text[:500])

        repository.update_raw_text(
            resume,
            raw_text,
        )

        print("✅ Raw Text Saved")

        print("🚀 Calling ResumeParserAgent...")

        parsed_content = (
            ResumeParserAgent
            .parse(raw_text)
            .model_dump()
        )

        print("✅ Gemini Returned")
        print(parsed_content)

        repository.update_parsed_content(
            resume,
            raw_text,
            parsed_content
        )

        print("✅ Parsed Content Saved")

    except Exception as e:

        print("❌ Exception")
        print(type(e))
        print(e)


        if resume:
            repository.update_status(
                resume,
                ResumeStatus.FAILED,
                str(e)
            )

        raise

    finally:
        db.close()