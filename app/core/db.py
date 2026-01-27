from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./dev.db"

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


# def read_user(username):
#     with open("datafile.txt", "r") as df:
#         if username in df.read():
#             return True
#         else:
#             return False

# def write_user(username):
#     with open("datafile.txt", "a") as df:
#         df.write(username + "\n")