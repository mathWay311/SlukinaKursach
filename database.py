class DataBase:
    def __init__(self, users_file_name):
        self.users_file_name = users_file_name

        # Определение роли

        role = {
            100 : "Ошибка",
            101 : "Администратор",
            102 : "Пассажир",
            103 : "Кассир",
            104 : "Машинист"
        }

# Проверка логина и пароля, а также определение роли
    def check_login(self, login, password):
        file = open(self.users_file_name, "r")
        for line in file.readlines():
            if len(line.strip()) != 0:
                arguments = line.split(";")
                login_db = arguments[0]
                password_db = arguments[1]
                role_db = arguments[2]
                if login_db == login and password_db == password:
                    if role_db == 'admin':
                        return 101
                    elif role_db == 'user':
                        return 102
                    elif role_db == 'cashier':
                        return 103
                    elif role_db == 'machinist':
                        return 104
                    else:
                        return 100

        file.close()


    #Проверка, чтобы логины не повторялись
    def check_account_presence(self, login):
        file = open(self.users_file_name, "r")
        success = False
        for line in file.readlines():
            arguments = line.split(";")
            login_db = arguments[0]
            if login_db == login:
                success = True
        file.close()
        return success

    def registration(self, login, password, role):
        is_account_present = self.check_account_presence(login)

        if is_account_present:
            return False
        else:
            file = open(self.users_file_name, "a")
            file.write(login + ";" + password + ";" + role + ";" + "\n")
            file.close()
            return True



