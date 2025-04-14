from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router

app = FastAPI(title="Riot's super safe encryption API", version="1.0.0")

# CORS middleware configuration. Uncomment if needed (e.g., for frontend access)

#app.add_middleware(
#    CORSMiddleware,
#    allow_origins=["*"],
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],
#)

app.include_router(api_router, prefix="/api/v1")