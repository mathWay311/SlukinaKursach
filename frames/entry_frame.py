import customtkinter as tk
from base_frame import BaseFrame


class EntryFrame(BaseFrame):
    def create_widgets(self, controller):

        self.entry_label_info = tk.CTkLabel(self, text="Вход", font=("Arial Bold", 20))
        self.entry_label_info.place(x=165, y=45)
        self.entry_label_info.pack()

        self.entry_label_login = tk.CTkLabel(self, text="Логин:", font=("Arial Bold", 15))
        self.entry_label_login.place(x=65, y=125)
        self.entry_label_login.pack()

        self.entry_field_login = tk.CTkEntry(self, width=150)
        self.entry_field_login.place(x=150, y=130)
        self.entry_field_login.pack()

        self.entry_label_password = tk.CTkLabel(self, text="Пароль:", font=("Arial Bold", 15))
        self.entry_label_password.place(x=60, y=195)
        self.entry_label_password.pack()

        self.entry_field_password = tk.CTkEntry(self,width=150, show="*")
        self.entry_field_password.place(x=150, y=200)
        self.entry_field_password.pack()

        self.entry_button_submit = tk.CTkButton(self, text="Войти", width=40,
                                             height=2,
                                             command=lambda : controller.click_entry_submit())
        self.entry_button_submit.place(x=55, y=100)
        self.entry_button_submit.pack(padx=30, pady=20)

        self.entry_button_back = tk.CTkButton(self, text="Назад", width=40, height=2,
                                           command=lambda :controller.switch_to_frame("AuthFrame"))
        self.entry_button_back.place(x=55, y=100)
        self.entry_button_back.pack(padx=30, pady=20)
        self.pack()