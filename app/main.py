from fastapi import FastAPI
from app.modules.auth.router import router
from app.core.db import engine
from app.modules.auth.models import Base
from app.modules.test_service.routes import router as test_router

app = FastAPI()
app.include_router(router, prefix="/auth", tags=["auth"])
app.include_router(test_router, prefix="/test", tags=["test"])

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)