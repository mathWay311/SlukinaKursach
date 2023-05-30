import customtkinter as tk
from base_frame import BaseFrame
from tkinter import *

class ReturnTicket(BaseFrame):

    def create_widgets(self, controller):

        self._label_info = tk.CTkLabel(self, text="Возврат билета", font=("Arial Bold", 20))
        self._label_info.pack()

        self.label_name = tk.CTkLabel(self, text="Имя", font=("Arial Bold", 15))
        self.label_name.pack()

        self.entry_name = tk.CTkEntry(self, width=150)
        self.entry_name.pack()

        self.label_surname = tk.CTkLabel(self, text="Фамилия",
                                                                   font=("Arial Bold", 15))
        self.label_surname.pack()

        self.entry_surname = tk.CTkEntry(self, width=150)
        self.entry_surname.pack()



        self.label_patronymic = tk.CTkLabel(self, text="Отчество", font=("Arial Bold", 15))
        self.label_patronymic.pack()

        self.entry_patronymic = tk.CTkEntry(self, width=150)
        self.entry_patronymic.pack()

        self.button_submit_search = tk.CTkButton(self, text="Поиск рейсов", fg_color="#FF7F50",
                                                                        font=("Arial Bold", 15),
                                                                        command=lambda: controller.click_return_ticket_search_for_cashier()
                                                                        )
        self.button_submit_search.pack(padx=8, pady=10)



        self.ticket_list = tk.CTkComboBox(self, width=300, values=[])
        self.ticket_list.set("")
        self.ticket_list.pack()

        self.button_submit_search = tk.CTkButton(self, text="Вернуть билет", fg_color="#FF7F50",
                                                                           font=("Arial Bold", 15),
                                                                           command=lambda: controller.click_delete_ticket()
                                                                           )
        self.button_submit_search.pack(padx=8, pady=5)

        self.button_submit_exit = tk.CTkButton(self, text="Вернуться назад", fg_color="#FF6347",
                                                               font=("Arial Bold", 15),
                                                               command=lambda: controller.click_back_to_main_menu_cashier())

        self.button_submit_exit.pack(padx=100, pady=10)

        self.pack()