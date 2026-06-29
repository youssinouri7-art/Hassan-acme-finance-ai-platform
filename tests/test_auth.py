from src.auth import validate_user

def test_valid_user():
    assert validate_user("developer@acmebank.example") is True

def test_invalid_user():
    assert validate_user("attacker@example.com") is False
