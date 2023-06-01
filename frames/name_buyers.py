import customtkinter as tk
from base_frame import BaseFrame
from tkinter import *


class BuyTicketPlace(BaseFrame):

    def create_widgets(self, controller):

        self.place_label_info = tk.CTkLabel(self, text="Выбор места", font=("Arial Bold", 20))
        self.place_label_info.pack(pady=10)

        self.place_label_login = tk.CTkLabel(self, text="Тип", font=("Arial Bold", 15))
        self.place_label_login.pack()

        self.place_main_window_entry_name_train = tk.CTkComboBox(self, width=150, state="readonly")
        self.place_main_window_entry_name_train.pack(padx=10, pady=5)

        self.place_label_password = tk.CTkLabel(self, text="Вагон", font=("Arial Bold", 15))
        self.place_label_password.pack()

        self.place_main_window_entry_name_train = tk.CTkComboBox(self, width=150, state="readonly")
        self.place_main_window_entry_name_train.pack(padx=10, pady=5)

        self.place_label_password_proof = tk.CTkLabel(self, text="Место", font=("Arial Bold", 15))
        self.place_label_password_proof.pack()

        self.place_main_window_entry_name_train = tk.CTkComboBox(self, width=150, state="readonly")
        self.place_main_window_entry_name_train.pack(padx=10, pady=5)

        self.place_button_submit = tk.CTkButton(self, text="Перейти далее", width=200, fg_color="#2E8B57",
                                               height=35,
                                               font=("Arial Bold", 15),
                                               command=lambda: controller.click_registration_submit())
        self.place_button_submit.pack(padx=30, pady=20)

        self.place_button_back = tk.CTkButton(self, text="Назад", fg_color="#FF6347",
                                             width=200,
                                             height=35,
                                             font=("Arial Bold", 15),
                                             command=lambda: controller.switch_to_frame("AuthFrame"))
        self.place_button_back.pack(padx=30, pady=10)
        self.pack()