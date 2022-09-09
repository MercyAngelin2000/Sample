from datetime import datetime,timedelta
from jose import JWTError,jwt
from app import models
from fastapi import Depends, status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy .orm import Session
from .database import get_db
from .config import setting


oauth2_schema =OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = setting.secret_key
ALGORITHM = setting.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = setting.access_token_expire_minute

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY,ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id:str = payload.get("user_id")

        if id is None:
            raise credential_exception
        # token_data = schema.TokenData(id=id)
        token_data = id
    except JWTError:
        raise credential_exception
    return token_data

def get_current_user(token: str=Depends(oauth2_schema),db : Session = Depends(get_db)):
    credential_exception =HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials",headers={"www-Authenticate":"Bearer"})
    token = verify_access_token(token,credential_exception)
    cur_user = db.query(models.Login).filter(models.Login.id == token).first()
    return cur_user

