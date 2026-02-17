import io
import os
import tempfile

import PyPDF2
import docx


def extract_text_from_pdf(file_bytes: bytes) -> str:
    reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def extract_text_from_docx(file_bytes: bytes) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name
    doc = docx.Document(tmp_path)
    os.unlink(tmp_path)
    return "\n".join(para.text for para in doc.paragraphs if para.text.strip())


def extract_text_from_txt(file_bytes: bytes) -> str:
    return file_bytes.decode("utf-8", errors="ignore")


def extract_text(file_bytes: bytes, extension: str) -> str:
    """Dispatch to the correct extractor based on file extension."""
    ext = extension.lower()
    if ext == "pdf":
        return extract_text_from_pdf(file_bytes)
    elif ext == "docx":
        return extract_text_from_docx(file_bytes)
    else:
        return extract_text_from_txt(file_bytes)
