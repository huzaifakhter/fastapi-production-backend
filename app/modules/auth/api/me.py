from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import get_current_user, get_user_repo
from app.modules.auth.schemas import UserOut, FullProfileOut, UpdateProfile, UpdatePassword
from app.core.interfaces.user_repository import UserRepository
from app.modules.auth.service import change_password
router = APIRouter()

@router.get("/me", response_model=UserOut)
async def me(user=Depends(get_current_user)):
    return user

@router.get("/full_profile", response_model=FullProfileOut)
async def full_profile(user=Depends(get_current_user)):
    return user

@router.patch("/update_profile", response_model=FullProfileOut)
async def update_profile(
    payload: UpdateProfile,
    user=Depends(get_current_user),
    repo: UserRepository = Depends(get_user_repo),
):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    updated_user = await repo.update_profile(
        user_id=user.id,
        first_name=payload.first_name,
        last_name=payload.last_name,
        avatar_url=payload.avatar_url,
        age=payload.age,
    )

    return updated_user

@router.patch("/change_password", response_model=FullProfileOut)
async def update_password(
    payload: UpdatePassword,
    user=Depends(get_current_user),
    repo: UserRepository = Depends(get_user_repo),
):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    updated_user = await change_password(
        user_id=user.id,
        current_password=payload.current_password,
        password=payload.password,
        repo=repo
    )

    return updated_user

