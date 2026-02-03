from fastapi import APIRouter
from app.modules.blog.api import blog

router = APIRouter()
router.include_router(blog.router)