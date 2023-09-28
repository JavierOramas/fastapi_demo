from pydantic import BaseModel
from typing import List
from schema.order import Order

class OrderRequest(BaseModel):
    orders: List[Order]
    criterion: str