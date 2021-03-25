from tinydb import TinyDB
from .schemas import Contact

db = TinyDB('db.json')

def create_contact_in_bd(contact: Contact):
    num = db.insert(contact.dict())
    return num

def read_contacts_from_db():
    contacts_from_db = db.all()
    return contacts_from_db 
