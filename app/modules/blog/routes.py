from fastapi import APIRouter
from app.modules.test_service.api import blog

router = APIRouter()
router.include_router(blog.router)