from sqlalchemy import Select
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.modules.auth.models import User
from app.core.interfaces.user_repository import UserRepository
from uuid import UUID

class SQLUserRepository(UserRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_email(self, email: str):
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()
    
    async def get_by_id(self, user_id: UUID):
        result = await self.db.execute(
            select(User).where(User.id == user_id)
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

    async def update_profile(
        self,
        user_id: UUID,
        first_name: str | None = None,
        last_name: str | None = None,
        avatar_url: str | None = None,
        age: int | None = None,
    ):
        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
        if avatar_url is not None:
            user.avatar_url = avatar_url
        if age is not None:
            user.age = age

        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def change_password(
        self,
        user_id: UUID,
        hashed_password: str
    ):

        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )

        user = result.scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=404, detail="User not found.")

        user.hashed_password=hashed_password

        await self.db.commit()
        await self.db.refresh(user)
        return user