import customtkinter as tk
from base_frame import BaseFrame


class UserFrame(BaseFrame):
    def create_widgets(self, controller):

        self.user_main_window_label_info = tk.CTkLabel(self, text="")
        self.user_main_window_label_info.place(x=120, y=45)
        self.user_main_window_label_info.pack()

        self.user_timetable_button_submit = tk.CTkButton(self, text="Выйти из системы",
                                                      width=40,
                                                      height=2,
                                                      command= lambda :controller.click_back_to_main_from_account())
        self.user_timetable_button_submit.place(x=55, y=100)
        self.user_timetable_button_submit.pack(padx=30, pady=20)
        self.pack()