from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass

class PostRespose(PostBase):
    id: int
    created_at: datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    email: EmailStr
    class Config:
        orm_mode = True