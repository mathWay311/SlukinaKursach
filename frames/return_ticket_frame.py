import customtkinter as tk
from base_frame import BaseFrame
from tkinter import *

class ReturnTicket(BaseFrame):

    def create_widgets(self, controller):

        self.return_ticket_main_window_label_info = tk.CTkLabel(self, text="Возврат билета", font=("Arial Bold", 20))
        self.return_ticket_main_window_label_info.pack()

        self.return_ticket_main_window_label_surname = tk.CTkLabel(self, text="Фамилия",
                                                                   font=("Arial Bold", 15))
        self.return_ticket_main_window_label_surname.pack()

        self.return_ticket_main_window_entry_surname = tk.CTkEntry(self, width=150)
        self.return_ticket_main_window_entry_surname.pack()

        self.return_ticket_main_window_label_name = tk.CTkLabel(self, text="Имя", font=("Arial Bold", 15))
        self.return_ticket_main_window_label_name.pack()

        self.return_ticket_main_window_entry_name = tk.CTkEntry(self, width=150)
        self.return_ticket_main_window_entry_name.pack()

        self.return_ticket_main_window_label_patronymic = tk.CTkLabel(self, text="Отчество", font=("Arial Bold", 15))
        self.return_ticket_main_window_label_patronymic.pack()

        self.return_ticket_main_window_entry_patronymic = tk.CTkEntry(self, width=150)
        self.return_ticket_main_window_entry_patronymic.pack()

        self.return_ticket_main_window_button_submit_search = tk.CTkButton(self, text="Поиск рейсов", fg_color="#FF7F50",
                                                                        font=("Arial Bold", 15),
                                                                        command=lambda: controller.click_return_ticket_search_for_cashier()
                                                                        )
        self.return_ticket_main_window_button_submit_search.pack(padx=8, pady=10)

        self.list_to_route_return_ticket_for_cashier = Listbox(self, selectbackground="green", width=50)
        self.list_to_route_return_ticket_for_cashier.pack()

        self.return_ticket_main_window_button_submit_search = tk.CTkButton(self, text="Вернуть билет", fg_color="#FF7F50",
                                                                           font=("Arial Bold", 15),
                                                                           command=lambda: controller.click_delete_ticket()
                                                                           )
        self.return_ticket_main_window_button_submit_search.pack(padx=8, pady=5)

        self.return_ticket_timetable_button_submit_exit = tk.CTkButton(self, text="Вернуться назад", fg_color="#FF6347",
                                                               font=("Arial Bold", 15),
                                                               command=lambda: controller.click_back_to_main_menu_cashier())

        self.return_ticket_timetable_button_submit_exit.pack(padx=100, pady=10)

        self.pack()