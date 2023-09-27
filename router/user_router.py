from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from schemas.user_schema import UserCreateRequest, Token
from controller import user_controller

router = APIRouter(tags=['auth'])

@router.post('/create')
async def create_user(user_request: UserCreateRequest, db : Session = Depends(get_db)):
    response = user_controller.register_new_user(user_request, db)
    return response
    
@router.post('/login')
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db : Session = Depends(get_db)):
    response = user_controller.login_user(form_data.username, form_data.password, db)
    return response
    