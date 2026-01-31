from fastapi import FastAPI, APIRouter, Depends
from app.core.dependencies import get_current_user

router = APIRouter()

@router.get("/blog")
async def get_blogs(user=Depends(get_current_user)):
    firstname = user.first_name
    return {
        "message": f"hello {firstname}, how are you?"
    }
