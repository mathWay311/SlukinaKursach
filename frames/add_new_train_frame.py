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

        self.coupe_wagon_label = tk.CTkLabel(self, text="Количество вагонов купе: 4", font=("Arial Bold", 15))
        self.coupe_wagon_label.pack()

        self.coupe_wagon = tk.CTkSlider(self, from_=3, to=5, command=self.slider_event_coupe)
        self.coupe_wagon.configure(number_of_steps=2)
        self.coupe_wagon.pack(pady=5)

        self.placcart_wagon_label = tk.CTkLabel(self, text="Количество вагонов плацкарт: 6", font=("Arial Bold", 15))
        self.placcart_wagon_label.pack()

        self.placcart_wagon = tk.CTkSlider(self, from_=5, to=7, command=self.slider_event_placcart)
        self.placcart_wagon.configure(number_of_steps=2)
        self.placcart_wagon.pack(pady=5)


        self.add_train_button = tk.CTkButton(self, text="Добавить поезд",
                                                                           fg_color="#FF7F50",
                                                                           font=("Arial Bold", 15),
                                                                       command=lambda: controller.add_new_train())
        self.add_train_button.pack(padx=10, pady=10)

        self.exit_submit = tk.CTkButton(self, text="В главное меню",
                                                                 fg_color="#FF6347",
                                                                 font=("Arial Bold", 15),
                                                                 command=lambda: controller.click_back_to_main_menu_admin())

        self.exit_submit.pack(padx=10, pady=10)

        self.pack()

    def slider_event_coupe(self, value):
        self.coupe_wagon_label.configure(text = "Количество вагонов купе: " + str(round(value)))

    def slider_event_placcart(self, value):
        self.placcart_wagon_label.configure(text = "Количество вагонов плацкарт: " + str(round(value)))