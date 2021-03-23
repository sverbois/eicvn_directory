from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import contacts

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

api.include_router(contacts)
