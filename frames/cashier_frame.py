import customtkinter as tk
from base_frame import BaseFrame


class CashierFrame(BaseFrame):
    def create_widgets(self, controller):

        self.cashier_main_window_label_info = tk.CTkLabel(self, font=("Arial Bold", 20))
        self.cashier_main_window_label_info.pack(padx=120, pady=20)

        self.cashier_main_window_button_buy_ticket = tk.CTkButton(self, text="Продажа билета",
                                                                width=200,
                                                                height=35,
                                                                font=("Arial Bold", 15),
                                                                command=lambda: controller.switch_to_frame("BuyTicket"))
        self.cashier_main_window_button_buy_ticket.pack(padx=120, pady=50)

        self.cashier_timetable_button_submit = tk.CTkButton(self, text="Выйти из системы",
                                                         width=200,
                                                         height=35,
                                                         font=("Arial Bold", 15),
                                                         command=lambda: controller.click_back_to_main_from_account())
        self.cashier_timetable_button_submit.pack(padx=120, pady=100)
        self.pack()
