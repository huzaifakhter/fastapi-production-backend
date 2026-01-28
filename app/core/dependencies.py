from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.sql.user_repo import SQLUserRepository
from fastapi import Depends
from app.core.db import get_db
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from app.core.interfaces.user_repository import UserRepository

SECRET_KEY = "secretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_MINUTES = 15

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_user_repo(db: AsyncSession = Depends(get_db)):
    return SQLUserRepository(db)

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    repo: UserRepository = Depends(get_user_repo),
):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email = payload.get("sub")
    if not email:
        raise HTTPException(status_code=401)

    user = await repo.get_by_email(email)
    if not user:
        raise HTTPException(status_code=401)

    return user
