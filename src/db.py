import psycopg_pool

# db_config = config.database
# conn_string = f"postgresql://{db_config.username}:{db_config.pwd}@{db_config.host}:{db_config.port}/{db_config.name}"
conn_string = "postgresql://osense:52605851@localhost:5432/osense"


class DBConnector:
    def __init__(self):
        self.psyco_async_pool: psycopg_pool.AsyncConnectionPool = (
            psycopg_pool.AsyncConnectionPool(conn_string)
        )
        # self.psyco_pool: psycopg_pool.ConnectionPool = psycopg_pool.ConnectionPool(
        #     conn_string
        # )

    async def create_tables(self):
        await self.psyco_async_pool.open()
        async with self.psyco_async_pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS user_table (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100)
                    );
                    CREATE TABLE IF NOT EXISTS order_table (
                        id SERIAL PRIMARY KEY,
                        user_id INTEGER REFERENCES user_table(id),
                        item VARCHAR(100),
                        quantity INTEGER
                    );
                """
                )
                await conn.commit()

    async def end(self):
        # self.psyco_pool.close()
        await self.psyco_async_pool.close()
