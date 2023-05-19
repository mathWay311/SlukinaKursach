import customtkinter as tk
from base_frame import BaseFrame


class RegistrationFrame(BaseFrame):
    def create_widgets(self, controller):

        self.registration_label_info = tk.CTkLabel(self, text="Регистрация")
        self.registration_label_info.place(x=120, y=45)
        self.registration_label_info.pack()

        self.registration_label_login = tk.CTkLabel(self, text="Логин:")
        self.registration_label_login.place(x=65, y=125)
        self.registration_label_login.pack()

        self.registration_field_login = tk.CTkEntry(self, width=150)
        self.registration_field_login.place(x=150, y=130)
        self.registration_field_login.pack()

        self.registration_label_password = tk.CTkLabel(self, text="Пароль:")
        self.registration_label_password.place(x=60, y=195)
        self.registration_label_password.pack()

        self.registration_field_password = tk.CTkEntry(self, width=150, show="*")
        self.registration_field_password.place(x=150, y=200)
        self.registration_field_password.pack()

        self.registration_label_password_proof = tk.CTkLabel(self, text="Подтвердите пароль:")
        self.registration_label_password_proof.place(x=60, y=195)
        self.registration_label_password_proof.pack()

        self.registration_field_password_proof = tk.CTkEntry(self, width=150, show="*")
        self.registration_field_password_proof.place(x=150, y=200)
        self.registration_field_password_proof.pack()

        self.registration_button_submit = tk.CTkButton(self, text="Зарегистрироваться", width=40,
                                                    height=2,
                                                    command=lambda :controller.click_registration_submit())
        self.registration_button_submit.place(x=55, y=100)
        self.registration_button_submit.pack(padx=30, pady=20)

        self.registration_button_back = tk.CTkButton(self, text="Назад", width=40, height=2,  command=lambda :controller.switch_to_frame("AuthFrame"))
        self.registration_button_back.place(x=55, y=100)
        self.registration_button_back.pack(padx=30, pady=20)
        self.pack()