import pytest
from calculator import add, sub, mul, divide

def test_add_positive():
    assert add(5, 3) == 8

def test_sub_negative_result():
    assert sub(3, 5) == -2

def test_mul():
    assert mul(4, 6) == 24
    
def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_add_zero():
    assert add(7, 0) == 7

def test_mul_negative():
    assert mul(-2, 3) == -6

def test_divide_float():
    assert divide(7, 2) == 3.5