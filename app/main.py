from fastapi import FastAPI
from routers import mock_summary
from routers import pdf_info
from routers import video_info
from routers import heath


app = FastAPI()


app.include_router(mock_summary.router)
app.include_router(pdf_info.router)
app.include_router(video_info.router)
app.include_router(heath.router)