from fastapi import HTTPException
from fastapi import APIRouter, Depends
from app.core.interfaces.user_repository import UserRepository
from app.core.dependencies import get_user_repo
from app.core.security import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from app.modules.auth.service import authenticate_user

router = APIRouter()

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    repo: UserRepository = Depends(get_user_repo),
):
    user = await authenticate_user(
        email=form_data.username,
        password=form_data.password,
        repo=repo
    )
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
