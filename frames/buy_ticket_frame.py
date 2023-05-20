import customtkinter as tk
from base_frame import BaseFrame


class BuyTicket(BaseFrame):

    def create_widgets(self, controller):

        def create_widgets(self, controller):

            self.buy_ticket_main_window_label_info = tk.CTkLabel(self)
            self.buy_ticket_main_window_label_info.place(x=120, y=45)
            self.buy_ticket_main_window_label_info.pack()

            self.buy_ticket_timetable_button_submit = tk.CTkButton(self, text="Вернуться назад",
                                                                width=40,
                                                                height=2,
                                                                command=lambda: controller.click_back_to_main_menu_admin())
            self.buy_ticket_timetable_button_submit.place(x=55, y=100)
            self.buy_ticket_timetable_button_submit.pack(padx=30, pady=20)
            self.pack()