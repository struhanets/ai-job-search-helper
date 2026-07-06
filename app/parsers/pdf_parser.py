import fitz
import logging

logger = logging.getLogger(__name__)


class PDFParser:
    @staticmethod
    def extract_text(file_content: bytes) -> str:
        try:
            doc = fitz.open(stream=file_content, filetype="pdf")
            text = ""
            for page in doc:
                text += page.get_text()
            return text
        except Exception as e:
            logger.error(f"Error extracting text from PDF: {e}")
            raise
