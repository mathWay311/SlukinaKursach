import customtkinter as tk
from base_frame import BaseFrame

class AddNewTrain(BaseFrame):

    def create_widgets(self, controller):
        self.add_route_main_window_label_info = tk.CTkLabel(self, text="Добавление нового поезда", font=("Arial Bold", 20))
        self.add_route_main_window_label_info.pack(padx=100, pady=5)



        self.train_name_label = tk.CTkLabel(self, text="Название поезда", font=("Arial Bold", 15))
        self.train_name_label.pack()

        self.train_name = tk.CTkEntry(self, width=150)
        self.train_name.pack(pady=5)

        self.add_route_main_window_label_city_end = tk.CTkLabel(self, text="Город прибытия", font=("Arial Bold", 15))
        self.add_route_main_window_label_city_end.pack()

        self.add_route_main_window_entry_city_end = tk.CTkEntry(self, width=150)
        self.add_route_main_window_entry_city_end.pack(pady=5)

        self.add_route_main_window_label_name_train = tk.CTkLabel(self, text="Выбрать поезд",
                                                                      font=("Arial Bold", 15))
        self.add_route_main_window_label_name_train.pack()

        self.add_route_main_window_entry_name_train = tk.CTkComboBox(self, width=150, state="readonly")
        self.add_route_main_window_entry_name_train.pack(padx=10, pady=5)

        self.add_route_main_window_label_name_machinist = tk.CTkLabel(self, text="Назначить машиниста",
                                                                  font=("Arial Bold", 15))
        self.add_route_main_window_label_name_machinist.pack(padx=10, pady=5)

        self.add_route_main_window_entry_name_machinist = tk.CTkComboBox(self, width=150, state="readonly")
        self.add_route_main_window_entry_name_machinist.pack(padx=10, pady=5)

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
                                                                       command=lambda: controller.add_new_train())
        self.add_route_main_window_button_submit_search.pack(padx=10, pady=10)

        self.add_route_button_exit_submit = tk.CTkButton(self, text="В главное меню",
                                                                 fg_color="#FF6347",
                                                                 font=("Arial Bold", 15),
                                                                 command=lambda: controller.click_back_to_main_menu_admin())

        self.add_route_button_exit_submit.pack(padx=10, pady=10)

        self.pack()