import uuid
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model.base_model import BaseModel
class Post(BaseModel):
    __tablename__ = "posts"

    title = Column(String(255))
    content = Column(String(1000))
    # Define the foreign key relationship to User
    user_id = Column(String(36), ForeignKey("users.id"))
    # Define the many-to-one relationship with User
    author = relationship("User", back_populates="posts")