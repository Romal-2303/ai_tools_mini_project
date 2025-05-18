from fastapi import APIRouter, UploadFile, File, HTTPException
from schemas import pdf_model
from services.pdf_service import extract_pdf_info


router = APIRouter()

@router.post("/upload/pdf-info", response_model=pdf_model.PDFInfoResponse)
def pdf_info(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only pdf files are allowed")
    
    num_pages, preview_text = extract_pdf_info(file)
    
    return {'num_pages': num_pages, "preview_text": preview_text}