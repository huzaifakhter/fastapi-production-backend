from sys import prefix
from fastapi import APIRouter
from .api import register, get_users, login, register

router = APIRouter()
# router.include_router(login.router)
router.include_router(register.router)
router.include_router(get_users.router)
router.include_router(login.router)

