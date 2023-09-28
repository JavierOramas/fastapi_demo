from internal.process_order import process_orders
from schema.order import Order
from schema.status import Status
from fastapi import HTTPException
from pydantic import ValidationError
import pytest

def test_valid_order():
    ord = Order(id=1,item="testitem", status=Status.completed, quantity=5, price=10)

def test_invalid_order_status():
    with pytest.raises(ValidationError):
        ord = Order(id=1,item="testitem", status="Wrong", quantity=5, price=10)
    
def test_invalid_quantity_order():
    orders = [Order(id=1,item="testitem",status=Status.completed, quantity=-1, price=20.0), Order(id=1,item="testitem",status=Status.pending, quantity=5, price=15.0)]
    criterion = Status.completed
    result = process_orders(orders, criterion)
    assert isinstance(result, HTTPException) 
    assert result.status_code == 422