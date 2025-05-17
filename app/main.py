from fastapi import FastAPI
from routers import mock_summary


app = FastAPI()


app.include_router(mock_summary.router)