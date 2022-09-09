from datetime import date
from typing import List, Optional
from pydantic import BaseModel
from pydantic.types import conint

class post(BaseModel):
    Hai:str
    Iam:str
    DoULoveMe:str
    IsItTrue: bool =True
    TellMeUrAge: Optional[int]= 21

class dbmethod(BaseModel):
    id:int
    title:str
    content:str
    published: bool = True

class Postmethod(BaseModel):
    id: int
    title:str
    
    class Config:
        orm_mode =True

class register(BaseModel):
    id:int
    email:str
    class Config:
        orm_mode = True



class Post(BaseModel):
    id:int
    title:str
    content:str
    owner_id:int
    owner:register
    class Config:
        orm_mode = True


class sqlmethod(BaseModel):
    title:str
    content:str
    published: bool = True
    

class login(BaseModel):
    email:str
    pwd:str

class reg(BaseModel):
    firstname:str
    lastname:str
    phone:int
    email:str
    dob:date
    gender:str
    pwd :str


class Token(BaseModel):
        access_token : str
        token_type : str

class TokenData(BaseModel):
    id : Optional[str]= None


class vote(BaseModel):
    post_id:int
    dir:conint(le=1)
