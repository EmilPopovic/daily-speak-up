from typing import List
from pydantic import BaseModel, EmailStr

class UsernameData(BaseModel):
    username: str

class EmailData(BaseModel):
    email: EmailStr

class InterestData(BaseModel):
    interests: List[str]