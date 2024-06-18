import psycopg
import psycopg.rows
from psycopg.connection_async import AsyncConnection

from src.model import Order, User


class UserOrderDAO:

    def __init__(self, connection: AsyncConnection):
        self.connection = connection

    async def get_user_orders(self):
        query = """
            SELECT 
                u.id AS user_id, u.name AS user_name, 
                o.id AS order_id, o.item, o.quantity
            FROM 
                user_table u
            JOIN 
                order_table o ON u.id = o.user_id
        """
        async with self.connection.cursor(row_factory=psycopg.rows.dict_row) as cur:
            await cur.execute(query)
            rows = await cur.fetchall()
            return rows

    async def create_user_order(self, user: User, order: Order):
        async with self.connection.transaction():
            async with self.connection.cursor() as cur:
                user_query = "INSERT INTO user_table (name) VALUES (%s) RETURNING id"
                await cur.execute(user_query, (user.name,))
                user_id = await cur.fetchone()
                order_query = "INSERT INTO order_table (user_id, item, quantity) VALUES (%s, %s, %s) RETURNING id"
                await cur.execute(order_query, (user_id, order.item, order.quantity))
                await self.connection.commit()
