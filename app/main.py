import imp
from fastapi import FastAPI
from app import models
from .database import engine
from .router import post, sqlalchemy , vote

models.Base.metadata.create_all(bind=engine)  # bind = A Connectable used to access the database Meta= collection of table objects

app = FastAPI()
app.include_router(post.router)
app.include_router(sqlalchemy.router)
app.include_router(vote.router)













    
    
