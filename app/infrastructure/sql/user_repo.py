from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.modules.auth.models import User
from app.core.interfaces.user_repository import UserRepository

class SQLUserRepository(UserRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_email(self, email: str):
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def check_username(self, username: str):
        result = await self.db.execute(
            select(User).where(User.username == username)
        )
        
        return result.scalar_one_or_none()

    async def create(self, username: str, email: str, hashed_password: str):
        user = User(username=username, email=email, hashed_password=hashed_password)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)

        return user


