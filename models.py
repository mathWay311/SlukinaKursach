class Model:
    def __init__(self, line : list):
        pass

class MachinistModel(Model):
    def __init__(self, line):
        super().__init__(line)
        self.name = line[0]
        self.password = line[1]
        self.role = line[2]