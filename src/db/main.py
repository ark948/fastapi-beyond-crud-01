from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlalchemy import select, text
from src import config



engine = AsyncEngine(
    create_engine(url=Config.DB_URL, echo=True)
)



async def init_db():
    async with engine.begin() as conn:
        from src.books.models import Book

        await conn.run_sync(SQLModel.metadata.create_all)
        # statement = text("SELECT 'hello';")
        # result = await conn.execute(statement)
        # print(result.all())
