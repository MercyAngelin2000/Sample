from sqlalchemy import create_engine  #used to connect with db
from sqlalchemy.ext.declarative import declarative_base  #to collect the obj that defined in new table
from sqlalchemy.orm import sessionmaker # used to interact with db
from .config import Settings


SQLALCHEMY_DATABASE_URL = f"postgresql://{Settings.database_username}:{Settings.database_password}@{Settings.database_hostname}:{Settings.database_port}/{Settings.database_name}"   #username:password@hostname/dbname
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False,bind=engine) 
Base = declarative_base()    #we will inherit from this class to create each of the database models or classes

# Dependency
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

