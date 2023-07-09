import datetime
from typing import Optional
from pydantic import EmailStr, BaseModel
from datetime import  date

class JobBase(BaseModel):
    title: Optional[str]=None
    company :Optional[str]=None
    company_url :Optional[str]=None
    location : Optional[str]="Remote"
    description : Optional[str]=None
    date_post : Optional[date]=datetime.datetime.today()

class JobCreate(JobBase):
    title:str
    company:str
    location:str
    description:str
    date_post : Optional[date]=datetime.datetime.today()


class ShowJob(JobBase):
    title:str
    company:str
    company_url:Optional[str]
    description:Optional[str]

    class Config:
        orm_mode=True
