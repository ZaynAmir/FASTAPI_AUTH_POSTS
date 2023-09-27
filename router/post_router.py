from fastapi import APIRouter, Depends, Body, HTTPException, Request
from typing import Annotated, List
from sqlalchemy.orm import Session
from database import get_db
from schemas.post_schema import PostCreateRequest, PostCreateResponse, PostDeleteResponse
from controller import post_controller, user_controller

router = APIRouter(tags=['post'])

auth = user_controller.get_current_user

# Assuming you want to limit the payload size to 1 MB (1048576 bytes)
MAX_PAYLOAD_SIZE_BYTES = 1048576


@router.post('/add', response_model=PostCreateResponse)
async def create_post(request: Request, post_request: PostCreateRequest,
                    db : Session = Depends(get_db), get_logged_user = Depends(auth) ):
    response = post_controller.add_new_post(request, post_request, get_logged_user, db, MAX_PAYLOAD_SIZE_BYTES)
    return response
    
@router.get('/getAll', response_model=List[PostCreateResponse])
async def get_all_posts(db : Session = Depends(get_db), get_logged_user = Depends(auth) ):
    response = post_controller.get_all_posts_of_user(get_logged_user, db)
    return response


@router.get('/{post_id}', response_model=PostCreateResponse)
async def get_one_post(post_id ,db : Session = Depends(get_db)):
    response = post_controller.get_post(post_id, db)
    return response

@router.delete('/{post_id}', response_model=PostDeleteResponse)
async def delete_posts(post_id ,db : Session = Depends(get_db), get_logged_user = Depends(auth) ):
    response = post_controller.delete_your_post(get_logged_user, post_id, db)
    return response