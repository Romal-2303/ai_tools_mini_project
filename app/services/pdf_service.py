import fitz
from typing import Tuple
from fastapi import UploadFile

def extract_pdf_info(receivedFile: UploadFile) -> Tuple[int, str]:
    contents = receivedFile.file.read()
    with fitz.open(stream=contents, filetype="pdf") as doc:
        num_pages = len(doc)
        text = ""
        for page in doc:
            text += page.get_text()
        preview = text[:300]
    return num_pages, preview
