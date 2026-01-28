from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.sql.user_repo import SQLUserRepository
from fastapi import Depends
from app.core.db import get_db

async def get_user_repo(db: AsyncSession = Depends(get_db)):
    return SQLUserRepository(db)