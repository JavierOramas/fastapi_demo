from internal.process_order import process_orders
from schema.order import Order
from schema.status import Status
from fastapi import HTTPException

def test_valid_status_filter():
    orders = [Order(id=1,item="testitem",status=Status.completed, quantity=10, price=20.0), Order(id=1,item="testitem",status=Status.pending, quantity=5, price=15.0)]
    criterion = Status.completed
    result = process_orders(orders, criterion)
    assert result == 200.0 
    
def test_all_status_filter():
    orders = [Order(id=1,item="testitem",status=Status.completed, quantity=10, price=20.0), Order(id=1,item="testitem",status=Status.pending, quantity=5, price=15.0)]
    criterion = "all"
    result = process_orders(orders, criterion)
    assert result == 275.0
    
def test_invalid_status_filter():
    orders = [Order(id=1,item="testitem",status=Status.completed, quantity=10, price=20.0), Order(id=1,item="testitem",status=Status.pending, quantity=5, price=15.0)]
    criterion = "invalid_status"
    result = process_orders(orders, criterion)
    assert isinstance(result, HTTPException)
    assert result.status_code == 422
    assert "Invalid filter criterion invalid_status" in result.detail