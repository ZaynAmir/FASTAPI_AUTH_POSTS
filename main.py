from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import APIRouter, Depends, HTTPException, status, Request, Query, FastAPI ,BackgroundTasks
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from router.user_router import router as auth_router


# Create the FastAPI app
app = FastAPI()

# Configure the SQLAlchemy database connection
# DATABASE_URL = "mysql+pymysql://root:zain1234@127.0.0.1/fastapi_db"

# DB_USER = "admin"
# DB_PASSWORD = "admin"
# DB_HOST = "mysql-db"
# DB_PORT = 3307
# DATABASE = "fastapi_db"
# DATABASE_URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DATABASE)

# Base = declarative_base()

# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base.metadata.create_all(bind=engine)



# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# Define FastAPI routes
# @app.post("/items/")
# async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
#     db_item = Item(**item.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, db: Session = Depends(get_db)):
#     db_item = db.query(Item).filter(Item.id == item_id).first()
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return db_item


app.include_router(auth_router, prefix="/auth")