from ast import Str
from cgitb import text
from enum import unique
from typing import Tuple
from wsgiref.simple_server import server_version
from psycopg2 import Timestamp
from sqlalchemy import Column,Integer,String,Boolean,BigInteger,Date,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base
from sqlalchemy .orm import relationship

class Login(Base):
    __tablename__ = "logintable"
    id = Column(Integer, primary_key = True, nullable=False, autoincrement=True)
    firstname = Column(String, nullable =False)
    lastname = Column(String,nullable = False)
    phone = Column(BigInteger, nullable =False)
    email = Column(String,nullable = False, unique = True)
    dob = Column(Date, nullable = False)
    gender = Column(String,nullable = False)
    pwd = Column(String,nullable = False)
   


class Fastapisample(Base):
    __tablename__ = "fastapisample"
    id = Column(Integer, primary_key =True , nullable =False, autoincrement=True)
    title = Column(String, nullable =False)
    content = Column(String, nullable =False)
    published = Column(Boolean, nullable =False, server_default="True")
    created_at = Column(TIMESTAMP(timezone=True),nullable =False, server_default = text('now()'))
    owner_id = Column(Integer,ForeignKey("logintable.id",ondelete="CASCADE"), nullable = False)
    owner = relationship("Login")
   

class Vote(Base):
    __tablename__ ="vote"
    user_id = Column(Integer,ForeignKey("logintable.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer,ForeignKey("fastapisample.id", ondelete="CASCADE"), primary_key=True)


class post(Base):
    __tablename__="post"
    id=Column(Integer, primary_key = True)
    name = Column(String,nullable= False)
    # age = Column(Integer,nullable=False)
    # gender = Column(String,nullable=False)



