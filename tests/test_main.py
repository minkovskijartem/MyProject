from src.main import check_auth

def test_check_auth():
    assert check_auth("admin", "secret") is True
    assert check_auth("user", "1234") is False