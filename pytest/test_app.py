from app import app_flow

def test_valid_login():
    assert app_flow("admin", "admin123") == "Welcome to dashboard, admin!"

def test_invalid_password():
    assert app_flow("admin", "wrong123") == "Login Failed"

def test_invalid_username():
    assert app_flow("user", "admin123") == "Login Failed"

def test_both_invalid():
    assert app_flow("user", "wrong") == "Login Failed"

