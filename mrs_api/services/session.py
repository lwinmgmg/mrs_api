from typing import AsyncGenerator, Any
from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from mrs_api.services.engine import engine

async_session = async_sessionmaker(engine)


async def get_async_session() -> AsyncGenerator[AsyncSession, Any]:
    async with async_session() as session:
        try:
            yield session
        except:
            await session.rollback()
            raise


def db_session():
    return Depends(get_async_session)
