from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import APIRouter, Depends, HTTPException, status, Request, Query, FastAPI ,BackgroundTasks
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from router.user_router import router as auth_router
from router.post_router import router as post_router

app = FastAPI()


app.include_router(auth_router, prefix="/auth")
app.include_router(post_router, prefix="/post")