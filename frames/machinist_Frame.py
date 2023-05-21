import customtkinter as tk
from base_frame import BaseFrame


class MachinistFrame(BaseFrame):
    def create_widgets(self, controller):

        self.machinist_main_window_label_info = tk.CTkLabel(self, font=("Arial Bold", 20))
        self.machinist_main_window_label_info.pack(pady=10)

        self.machinist_main_window_button_buy_ticket = tk.CTkButton(self, text="Посмотреть расписание", fg_color="#FF7F50",
                                                                  width=200,
                                                                  height=35,
                                                                  font=("Arial Bold", 15))
        self.machinist_main_window_button_buy_ticket.pack(padx=120, pady=30)


        self.machinist_timetable_button_exit_submit = tk.CTkButton(self, text="Выйти из системы", fg_color="#FF6347",
                                                           width=200,
                                                           height=35,
                                                           font=("Arial Bold", 15),
                                                           command=lambda: controller.click_back_to_main_from_account())
        self.machinist_timetable_button_exit_submit.place(x=55, y=100)
        self.machinist_timetable_button_exit_submit.pack(padx=30, pady=20)
        self.pack()