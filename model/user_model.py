import uuid  # Import the UUID module
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.base_model import BaseModel
class User(BaseModel):
    __tablename__ = "users"

    username = Column(String(50), index=True, unique=True)
    hashed_password = Column(String(1000))

    # Define the one-to-many relationship with Post
    posts = relationship("Post", back_populates="author")

