import uuid  # Import the UUID module
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()), unique=True)
    username = Column(String(50), index=True, unique=True)
    hashed_password = Column(String(1000))

