from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

from config import settings

Base = declarative_base()

engine = create_async_engine(
    url=settings.db.url, echo=False, pool_size=5, max_overflow=10
)

session_maker = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_sessionmaker() as session:
        yield session