import os
from tkinter import messagebox

PATH = "BaseData/"

class Table:
    def __init__(self, name):
        self.name = name
        self.path = PATH + name + ".db"
        self.column_config = []
        self.id_counter = 0

    def id_counter_refresh(self):
        file = open(self.path, "r")
        lines = file.readlines()
        last_line = lines[-1]
        last_ID = last_line.split(";")[0]
        self.id_counter = int(last_ID)

    def search_list(self, column, search_string):
        file = open(self.path, "r")
        for line in file.readlines():
            args = line.split(";")
            search_index = self.column_config.index(column)
            if args[search_index] == search_string:
                file.close()
                return args
        file.close()
        return False

    def search_line(self, column, search_string):
        file = open(self.path, "r")
        for line in file.readlines():
            args = line.split(";")
            search_index = self.column_config.index(column)
            if args[search_index] == search_string:
                file.close()
                return line
        file.close()
        return False

    def get_all(self):
        file = open(self.path, "r")
        lines = file.readlines()
        file.close()
        return lines

    def add_record(self, record):
        print(record)
        self.id_counter_refresh()
        file = open(self.path, "a")
        write_string = str(self.id_counter + 1) + ";" + record + "\n"
        print(write_string)
        file.write(write_string)

    def delete_by_id(self, id):
        lines = self.get_all()
        del_line = self.search_line("ID", id).strip()
        file = open(self.path, "w")
        for line in lines:
            print(line, del_line)
            if line.strip("\n") != del_line:
                file.write(line)
        file.close()
        print("DEBUG: DELETE OF", id, "COMPLETE")

#   <--------Таблицы--------->

users_table = Table("users")
users_table.column_config = ["Login", "Password", "Role"]

route_table = Table("route")
route_table.column_config = ["ID", "City_Beg", "City_End", "Name"]

#   <--------Таблицы--------->

class DB:
    def __init__(self):
        self.tables = {"users": users_table, "route": route_table}

    def get_all_from(self, table_name):
        return self.tables[table_name].get_all()

    def delete_by_id(self, table_name, id):
        self.tables[table_name].delete_by_id(id)

    def add_new_route(self, table_name, record):
        self.tables[table_name].add_record(record)
        messagebox.showinfo("Уведомление", "Успешно")


