from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from db.meta import meta

engine = create_async_engine("postgresql+asyncpg://pandora:pandora@db:5432/pandora")
async_session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
)


async def create_tables() -> None:  # pragma: no cover
    """Populates tables in the database."""
    async with engine.begin() as connection:
        await connection.run_sync(meta.create_all)
    await engine.dispose()
