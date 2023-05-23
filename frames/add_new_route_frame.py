import customtkinter as tk
from base_frame import BaseFrame

class AddNewRoute(BaseFrame):

    def create_widgets(self, controller):
        self.add_route_main_window_label_info = tk.CTkLabel(self, text="Добавление нового рейса", font=("Arial Bold", 20))
        self.add_route_main_window_label_info.pack(padx=100, pady=5)

        self.add_route_main_window_label_data = tk.CTkLabel(self, text='Дата в формате: "дд мм чч:мм" (например: 12 мая 13:00)',
                                                                   font=("Arial Bold", 15))
        self.add_route_main_window_label_data.pack()

        self.add_route_main_window_entry_data = tk.CTkEntry(self, width=150)
        self.add_route_main_window_entry_data.pack(pady=5)

        self.add_route_main_window_label_city_beg = tk.CTkLabel(self, text="Город отправления", font=("Arial Bold", 15))
        self.add_route_main_window_label_city_beg.pack()

        self.add_route_main_window_entry_city_beg = tk.CTkEntry(self, width=150)
        self.add_route_main_window_entry_city_beg.pack(pady=5)

        self.add_route_main_window_label_city_end = tk.CTkLabel(self, text="Город прибытия", font=("Arial Bold", 15))
        self.add_route_main_window_label_city_end.pack()

        self.add_route_main_window_entry_city_end = tk.CTkEntry(self, width=150)
        self.add_route_main_window_entry_city_end.pack(pady=5)

        self.add_route_main_window_label_name_train = tk.CTkLabel(self, text="Название поезда",
                                                                      font=("Arial Bold", 15))
        self.add_route_main_window_label_name_train.pack()

        self.add_route_main_window_entry_name_train = tk.CTkEntry(self, width=150)
        self.add_route_main_window_entry_name_train.pack(padx=10, pady=5)

        self.add_route_main_window_button_submit_search = tk.CTkButton(self, text="Добавить рейс",
                                                                           fg_color="#FF7F50",
                                                                           font=("Arial Bold", 15),
                                                                       command=lambda: controller.add_new_route(lambda: self.add_route_main_window_label_data.get()))
        self.add_route_main_window_button_submit_search.pack(padx=10, pady=10)

        self.add_route_button_exit_submit = tk.CTkButton(self, text="В главное меню",
                                                                 fg_color="#FF6347",
                                                                 font=("Arial Bold", 15),
                                                                 command=lambda: controller.click_back_to_main_menu_admin())

        self.add_route_button_exit_submit.pack(padx=10, pady=10)

        self.pack()