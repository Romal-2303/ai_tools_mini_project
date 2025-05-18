from fastapi import APIRouter
from schemas import summary_model

router = APIRouter()


@router.post("/mock-summarizer", response_model=summary_model.SummaryResponse) ## This tells FastAPI: “When this endpoint returns a response, it must follow the shape (schema) defined in SummaryResponse.
def mock_summarizer(request: summary_model.TextRequest):
    return {
        "summary": "This is a fake summary.", 
        "sentText": f"{request.text}"
        }