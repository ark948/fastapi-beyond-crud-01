from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlalchemy import select, text
from src import config
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker



async_engine = AsyncEngine(
    create_engine(url=Config.DB_URL)
)



async def init_db():
    async with async_engine.begin() as conn:
        from src.db.models import Book

        await conn.run_sync(SQLModel.metadata.create_all)
        # statement = text("SELECT 'hello';")
        # result = await conn.execute(statement)
        # print(result.all())




async def get_session() -> AsyncSession:
    Session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False # allows us to use session even after commit command
    )

    async with Session() as session:
        yield session