class Model:
    def __init__(self, line : list):
        pass

class BuyerModel(Model):
    def __init__(self, line):
        super().__init__(line)
        self.id = int(line[0])
        self.surname = line[1]
        self.name = line[2]
        self.patronymic = line[3]
        self.pass_serial = line[4]
        self.pass_number = line[5]
        self.login = line[6]
        self.routeID = int(line[7])
        self.wagonID = int(line[8])
        self.place = line[9]


class RouteModel(Model):
    def __init__(self, line):
        super().__init__(line)
        self.id = int(line[0])
        self.dept_time = line[1]
        self.from_ = line[2]
        self.to_ = line[3]
        self.trainID = int(line[4])
        self.machinistID = int(line[5])


class TrainModel(Model):
    def __init__(self, line):
        super().__init__(line)
        self.id = int(line[0])
        self.name = line[1]
        self.isOccupied = bool(int(line[2]))

    def db_add_string(self) -> str:
        """
        Возвращает строку, которую можно поместить в db.add_record()

        :return: Строка
        """
        return self.name + ";" + str(self.isOccupied) + ";"


class UserModel(Model):
    def __init__(self, line):
        super().__init__(line)
        self.id = int(line[0])
        self.from_ = line[1]
        self.to_ = line[2]


class WagonModel(Model):
    def __init__(self, line):
        super().__init__(line)
        self.id = int(line[0])
        self.type = line[1]
        self.number= line[2]
        self.seats_string = line[3]
        self.trainID = int(line[4])

    def db_add_string(self) -> str:
        """
        Возвращает строку, которую можно поместить в db.add_record()

        :return: Строка
        """
        if self.type == "Купе":
            self.seats_string = "0" * 10
        if self.type == "Плацкарт":
            self.seats_string = "0" * 20
        return self.type + ";" + self.number + ";" + self.seats_string + ";" + str(self.trainID) + ";"

