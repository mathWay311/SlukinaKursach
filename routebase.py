

class RouteBase:

    def __init__(self, routes_file_name):
        self.routes_file_name = routes_file_name

    def check_cities_when_buying(self, city_beg_entry, city_end_entry):
        file = open(self.routes_file_name, "r")
        for line in file.readlines():
            arguments = line.split(";")
            id_route = arguments[0]
            data = arguments[1]
            city_beg = arguments[2]
            city_end = arguments[3]
            if city_beg_entry == city_beg and city_end_entry == city_end:
                return data
        file.close()

    def output_date_route(self):
        file = open(self.routes_file_name, "r")

