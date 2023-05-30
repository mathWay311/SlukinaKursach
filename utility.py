# Коды ошибок
# 100 - Успех

from tkinter import messagebox
from use_BD import DB

errorcodes_descriptions = { 400 : "Пароли не совпадают",
                            401 : "Слишком короткий логин",
                            402 : "Слишком короткий пароль",
                            403 : "Слишком длинный логин",
                            404 : "Слишком длинный пароль",
                            405 : "Город отправления и прибытия не могут совпадать",
                            406 : "Пустое имя поезда",
                            407 : "Такое название поезда уже существует",
                            408 : "Неправильные пасспортные данные"
                            }

MINIMUM_LOGIN_LENGTH = 4
MINIMUM_PASSWORD_LENGTH = 6

MAXIMUM_LOGIN_LENGTH = 30
MAXIMUM_PASSWORD_LENGTH = 30


def check_login_and_password_for_register(login : str, password : str, password_proof : str) -> int:
    """

    :param login: Логин
    :param password: Пароль
    :param password_proof: Подтверждение пароля
    :return: Код ошибки или успеха
    """
    if password != password_proof:
        return 400
    if len(login.strip()) < MINIMUM_LOGIN_LENGTH:
        return 401
    if len(password.strip()) < MINIMUM_PASSWORD_LENGTH:
        return 402
    if len(login.strip()) > MAXIMUM_LOGIN_LENGTH:
        return 403
    if len(password.strip()) > MAXIMUM_PASSWORD_LENGTH:
        return 404
    return 100

def check_route_for_register(beg_city, end_city):
    if beg_city == end_city:
        return 405
    return 100

def check_ticket(name_, surname_, patronymic_, serial_, number_, login_, route_id_, wagon_id_, place_):
    if len(serial_) != 4 or len(number_) != 6 or not serial_.isdigit() or not number_.isdigit():
        return 408
    return 100


def check_train(name : str) -> int:
    """
    Проверяет при создании поезда правильность введённых данных

    :param name: Название поезда
    :return: Результат проверки
    """
    db = DB()
    trains = db.get_all_from("train")

    for train in trains:
        if train.name == name:
            return 407

    if len(name.strip()) == 0:
        return 406
    return 100
