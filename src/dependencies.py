from fastapi import Depends
from fastapi.requests import Request
from psycopg_pool import AsyncConnectionPool, ConnectionPool

from src.dao import UserOrderDAO


# def get_psycopg_db_connection(request: Request):
#     """
#     Returns a psycopg DB connection from the DB connection pool.
#     """
#     pool: ConnectionPool = request.app.state.db_connector.psyco_pool
#     with pool.connection(None) as conn:
#         yield conn


async def get_psycopg_async_db_connection(request: Request):
    """
    Returns a psycopg DB connection from the DB connection pool.
    """
    pool: AsyncConnectionPool = request.app.state.db_connector.psyco_async_pool
    async with pool.connection(None) as conn:
        yield conn


def get_user_order_dao(
    connection=Depends(get_psycopg_async_db_connection),
) -> UserOrderDAO:
    return UserOrderDAO(connection)
