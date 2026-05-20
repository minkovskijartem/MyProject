def check_auth(username, password):
    if username == "admin" and password == "secret":
        return True
    return False

# Тест роботи CI конвеєра