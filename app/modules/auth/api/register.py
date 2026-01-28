from select import select
from fastapi import FastAPI, APIRouter
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.modules.auth.service import create_user, get_user_by_email

router = APIRouter()

@router.post("/register")
async def register(email: str, password: str, db: AsyncSession = Depends(get_db)):
    if await get_user_by_email(db, email):
        return {"message": f"a user with '{email}' already exist in our database"}
    else:
        user = await create_user(db, email, password)
        return {"message": "Success"}
