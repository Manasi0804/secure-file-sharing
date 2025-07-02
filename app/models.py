from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    email: EmailStr
    password: str
    role: str  

class FileMeta(BaseModel):
    filename: str
    uploader: str  
