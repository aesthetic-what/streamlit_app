from typing import AsyncGenerator
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from contextlib import asynccontextmanager

engine = create_async_engine("sqlite+aiosqlite:///users.db")
local_session = async_sessionmaker(engine)
class Base(DeclarativeBase): pass


# @asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with local_session() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

