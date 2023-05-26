# Коды ошибок
# 100 - Успех

errorcodes_descriptions = { 400 : "Пароли не совпадают",
                            401 : "Слишком короткий логин",
                            402 : "Слишком короткий пароль",
                            403 : "Слишком длинный логин",
                            404 : "Слишком длинный пароль",
                            405 : "Город отправления и прибытия не могут совпадать"
                            }

MINIMUM_LOGIN_LENGTH = 4
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

def check_route_for_register(beg_city, end_city):
    if beg_city == end_city:
        return 405
    return 100
