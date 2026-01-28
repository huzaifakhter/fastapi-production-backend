from pygments.token import Token
from fastapi import HTTPException
from fastapi import APIRouter, Depends
from app.modules.auth.service import get_user_by_email, login_user
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.modules.auth.schemas import UserOut, UserLogin

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(
    payload: UserLogin,
    db: AsyncSession = Depends(get_db)
    ):

    token = await login_user(db, payload.email, payload.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return token

