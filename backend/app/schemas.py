import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr


class Contact(BaseModel):
    firstname: str
    lastname: str
    birthday: datetime.date
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
