from fastapi import FastAPI

from .routers import contacts

api = FastAPI()

api.include_router(contacts)
