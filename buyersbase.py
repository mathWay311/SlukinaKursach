
class BuyersBase:

    def __init__(self, users_file_name):
        self.users_file_name = users_file_name

    def search_ticket(self, surname, name, patronymic):
        file = open(self.users_file_name, "r")
        list_buyers
        for line in file.readlines():
            arguments = line.split(";")
            surname_bd = arguments[1]
            name_bd = arguments[2]
            patronymic_bd = arguments[3]
            if surname_bd == surname and name_bd == name and patronymic_bd == patronymic:



    def delete_ticket(self):
            pass

