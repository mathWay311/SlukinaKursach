import customtkinter as tk
from base_frame import BaseFrame


class UserFrame(BaseFrame):
    def create_widgets(self, controller):

        self.user_main_window_label_info = tk.CTkLabel(self, font=("Arial Bold", 20))
        self.user_main_window_label_info.pack(pady=10)

        self.user_main_window_button_buy_ticket = tk.CTkButton(self, text="Купить билет", fg_color="#FF7F50",
                                                                  width=200,
                                                                  height=35,
                                                                  font=("Arial Bold", 15),
                                                                  command=lambda: controller.switch_to_frame(
                                                                      "BuyTicket"))
        self.user_main_window_button_buy_ticket.pack(padx=120, pady=30)

        self.user_main_window_button_purchase_tickets = tk.CTkButton(self, text="Приобретённые билеты", fg_color="#FF7F50",
                                                                  width=200,
                                                                  height=35,
                                                                  font=("Arial Bold", 15))
        self.user_main_window_button_purchase_tickets.pack(padx=120, pady=30)

        self.user_timetable_button_exit_submit = tk.CTkButton(self, text="Выйти из системы", fg_color="#FF6347",
                                                      width=200,
                                                      height=35,
                                                      font=("Arial Bold", 15),
                                                      command= lambda :controller.click_back_to_main_from_account())
        self.user_timetable_button_exit_submit.pack(padx=30, pady=30)
        self.pack()