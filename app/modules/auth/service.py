from app.core.security import create_access_token
from fastapi import HTTPException, Depends
from app.core.security import verify_password
from app.modules.auth.schemas import Token
from app.core.interfaces.user_repository import UserRepository
from app.core.security import hash_password
import random
from app.core.dependencies import get_user_repo

class UserAlreadyExists(Exception):
    pass

async def generate_username(repo: UserRepository) -> str:
    adjectives = ["brave","bold","true","just","strong","fierce","iron","keen","sure","firm","pure","fast","hard","wise","calm"]
    nouns = ["hero","knight","king","champ","lord","chief","guard","war","blade","shield","valor","honor","might","force","will"]


    for _ in range(10):
        username = (
            f"{random.choice(adjectives).title()}"
            f"{random.choice(nouns).title()}"
            f"{random.randint(0, 999):03d}"
        )

        exists = await repo.check_username(username)
        if not exists:
            return username

    raise HTTPException(
        status_code=409,
        detail="Unable to generate unique username"
    )

async def register_user(email: str, password: str, repo: UserRepository = Depends(get_user_repo)):
    if await repo.get_by_email(email):
        raise UserAlreadyExists()

    username = await generate_username(repo)
    return await repo.create(
        username=username,
        email=email,
        hashed_password=hash_password(password)
    )

async def authenticate_user(email: str, password: str, repo: UserRepository = Depends(get_user_repo)):
    user = await repo.get_by_email(email)
    if not user:
        return None

    if not verify_password(password, user["hashed_password"] if isinstance(user, dict) else user.hashed_password):
        return None

    return user

