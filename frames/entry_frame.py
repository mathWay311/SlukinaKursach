import customtkinter as tk
from base_frame import BaseFrame


class EntryFrame(BaseFrame):
    def create_widgets(self, controller):

        self.entry_label_info = tk.CTkLabel(self, text="Вход", font=("Arial Bold", 20))
        self.entry_label_info.pack(pady=10)

        self.entry_label_login = tk.CTkLabel(self, text="Логин", font=("Arial Bold", 15))
        self.entry_label_login.pack()

        self.entry_field_login = tk.CTkEntry(self, width=150)
        self.entry_field_login.pack()

        self.entry_label_password = tk.CTkLabel(self, text="Пароль", font=("Arial Bold", 15))
        self.entry_label_password.pack()

        self.entry_field_password = tk.CTkEntry(self, width=150, show="*")
        self.entry_field_password.pack()

        self.entry_button_submit = tk.CTkButton(self, text="Войти", width=200, fg_color="#2E8B57",
                                             height=35,
                                             font = ("Arial Bold", 15),
                                             command=lambda : controller.click_entry_submit())
        self.entry_button_submit.pack(padx=30, pady=20)

        self.entry_button_back = tk.CTkButton(self, text="Назад", width=200, height=35, fg_color="#FF6347",
                                           font = ("Arial Bold", 15),
                                           command=lambda :controller.switch_to_frame("AuthFrame"))
        self.entry_button_back.pack(padx=30, pady=10)
        self.pack()