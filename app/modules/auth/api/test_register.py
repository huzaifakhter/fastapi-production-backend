from fastapi import APIRouter, Depends
from app.modules.auth.service import register_user
from app.core.interfaces.user_repository import UserRepository
from app.core.dependencies import get_user_repo
from app.modules.auth.schemas import UserCreate
from app.modules.auth.service import UserAlreadyExists
from fastapi import HTTPException

router = APIRouter()

@router.post("/test_register")
async def register(
    payload: UserCreate,
    repo: UserRepository = Depends(get_user_repo),
):
    try:
        await register_user(payload.email, payload.password, repo)
        return {"message": "User created"}
    except UserAlreadyExists:
        raise HTTPException(status_code=400, detail="User already exists")




