from contextlib import asynccontextmanager

from fastapi import FastAPI

from db.utils import create_tables, engine
from services import handler


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:  # noqa: WPS430
    app.middleware_stack = None
    await create_tables()
    await handler.add_normal_values()
    app.middleware_stack = app.build_middleware_stack()

    yield

    await engine.dispose()
