from fastapi import FastAPI
from schemas import summary


app = FastAPI()


@app.post("/mock-summarizer", response_model=summary.SummaryResponse) ## This tells FastAPI: “When this endpoint returns a response, it must follow the shape (schema) defined in SummaryResponse.
def mock_summarizer(request: summary.TextRequest):
    return {
        "summary": "This is a fake summary.", 
        "sentText": f"{request.text}"
        }