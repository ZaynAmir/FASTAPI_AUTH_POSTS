from pydantic import BaseModel, validator
from fastapi import APIRouter, Depends, FastAPI, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from model.user_model import User



# Pydantic model for item creation

class UserCreateRequest(BaseModel):
    username: str
    password: str

    @validator('password')
    def validate_password(cls, value, db : Session = Depends(get_db)):
        if len(value) < 8:
            raise HTTPException(status_code=400, detail="password must be greater or equal to 8 digits")
        return value



class Token(BaseModel):
    access_token: str
    token_type: str
