from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.sql.user_repo import SQLUserRepository
from fastapi import Depends
from app.core.db import get_db
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from fastapi import Depends, HTTPException

SECRET_KEY = "secretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_MINUTES = 15

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

async def get_user_repo(db: AsyncSession = Depends(get_db)):
    return SQLUserRepository(db)