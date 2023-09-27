from fastapi import APIRouter, Depends
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from database import get_db
from model.user_model import User
from schemas.user_schema import UserCreateRequest, Token

from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, FastAPI, HTTPException
from starlette import status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
import uuid


# must be hidden in prod env
SECRET_KEY = "12fc35468045690$78900-323235#ec46754b4354a5196696969e69"
ALGORITHM = 'HS256'

bycrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

def register_new_user(user_request, db: Session):
    # Check if the username already exists in the database
    existing_user = db.query(User).filter(User.username == user_request.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    try:
        new_user = User(username=user_request.username,
                    hashed_password=bycrypt_context.hash(user_request.password)) #hashed the user password before saving into DB
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {
            "message": "user registered successfully",
            "id": new_user.id
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail={"error": "Internal Server Error"})
    
def login_user(username: str, password: str, db: Session):
    user = authenticate_user(username, password, db)
    if not user:
        raise HTTPException(status_code=400, detail="Could not validate user")
    token = create_access_token(user.username, user.id, timedelta(minutes=60))
    return {
        "username" : user.username,
        "user_id": user.id,
        "access_token": token
    }

def authenticate_user(username:str, password:str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not bycrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: uuid.uuid4(), expire_time: timedelta):
    
    expires = datetime.utcnow() + expire_time
    iat = datetime.utcnow()
    jti = str(uuid.uuid4())

    to_encode = {
        "token_type": 'access',
        "exp": expires, 
        "user_id": str(user_id),
        "sub": username,
        "iat": iat,
        "jti": jti,
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt