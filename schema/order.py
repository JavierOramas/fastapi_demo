from pydantic import BaseModel
from schema.status import Status

class Order(BaseModel):
    id: int
    item: str
    quantity: int
    price: float
    status: Status
    
class OrderModel:
    def __init__(self, order: dict):
        self.id = int(order.id)
        self.quantity = int(order.quantity)
        self.price = float(order.price)
        self.status = Status(order.status)
    

