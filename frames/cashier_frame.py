import customtkinter as tk
from base_frame import BaseFrame


class CashierFrame(BaseFrame):
    def create_widgets(self, controller):

        self.cashier_main_window_label_info = tk.CTkLabel(self, font=("Arial Bold", 20))
        self.cashier_main_window_label_info.pack(pady=10)

        self.cashier_main_window_button_buy_ticket = tk.CTkButton(self, text="Продажа билета",
                                                                width=200,
                                                                height=35,
                                                                font=("Arial Bold", 15), fg_color="#FF7F50",
                                                                command=lambda: controller.switch_to_frame("BuyTicket"))
        self.cashier_main_window_button_buy_ticket.pack(padx=120, pady=30)

        self.cashier_main_window_button_buy_ticket = tk.CTkButton(self, text="Возврат билета",
                                                                  width=200,
                                                                  height=35,
                                                                  font=("Arial Bold", 15), fg_color="#FF7F50",
                                                                  command=lambda: controller.switch_to_frame(
                                                                      "ReturnTicket"))
        self.cashier_main_window_button_buy_ticket.pack(padx=120, pady=30)

        self.cashier_timetable_button_exit_submit = tk.CTkButton(self, text="Выйти из системы",
                                                         width=200,
                                                         height=35, fg_color="#FF6347",
                                                         font=("Arial Bold", 15),
                                                         command=lambda: controller.click_back_to_main_from_account())
        self.cashier_timetable_button_exit_submit.pack(padx=120, pady=30)
        self.pack()
