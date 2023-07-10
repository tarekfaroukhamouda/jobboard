from typing import Optional
from pydantic import EmailStr, BaseModel


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class ShowUser(BaseModel):
    username:str
    email:EmailStr
    is_actibe:bool
    class Config:
        orm_mode=True