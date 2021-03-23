from fastapi import APIRouter
from fastapi import status

from .schemas import Contact

contacts = APIRouter()


@contacts.get("/contacts")
def read_contacts():
    """Return all contacts"""
    return {}


@contacts.post("/contacts", status_code=status.HTTP_201_CREATED)
def create_user(contact: Contact):
    """Add a new contact"""
    return contact
