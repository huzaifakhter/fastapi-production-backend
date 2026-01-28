from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.auth.models import User
from sqlalchemy.orm import session
from sqlalchemy import select

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