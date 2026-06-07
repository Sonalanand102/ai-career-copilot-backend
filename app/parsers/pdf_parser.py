import fitz


class PDFParser:

    @staticmethod
    def extract_text(
        file_url: str,
    ) -> str:

        document = fitz.open(file_url)

        pages = []

        for page in document:
            pages.append(page.get_text())

        document.close()

        return "\n".join(pages)