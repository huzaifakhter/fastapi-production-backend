from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user
from app.modules.auth.schemas import UserOut, FullProfileOut

router = APIRouter()

@router.get("/me", response_model=UserOut)
async def me(user=Depends(get_current_user)):
    return user

@router.get("/full_profile", response_model=FullProfileOut)
async def full_profile(user=Depends(get_current_user)):
    return user
