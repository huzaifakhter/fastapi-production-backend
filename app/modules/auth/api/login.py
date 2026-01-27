from app.core.db import read_user
from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/login")
async def user_login(username: str):
    if read_user(username):
        return {"message": f"🥳 {username.upper()} was found in db."}
    return {"message": f"we are sorry, {username} was not found in the db."}

