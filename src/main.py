from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api import router
from src.db import DBConnector


@asynccontextmanager
async def lifespan(application: FastAPI):
    # Creates database connections when the FastAPI application starts.
    application.state.db_connector = DBConnector()
    yield
    # Closes the database connection when the FastAPI application is shut down.
    await application.state.db_connector.end()


app = FastAPI(
    title="FastAPI PostgreSQL Benchmark",
    lifespan=lifespan,
)

app.include_router(router)
