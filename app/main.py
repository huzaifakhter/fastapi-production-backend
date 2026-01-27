from fastapi import FastAPI
from app.modules.auth.router import router
from app.core.db import engine
from app.modules.auth.models import Base


app = FastAPI()
app.include_router(router, prefix="/auth")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
