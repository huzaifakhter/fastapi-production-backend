from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    sub: UUID

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

# class UserProfile(BaseModel):
#     id: UUID
#     username: str
#     email: EmailStr
#     is_active: bool
#     first_name: str
#     last_name: str
#     avatar_url: str
#     age: int
    
class FullProfileOut(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    is_active: bool
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    avatar_url: Optional[str] = None
    age: Optional[int] = None

    class Config:
        from_attributes = True

class UpdateProfile(BaseModel):
    first_name: str
    last_name: str
    avatar_url: str
    age: int

class UpdatePassword(BaseModel):
    current_password: str
    password: str