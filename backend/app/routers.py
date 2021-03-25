from fastapi import APIRouter
from fastapi import status
from .schemas import Contact
from .cruds import create_contact_in_bd
from .cruds import read_contacts_from_db
from .cruds import db

contacts = APIRouter()

@contacts.get("/contacts")
def read_contacts():
    """Return all contacts"""
    return read_contacts_from_db()


@contacts.post("/contacts", status_code=status.HTTP_201_CREATED)
def create_contact(contact: Contact):
    if contact in db :
       return {"message" : "The contact already exists"}
    
    else :
       # """Add a new contact"""
        create_contact_in_bd(contact)
        return contact