from fastapi import FastAPI
from routers import mock_summary
from routers import pdf_info


app = FastAPI()


app.include_router(mock_summary.router)
app.include_router(pdf_info.router)