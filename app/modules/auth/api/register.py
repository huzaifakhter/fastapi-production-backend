from select import select
from fastapi import FastAPI, APIRouter
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.modules.auth.service import create_user, get_user_by_email
from app.core.securrity import hash_password
from app.modules.auth.schemas import UserCreate

router = APIRouter()

@router.post("/register", status_code=201)
async def register(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    hashed = hash_password(payload.password)   # ONLY here
    await create_user(db, payload.email, hashed)
    return {"message": "User created"}
