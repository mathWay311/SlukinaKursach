import os
from tkinter import messagebox
from models import *

PATH = "BaseData/"

class Table:
    def __init__(self, name, model_name):
        self.name = name
        self.path = PATH + name + ".db"
        self.column_config = []
        self.id_counter = 0

        self.model_name = model_name
        self.model_class = globals()[model_name]

    def id_counter_refresh(self):
        file = open(self.path, "r")
        lines = file.readlines()
        if len(lines) > 0:
            last_line = lines[-1]
            last_ID = last_line.split(";")[0]
            self.id_counter = int(last_ID)

    def search_list(self, column, search_string) -> list[str] | bool:
        file = open(self.path, "r")
        for line in file.readlines():
            args = line.split(";")
            search_index = self.column_config.index(column)
            if args[search_index] == search_string:
                file.close()
                return args
        file.close()
        return False

    def search_line(self, column: str, search_string: str) -> str | bool:
        """
        Поиск строки в таблице БД по соответствию

        Args:
            column: Столбец для поиска
            search_string: Строка по которой производится поиск

        Returns:
            Строка таблицы БД или False в случае провала
        """
        file = open(self.path, "r")
        search_string = str(search_string)
        for line in file.readlines():
            args = line.split(";")
            search_index = self.column_config.index(column)
            if args[search_index] == search_string:
                file.close()
                return line
        file.close()
        return False

    def search_model(self, column: str, search_string: str) -> Model | bool:
        """
        Поиск строки в таблице БД по соответствию с выводом модели

        Args:
            column: Столбец для поиска
            search_string: Строка по которой производится поиск

        Returns:
            Строка таблицы БД или False в случае провала
        """
        file = open(self.path, "r")
        search_string = str(search_string)
        for line in file.readlines():
            args = line.split(";")
            search_index = self.column_config.index(column)
            if args[search_index] == search_string:
                file.close()
                item = self.model_class(args)
                return item
        file.close()
        return False

    def __get_all_lines(self) -> list[str]:
        """
        !Приватный метод!
        Возвращает список всех строк таблицы

        Returns:
            Список всех строк таблицы
        """
        file = open(self.path, "r")
        lines = file.readlines()
        return lines

    def get_all(self) -> list[Model]:
        """
        Получает список всех обьектов данной таблицы и переводит их список обьектов класса модели (Название класса модели инициализируются конструктором)

        Returns:
            Список обьектов модели таблицы
        """
        file = open(self.path, "r")
        lines = file.readlines()
        models = []
        for line in lines:
            args = line.split(";")
            models.append(self.model_class(args))
        return models

    def get_all_where(self, column: str, text: str) -> list[Model]:
        """
        Получает список всех обьектов данной таблицы и переводит их список обьектов класса модели (Название класса модели инициализируются конструктором)
        Обьекты фильтруются и передаются только те, где column == text

        Args:
            column: Название столбца
            text: Содержание для сравнения

        Returns:
            Список обьектов модели таблицы, где column == text

        """
        lines = self.__get_all_lines()
        models = []
        for line in lines:
            args = line.split(";")
            if args[self.column_config.index(column)] == text:
                models.append(self.model_class(line))
        return models

    def delete_by_id(self, id):
        lines = self.__get_all_lines()
        del_line = self.search_line("ID", id)
        if type(del_line) == bool:
            raise Exception("Обьект по ID не найден")
        del_line = del_line.strip()
        file = open(self.path, "w")
        for line in lines:
            if line.strip("\n") != del_line:
                file.write(line)
        file.close()

    def add_record(self,record) -> int:
        self.id_counter_refresh()
        file = open(self.path, "a")
        record = record.replace("\n", r"\\n")
        write_string = str(self.id_counter + 1) + ";" + record + "\n"
        file.write(write_string)
        return self.id_counter + 1

    def alter_record(self, id, column, text):
        lines = self.__get_all_lines()
        isAltered = False
        alter_line = self.search_line("ID", id)
        if not alter_line:
            print("SEARCH FAIL: NON-EXISTENT ID")

        else:
            file = open(self.path, "w")
            for line in lines:
                if line != alter_line:
                    file.write(line)

                else:
                    args = alter_line.split(";")
                    args.pop(-1)
                    print(self.column_config.index(column))
                    args[self.column_config.index(column)] = text
                    outline = ""
                    for arg in args:
                        outline += str(arg) + ";"
                    isAltered = True
                    outline = outline.replace("\n", r"\\n")
                    outline += "\n"
                    file.write(outline)
        if not isAltered:
            print("DEBUG: ALTER FAIL (ID:", id, ",COLUMN:", column, "TEXT:",text)



#   <--------Таблицы--------->

users_table = Table("users", "UserModel")
users_table.column_config = ["Login", "Password", "Role"]

route_table = Table("route", "RouteModel")
route_table.column_config = ["ID", "City_Beg", "City_End", "Name"]

wagon_table = Table("wagon", "WagonModel")
wagon_table.column_config = ["ID", "Type", "Number", "Seats", "TrainID"]

train_table = Table("train", "TrainModel")
train_table.column_config = ["ID", "Name"]


#   <--------Таблицы--------->

class DB:
    def __init__(self):
        self.tables = {"users": users_table, "route": route_table}

    def get_all_from(self, table_name):
        return self.tables[table_name].get_all()

    def delete_by_id(self, table_name, id):
        self.tables[table_name].delete_by_id(id)

    def add_new_route(self, table_name, record):
        result = self.tables[table_name].add_record(record)
        return result


