class DataBase:
    def __init__(self, users_file_name):
        self.users_file_name = users_file_name

    def check_login(self, login, password):
        file = open(self.users_file_name, "r")
        success = False
        for line in file.readlines():
            print(line)
            if len(line.strip()) != 0:
                arguments = line.split(";")
                login_db = arguments[0]
                password_db = arguments[1]
                if login_db == login and password_db == password:
                    success = True
        file.close()
        return success

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

    def registration(self, login, password):
        is_account_present = self.check_account_presence(login)

        if is_account_present:
            return False
        else:
            file = open(self.users_file_name, "a")
            file.write(login + ";" + password + ";user;" + "\n")
            file.close()
            return True

