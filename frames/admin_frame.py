import customtkinter as tk
from base_frame import BaseFrame
from PIL import Image



class AdminFrame(BaseFrame):
    def create_widgets(self, controller):

        self.admin_main_window_label_info = tk.CTkLabel(self, font=("Arial Bold", 20))
        self.admin_main_window_label_info.pack(pady=10)

        self.admin_main_menu_label_registration_cashier = tk.CTkButton(self, text="Регистрация нового кассира",
                                                            width=230,
                                                            height=35,
                                                            fg_color="#FF7F50",
                                                            font=("Arial Bold", 15),
                                                            command=lambda: controller.click_registration_for_cashier())
        self.admin_main_menu_label_registration_cashier.pack(padx=120, pady=20)

        self.admin_main_menu_label_registration_machinist = tk.CTkButton(self, text="Регистрация нового машиниста",
                                                                       fg_color="#FF7F50",
                                                                       width=230,
                                                                       height=35,
                                                                       font=("Arial Bold", 15),
                                                                       command=lambda: controller.click_registration_for_machinist())
        self.admin_main_menu_label_registration_machinist.pack(padx=120, pady=20)

        self.admin_main_menu_label_registration_add_new_route = tk.CTkButton(self, text="Рейсы",
                                                                         width=230,
                                                                         height=35,
                                                                         fg_color="#FF7F50",
                                                                         font=("Arial Bold", 15),
                                                                         command=lambda: controller.switch_to_frame("AddNewRoute"))
        self.admin_main_menu_label_registration_add_new_route.pack(padx=120, pady=20)

        self.admin_main_menu_label_add_new_train = tk.CTkButton(self, text="Поезда",
                                                                         fg_color="#FF7F50",
                                                                         width=230,
                                                                         height=35,
                                                                         font=("Arial Bold", 15))
        self.admin_main_menu_label_add_new_train.pack(padx=120, pady=20)


        self.admin_timetable_button_exit_submit = tk.CTkButton(self, text="Выйти из системы",
                                                            fg_color="#FF6347",
                                                            width=230,
                                                            height=35,
                                                            font=("Arial Bold", 15),
                                                            command=lambda: controller.click_back_to_main_from_account())
        self.admin_timetable_button_exit_submit.pack(padx=30, pady=20)
        self.pack()