from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.db import get_db
from app.modules.auth.models import User
from app.core.interfaces.user_repository import UserRepository
from app.core.dependencies import get_user_repo, get_current_user
router = APIRouter()

@router.get("/users")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users

@router.get("/check-username")
async def check_username(
    username: str,
    repo: UserRepository = Depends(get_user_repo),
    current_user=Depends(get_current_user),
):
    return await repo.check_username(username)