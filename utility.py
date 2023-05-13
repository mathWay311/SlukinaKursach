# Коды ошибок
# 100 - Успех
# 400 - Слишком короткий логин
# 401 - Слишком короткий пароль
# 402 - Слишком длинный логин
# 403 - Слишком длинный пароль

errorcodes_descriptions = { 400 : "Слишком короткий логин",
                            401 : "Слишком короткий пароль",
                            402 : "Слишком длинный логин",
                            403 : "Слишком длинный пароль"}

MINIMUM_LOGIN_LENGTH = 3
MINIMUM_PASSWORD_LENGTH = 6

MAXIMUM_LOGIN_LENGTH = 15
MAXIMUM_PASSWORD_LENGTH = 15


def check_login_and_password_for_register(login, password):
    if len(login) < MINIMUM_LOGIN_LENGTH:
        return 400
    if len(password) < MINIMUM_PASSWORD_LENGTH:
        return 401
    if len(login) > MAXIMUM_LOGIN_LENGTH:
        return 402
    if len(password) > MAXIMUM_PASSWORD_LENGTH:
        return 403
    return 100
