from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)


class UserPublic(BaseModel):
    id: str
    full_name: str
    email: EmailStr
    created_at: datetime
    updated_at: Optional[datetime] = None


