from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse

from src.dao import UserOrderDAO
from src.dependencies import get_user_order_dao
from src.model import Order, User

router = APIRouter()


@router.get("/", response_class=RedirectResponse)
def root():
    return RedirectResponse("/docs")


@router.get("/user_orders/")
async def read_user_orders(user_order_dao: UserOrderDAO = Depends(get_user_order_dao)):
    user_orders = await user_order_dao.get_user_orders()
    if not user_orders:
        raise HTTPException(status_code=404, detail="User orders not found")
    return user_orders


@router.post("/user_orders/")
async def create_user_order(
    user: User, order: Order, user_order_dao: UserOrderDAO = Depends(get_user_order_dao)
):
    await user_order_dao.create_user_order(user, order)
    return {"message": "User and order created successfully"}
