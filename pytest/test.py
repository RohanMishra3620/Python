import pytest

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


def test_add():
    assert add(5,5) == 10
    assert sub(10,5) == 5
    assert mul(10,5) == 50
    assert div(100,5) == 20