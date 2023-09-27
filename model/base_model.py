import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from database import Base
from sqlalchemy.ext.declarative import AbstractConcreteBase

class BaseModel(Base, AbstractConcreteBase):
    id = Column(String(36), primary_key=True, unique=True)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now())