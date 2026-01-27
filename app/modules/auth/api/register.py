from fastapi import FastAPI, APIRouter
from app.core.db import write_user, read_user

router = APIRouter()

@router.post("/register")
async def user_register(username: str):
    if read_user(username):
        return {"message": f"{username} already exists."}
    else:
        write_user(username)
        return {"message": f"{username} registered successfully."}