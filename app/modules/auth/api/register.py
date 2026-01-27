from fastapi import FastAPI, APIRouter
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.modules.auth.service import create_user

router = APIRouter()

@router.post("/register")
async def register(email: str, password: str, db: AsyncSession = Depends(get_db)):
    user = await create_user(db, email, password)
    return {"id": user.id, "email": user.email}
