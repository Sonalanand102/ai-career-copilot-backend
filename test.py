from app.parsers.pdf_parser import PDFParser
from app.ai.agents.resume_parser_agent import ResumeParserAgent

text = PDFParser.extract_text(
    "storage/resumes/sample.pdf"
)

parsed = ResumeParserAgent.parse(text)

print(parsed.model_dump())