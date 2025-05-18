from pydantic import BaseModel

class PDFInfoResponse(BaseModel):
    num_pages: int
    preview_text: str