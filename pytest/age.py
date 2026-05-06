def validate(age):
    if 1 <= age <= 100:
        return True
    return False

def test_valid_age():
    assert validate(1) is True
    assert validate(2) is True
    assert validate(99) is True
    assert validate(100) is True

def test_invalid_age():
    assert validate(0) is False
    assert validate(101) is False

