from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI(title="Riot's super safe encryption API", version="1.0.0")

app.include_router(api_router, prefix="/api/v1")