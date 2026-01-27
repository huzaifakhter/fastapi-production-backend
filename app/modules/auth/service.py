from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.auth.models import User

async def create_user(
    db: AsyncSession,
    email: str,
    password_hash: str
):
    user = User(
        email=email,
        password_hash=password_hash
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user
