from app.core.security import create_access_token
from fastapi import HTTPException
from app.core.security import verify_password
from app.modules.auth.schemas import Token
from app.core.interfaces.user_repository import UserRepository
from app.core.security import hash_password

class UserAlreadyExists(Exception):
    pass

async def register_user(email: str, password: str, repo: UserRepository):
    if await repo.get_by_email(email):
        raise UserAlreadyExists()

    return await repo.create(
        email=email,
        hashed_password=hash_password(password)
    )

async def authenticate_user(email: str, password: str, repo: UserRepository):
    user = await repo.get_by_email(email)
    if not user:
        return None

    if not verify_password(password, user["hashed_password"] if isinstance(user, dict) else user.hashed_password):
        return None

    return user