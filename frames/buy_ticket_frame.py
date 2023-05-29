import customtkinter as tk
from base_frame import BaseFrame
from tkinter import *


class BuyTicket(BaseFrame):

    def create_widgets(self, controller):


        self.label_info = tk.CTkLabel(self, text="Покупка билета", font=("Arial Bold", 20))
        self.label_info.pack(padx=10)

        self.label_city_begin = tk.CTkLabel(self, text="Город отправления", font=("Arial Bold", 15))
        self.label_city_begin.pack()

        self.label_city_begin = tk.CTkEntry(self, width=150)
        self.label_city_begin.pack()

        self.label_city_end = tk.CTkLabel(self, text="Город прибытия", font=("Arial Bold", 15))
        self.label_city_end.pack()

        self.label_city_end = tk.CTkEntry(self, width=150)
        self.label_city_end.pack()

        self.button_submit_search = tk.CTkButton(self, text="Поиск возможных рейсов", font=("Arial Bold", 15), fg_color="#FF7F50",
                                                                        command = lambda: controller.click_buy_ticket_search())
        self.button_submit_search.pack(padx=8, pady=10)

        self.list_to_route_buy_ticket = tk.CTkComboBox(self, width=300, values=[])
        self.list_to_route_buy_ticket.set("")
        self.list_to_route_buy_ticket.pack()

        self.button_submit_next = tk.CTkButton(self, text="Выбрать рейс и перейти далее", font=("Arial Bold", 15), fg_color="#FF7F50")
        self.button_submit_next.pack(padx=8, pady=10)

        self.timetable_button_submit = tk.CTkButton(self, text="Вернуться назад", fg_color="#FF6347",
                                                               font=("Arial Bold", 15))
        self.timetable_button_submit.pack(padx=100, pady=10)


        self.pack()