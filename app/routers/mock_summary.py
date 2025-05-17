from fastapi import APIRouter
from schemas import summary

router = APIRouter()


@router.post("/mock-summarizer", response_model=summary.SummaryResponse) ## This tells FastAPI: “When this endpoint returns a response, it must follow the shape (schema) defined in SummaryResponse.
def mock_summarizer(request: summary.TextRequest):
    return {
        "summary": "This is a fake summary.", 
        "sentText": f"{request.text}"
        }