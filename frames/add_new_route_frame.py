import datetime
from tkinter import messagebox

import customtkinter as tk
from base_frame import BaseFrame

class AddNewRoute(BaseFrame):

    def create_widgets(self, controller):
        self.controller = controller
        self.add_route_main_window_label_info = tk.CTkLabel(self, text="Добавление нового рейса", font=("Arial Bold", 20))
        self.add_route_main_window_label_info.pack(padx=100, pady=5)

        self.add_route_main_window_label_data = tk.CTkLabel(self, text='Дата',
                                                                   font=("Arial Bold", 15))
        self.add_route_main_window_label_data.pack()

        self.entry_data = tk.CTkEntry(self, width=150)
        self.entry_data.pack(pady=5)

        self.add_route_main_window_label_city_beg = tk.CTkLabel(self, text="Город отправления", font=("Arial Bold", 15))
        self.add_route_main_window_label_city_beg.pack()

        self.entry_city_beg = tk.CTkEntry(self, width=150)
        self.entry_city_beg.pack(pady=5)

        self.label_city_end = tk.CTkLabel(self, text="Город прибытия", font=("Arial Bold", 15))
        self.label_city_end.pack()

        self.entry_city_end = tk.CTkEntry(self, width=150)
        self.entry_city_end.pack(pady=5)

        self.label_name_train = tk.CTkLabel(self, text="Выбрать поезд",
                                                                      font=("Arial Bold", 15))
        self.label_name_train.pack()

        models = controller.get_available_trains()
        avail_trains = []
        for model in models:
            avail_trains.append(str(model.name))

        self.entry_name_train = tk.CTkComboBox(self, width=150, state="readonly")
        self.entry_name_train.configure(values=avail_trains)
        self.entry_name_train.pack(padx=10, pady=5)

        self.label_name_machinist = tk.CTkLabel(self, text="Назначить машиниста",
                                                                  font=("Arial Bold", 15))
        self.label_name_machinist.pack(padx=10, pady=5)

        models = controller.get_available_machinists()
        avail_machinists = []
        for model in models:
            avail_machinists.append(str(model.name))

        self.entry_name_machinist = tk.CTkComboBox(self, width=150, state="readonly")
        self.entry_name_machinist.configure(values=avail_machinists)
        self.entry_name_machinist.pack(padx=10, pady=5)

        """
        available_machinists = controller.get_available_machinist()
        list_directions = []
        for dir in available_machinists:
            list_directions.append(dir.name + " " + dir.password + " " + dir.role)

        self.add_route_main_window_label_name_machinist.configure(values=list_directions)
        if len(list_directions):
            self.add_route_main_window_label_name_machinist.set(list_directions[0])
        else:
            self.add_route_main_window_label_name_machinist.set("")
        self.add_route_main_window_label_name_machinist.pack()
        """

        self.add_route_main_window_button_submit_search = tk.CTkButton(self, text="Добавить рейс",
                                                                           fg_color="#FF7F50",
                                                                           font=("Arial Bold", 15),
                                                                       command=lambda: self.before_adding_route_check())
        self.add_route_main_window_button_submit_search.pack(padx=10, pady=10)

        self.add_route_button_exit_submit = tk.CTkButton(self, text="Назад",
                                                                 fg_color="#FF6347",
                                                                 font=("Arial Bold", 15),
                                                                 command=lambda: controller.show_routes())

        self.add_route_button_exit_submit.pack(padx=10, pady=10)

        self.pack()

    def before_adding_route_check(self):
        if self.__check_time():
            self.controller.add_new_route()
        else:
            messagebox.showerror("Рейс не создан", "Произошла ошибка при введении времени. Рейс не будет создан.")

    def __check_time(self):

            date_start_str = self.entry_data.get()

            if len(date_start_str.split(" ")) == 2:
                if len(date_start_str.split(" ")[0].split(".")) == 3:
                    if len(date_start_str.split(" ")[1].split(":")) == 2:
                        start_args_date = date_start_str.split(" ")[0].split(".")
                        for i in range(len(start_args_date)):
                            try:
                                start_args_date[i] = int(start_args_date[i])
                            except:
                                messagebox.showerror("Ошибка",
                                                     "Недопустимый формат времени!\n Проверьте на соответствие шаблону (DD.MM.YYYY HH:MM)\nПроверьте, что вводите цифры!")
                                return False
                        start_args_time = date_start_str.split(" ")[1].split(":")
                        for i in range(len(start_args_time)):
                            try:
                                start_args_time[i] = int(start_args_time[i])
                            except:
                                messagebox.showerror("Ошибка",
                                                     "Недопустимый формат времени!\n Проверьте на соответствие шаблону (DD.MM.YYYY HH:MM)\nПроверьте, что вводите цифры!")
                                return False



                        date_start = datetime.datetime(year=start_args_date[2], month=start_args_date[1],
                                                       day=start_args_date[0], hour=start_args_time[0],
                                                       minute=start_args_time[1])



                        if ((date_start - datetime.datetime.now()).total_seconds() <= 0):
                            messagebox.showerror("Ошибка",
                                                 "Дата начала раньше текущей даты или точно совпадает с текущим временем.")
                            return False
                        return True
            return False