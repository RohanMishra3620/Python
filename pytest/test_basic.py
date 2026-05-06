def add(x,y):
    return x+y

def test_add():
    assert add(2,2)==4

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -2) == -3

def test_add_zero():
    assert add(0, 5) == 5