from fastapi import FastAPI
from app.modules.auth.router import router
from app.core.db import engine
from app.modules.auth.models import Base
from app.core.dependencies import get_current_user
from fastapi import Depends

app = FastAPI()
app.include_router(router, prefix="/auth")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/protected")
async def protected(user=Depends(get_current_user)):
    return {"user": user}