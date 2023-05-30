import customtkinter as tk
from base_frame import BaseFrame
from tkinter import *

class ReturnTicketUser(BaseFrame):

    def create_widgets(self, controller):

        self._label_info = tk.CTkLabel(self, text="Возврат билета", font=("Arial Bold", 20))
        self._label_info.pack()

        tickets = self.controller.show_tickets_for_current_user_withIDS()

        self.ticket_list = tk.CTkComboBox(self, width=300, values=tickets)
        self.ticket_list.set("")
        self.ticket_list.pack()


        self.button_submit_search = tk.CTkButton(self, text="Вернуть билет", fg_color="#FF7F50",
                                                                           font=("Arial Bold", 15),
                                                                           command=lambda: self.delete_ticket()
                                                                           )
        self.button_submit_search.pack(padx=8, pady=5)

        self.button_submit_exit = tk.CTkButton(self, text="Вернуться назад", fg_color="#FF6347",
                                                               font=("Arial Bold", 15),
                                                               command=lambda: controller.click_back_to_main_menu_user())

        self.button_submit_exit.pack(padx=100, pady=10)

        self.pack()
    def delete_ticket(self):
        if len(self.ticket_list.get().strip()) != 0:
            self.controller.click_delete_ticket()