from app.core.security import create_access_token
from fastapi import HTTPException, Depends
from app.core.security import verify_password
from app.modules.auth.schemas import Token
from app.core.interfaces.user_repository import UserRepository
from app.core.security import hash_password
import random
from app.core.dependencies import get_user_repo
from uuid import UUID

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

async def update_profile(
    user_id: UUID,
    first_name: str,
    last_name: str, 
    avatar_url: str,
    age: int,
    repo: UserRepository = Depends(get_user_repo)
    ):

    return await repo.update_profile(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name, 
        avatar_url=avatar_url,
        age=age
    )

async def change_password(user_id: UUID, current_password: str, password: str, repo: UserRepository):
    
    user = await repo.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(current_password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    hashed_password = hash_password(password)
    return await repo.change_password(
        user_id=user_id,
        hashed_password=hashed_password
    )

async def authenticate_user(email: str, password: str, repo: UserRepository = Depends(get_user_repo)):
    user = await repo.get_by_email(email)
    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user

