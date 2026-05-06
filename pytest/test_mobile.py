def validate_mobile(number):
    if len(number) == 10 and number.isdigit():
        return True
    return False

import pytest



# TC1: Valid number
def test_valid_number():
    assert validate_mobile("9876543210") == True


# TC2: Less than 10 digits
def test_less_than_10_digits():
    assert validate_mobile("987654321") == False


# TC3: More than 10 digits
def test_more_than_10_digits():
    assert validate_mobile("98765432101") == False


# TC4: Contains alphabets
def test_contains_alphabets():
    assert validate_mobile("98765abc10") == False


# TC5: Contains special characters
def test_contains_special_characters():
    assert validate_mobile("98765@3210") == False


# TC6: Empty input
def test_empty_input():
    assert validate_mobile("") == False


# TC7: Spaces included
def test_spaces_included():
    assert validate_mobile("98765 43210") == False