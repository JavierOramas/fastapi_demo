from internal.process_order import process_orders
from schema.order import Order
from schema.status import Status
from fastapi import HTTPException

def test_valid_quantity():
    orders = [Order(id=1,item="testitem",status=Status.completed, quantity=10, price=20.0), Order(id=1,item="testitem",status=Status.pending, quantity=5, price=15.0)]
    criterion = Status.completed
    result = process_orders(orders, criterion)
    assert result == 200.0 
    
def test_negative_quantity():
    orders = [Order(id=1,item="testitem",status=Status.completed, quantity=-1, price=20.0), Order(id=1,item="testitem",status=Status.pending, quantity=5, price=15.0)]
    criterion = "all"
    result = process_orders(orders, criterion)
    assert isinstance(result, HTTPException)
    assert result.status_code == 422 
    
def test_zero_quantity():
    orders = [Order(id=1,item="testitem",status=Status.completed, quantity=0, price=20.0), Order(id=1,item="testitem",status=Status.pending, quantity=5, price=15.0)]
    criterion = "invalid_status"
    result = process_orders(orders, criterion)
    assert isinstance(result, HTTPException)
    assert result.status_code == 422