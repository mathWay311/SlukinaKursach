import customtkinter as tk
from base_frame import BaseFrame
from tkinter import *


class BuyTicket(BaseFrame):

    def create_widgets(self, controller):


        self.buy_ticket_main_window_label_info = tk.CTkLabel(self)
        self.buy_ticket_main_window_label_info.pack()

        self.buy_ticket_main_window_label_city_begin = tk.CTkLabel(self, text="Город отправления", font=("Arial Bold", 13))
        self.buy_ticket_main_window_label_city_begin.pack(padx=7, pady=3)

        self.buy_ticket_main_window_label_city_begin = tk.CTkEntry(self, width=150)
        self.buy_ticket_main_window_label_city_begin.pack(padx=8, pady=5)

        self.buy_ticket_main_window_label_city_end = tk.CTkLabel(self, text="Город прибытия", font=("Arial Bold", 13))
        self.buy_ticket_main_window_label_city_end.pack(padx=7, pady=3)

        self.buy_ticket_main_window_label_city_end = tk.CTkEntry(self, width=150)
        self.buy_ticket_main_window_label_city_end.pack(padx=8, pady=5)

        self.buy_ticket_main_window_button_submit_search = tk.CTkButton(self, text="Поиск возможных рейсов", font=("Arial Bold", 15),
                                                                        command = lambda: controller.click_buy_ticket_search()
                                                                        )
        self.buy_ticket_main_window_button_submit_search.pack(padx=8, pady=10)

        self.list_to_route_buy_ticket = Listbox(self, selectbackground="green", width=50)
        self.list_to_route_buy_ticket.pack()

        self.buy_ticket_main_window_button_submit_next = tk.CTkButton(self, text="Выбрать рейс и перейти далее", font=("Arial Bold", 15))
        self.buy_ticket_main_window_button_submit_next.pack(padx=8, pady=10)

        self.buy_ticket_timetable_button_submit = tk.CTkButton(self, text="Вернуться назад",
                                                               font=("Arial Bold", 15),
                                                               command=lambda: controller.click_back_to_main_menu_cashier())

        self.buy_ticket_timetable_button_submit.pack(padx=100, pady=10)


        self.pack()