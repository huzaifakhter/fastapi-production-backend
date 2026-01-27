from sys import prefix
from fastapi import APIRouter
from .api import login, register

router = APIRouter()
router.include_router(login.router)
router.include_router(register.router)

