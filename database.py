class DataBase:
    def __init__(self, users_file_name):
        self.users_file_name = users_file_name

    def check_login(self, login, password):
        file = open(self.users_file_name, "r")
        success = False
        for line in file.readlines():
            arguments = line.split(";")
            login_db = arguments[0]
            password_db = arguments[1]
            if login_db == login and password_db == password:
                success = True
        file.close()
        return success

    def registration(self, login, password):
        file = open(self.users_file_name, "r+")
        success = True
        for line in file:
            line = line.split(";")
            if login == line[0]:
                success = False
                file.close()
                break
            else:
                file.write(login + ";" + password + "\n")
                file.close()
                break

        return success

