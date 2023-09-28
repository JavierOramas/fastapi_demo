from fastapi import APIRouter
from internal.process_order import process_orders
from schema.query import OrderRequest

router = APIRouter(
    prefix="/solution",
    tags=["solution"],
    responses={404: {"description": "Not found"}},
)

@router.post("")
def filter(query_criterion: OrderRequest):
    print("orders", query_criterion.orders)
    return process_orders(orders=query_criterion.orders, criterion=query_criterion.criterion)