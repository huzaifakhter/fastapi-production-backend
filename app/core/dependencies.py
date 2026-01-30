from jose import ExpiredSignatureError
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.sql.user_repo import SQLUserRepository
from fastapi import Depends, HTTPException
from app.core.db import get_db
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.interfaces.user_repository import UserRepository
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_MINUTES = int(os.getenv("ACCESS_TOKEN_MINUTES"))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_user_repo(db: AsyncSession = Depends(get_db)):
    return SQLUserRepository(db)

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    repo: UserRepository = Depends(get_user_repo),
):  

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401)

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token Expired"
        )

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    user = await repo.get_by_email(email)
    if not user:
        raise HTTPException(status_code=401)

    return user
