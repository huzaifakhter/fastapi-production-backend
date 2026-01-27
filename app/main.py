from fastapi import FastAPI
from app.modules.auth.router import router

app = FastAPI()
app.include_router(router, prefix="/auth")
