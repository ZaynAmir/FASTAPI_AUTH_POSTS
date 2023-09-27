from pydantic import BaseModel, validator, UUID4
from fastapi import HTTPException
from datetime import datetime

# Pydantic model for item creation

class PostCreateRequest(BaseModel):
    title: str
    content: str

    @validator('title')
    def validate_password(cls, value):
        if len(value) < 4:
            raise HTTPException(status_code=400, detail="title must be greater than 3 letters")
        return value

class PostCreateResponse(BaseModel):
    id: UUID4
    title: str
    content: str
    user_id: UUID4
    createdAt: datetime
    updatedAt: datetime | None

class PostDeleteResponse(BaseModel):
    message: str