# Коды ошибок
# 100 - Успех
# 400 - Слишком короткий логин
# 401 - Слишком короткий пароль
# 402 - Слишком длинный логин
# 403 - Слишком длинный пароль

errorcodes_descriptions = { 400 : "Пароли не совпадают",
                            401 : "Слишком короткий логин",
                            402 : "Слишком короткий пароль",
                            403 : "Слишком длинный логин",
                            404 : "Слишком длинный пароль"}

MINIMUM_LOGIN_LENGTH = 3
MINIMUM_PASSWORD_LENGTH = 6

MAXIMUM_LOGIN_LENGTH = 15
MAXIMUM_PASSWORD_LENGTH = 15


def check_login_and_password_for_register(login, password, password_proof):
    if password != password_proof:
        return 400
    if len(login) < MINIMUM_LOGIN_LENGTH:
        return 401
    if len(password) < MINIMUM_PASSWORD_LENGTH:
        return 402
    if len(login) > MAXIMUM_LOGIN_LENGTH:
        return 403
    if len(password) > MAXIMUM_PASSWORD_LENGTH:
        return 404
    return 100
