from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from db.utils import async_session_maker


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Create and get database session.

    :yield: database session.
    """
    session: AsyncSession = async_session_maker()

    try:
        yield session
    finally:
        await session.commit()
        await session.close()


@asynccontextmanager
async def get_db_session_manager():
    session: AsyncSession = async_session_maker()

    try:
        yield session
    finally:
        await session.commit()
        await session.close()
