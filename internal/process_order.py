from schema.status import Status
from schema.order import Order, OrderModel
from fastapi import HTTPException
from typing import List

def process_orders(orders:List[Order], criterion: Status):
    if criterion == 'all':
        filtered_orders = orders
    else:
        try:
            st = Status(criterion)
        except ValueError:
            return HTTPException(422, f"Invalid filter criterion {criterion}")
        
        filtered_orders = [OrderModel(order) for order in orders if order.status == criterion]

    total_revenue = 0
    
    for order in filtered_orders:
        if order.quantity <= 0:
            return HTTPException(422, f"Invalid Quantity, got item id:{order.id} with {order.quantity}, must be grater than 0")
        if order.price < 0:
            return HTTPException(422, f"Invalid Price, got item id:{order.id} with {order.price}, must be grater or equal than 0")
        total_revenue += order.quantity * order.price

    return total_revenue