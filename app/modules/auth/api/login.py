from fastapi import HTTPException
from fastapi import APIRouter, Depends
from app.modules.auth.service import get_user_by_email
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.modules.auth.schemas import UserOut, UserLogin

router = APIRouter()

@router.post("/login/", response_model=UserOut)
async def login(
    payload: UserLogin,
    db: AsyncSession = Depends(get_db)
    ):
    user = await get_user_by_email(db, email=payload.email)
    
    if not user:
        raise HTTPException(status_code=404, detail=f"User with email '{payload.email}' was not found.")
    
    elif user.password_hash == payload.password:
        return UserOut.model_validate(user)

    else:
        raise HTTPException(status_code=400, detail="invalid credentials")


