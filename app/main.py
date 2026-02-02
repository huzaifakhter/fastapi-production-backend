from fastapi import FastAPI
from app.modules.auth.router import router
from app.core.db import engine
from app.modules.auth.models import Base
from app.modules.blog.routes import router as blog

app = FastAPI()
app.include_router(router, prefix="/auth", tags=["auth"])
app.include_router(blog, prefix="/blog", tags=["blog"])

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)