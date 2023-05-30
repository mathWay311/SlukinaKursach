import customtkinter as tk
from base_frame import BaseFrame
from tkinter import *


class ShowTicketsFrame(BaseFrame):

    def create_widgets(self, controller):


        self.label_info = tk.CTkLabel(self, text="Ваши билеты", font=("Arial Bold", 20))
        self.label_info.pack(padx=10)

        self.tickets_label = tk.CTkLabel(self, text="У вас пока нет билетов", font=("Arial Bold", 16))
        self.tickets_label.pack(padx=10)

        tickets = self.controller.show_tickets_for_current_user()
        if len(tickets):
            text = ""
            for ticket in tickets:
                text += ticket + "\n"
            self.tickets_label.configure(text=text)
        else:
            self.tickets_label.configure(text="У вас пока нет билетов")



        self.timetable_button_submit = tk.CTkButton(self, text="Вернуться назад", fg_color="#FF6347",
                                                    font=("Arial Bold", 15),
                                                    command=lambda: controller.click_away_from_ticket_buy())


        self.timetable_button_submit2 = tk.CTkButton(self, text="Возврат билетов", fg_color="#FF6347",
                                                    font=("Arial Bold", 15),
                                                    command=lambda: controller.switch_to_frame("ReturnTicketUser"))
        self.timetable_button_submit2.pack(padx=100, pady=10)
        self.timetable_button_submit.pack(padx=100, pady=10)
        self.pack()

