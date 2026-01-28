from app.core.securrity import create_access_token
from fastapi import HTTPException
from app.core.securrity import verify_password
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.auth.models import User
from sqlalchemy.orm import session
from sqlalchemy import select
from app.modules.auth.schemas import Token

from app.core.interfaces.user_repository import UserRepository
from app.core.securrity import hash_password

class UserAlreadyExists(Exception):
    pass

async def register_user(email: str, password: str, repo: UserRepository):
    if await repo.get_by_email(email):
        raise UserAlreadyExists()

    return await repo.create(
        email=email,
        hashed_password=hash_password(password)
    )









async def create_user(
    db: AsyncSession,
    email: str,
    password_hash: str
):
    user = User(
        email=email,
        password_hash=password_hash
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user

async def get_user_by_email(db: AsyncSession, email: str):
    stmt = select(User).where(User.email == email)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

async def login_user(db: AsyncSession, email: str, password: str):
    user = await get_user_by_email(db, email)

    if not user or not verify_password(password, user.password_hash):
        return None
    
    token = create_access_token({"sub": str(user.id)})
    return Token(access_token=token)