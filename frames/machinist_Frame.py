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

class MachinistRegistrationFrame(BaseFrame):
    def create_widgets(self, controller):

        self.registration_label_info = tk.CTkLabel(self, text="Регистрация", font=("Arial Bold", 20))
        self.registration_label_info.pack(pady=10)

        self.registration_label_login = tk.CTkLabel(self, text="Логин (ФИО)", font=("Arial Bold", 15))
        self.registration_label_login.pack()

        self.registration_field_login = tk.CTkEntry(self, width=150)
        self.registration_field_login.pack()

        self.registration_label_password = tk.CTkLabel(self, text="Пароль", font=("Arial Bold", 15))
        self.registration_label_password.pack()

        self.registration_field_password = tk.CTkEntry(self, width=150, show="*", font=("Arial Bold", 15))
        self.registration_field_password.pack()

        self.registration_label_password_proof = tk.CTkLabel(self, text="Подтвердите пароль", font=("Arial Bold", 15))
        self.registration_label_password_proof.pack()

        self.registration_field_password_proof = tk.CTkEntry(self, width=150, show="*", font=("Arial Bold", 15))
        self.registration_field_password_proof.pack()

        self.registration_button_submit = tk.CTkButton(self, text="Зарегистрировать", width=200, fg_color="#2E8B57",
                                                    height=35,
                                                    font = ("Arial Bold", 15),
                                                    command=lambda :controller.click_registration_for_machinist())
        self.registration_button_submit.pack(padx=30, pady=20)

        self.registration_button_back = tk.CTkButton(self, text="Назад", fg_color="#FF6347",
                                                     width=200,
                                                     height=35,
                                                     font = ("Arial Bold", 15),
                                                     command=lambda :controller.switch_to_frame("AdminFrame"))
        self.registration_button_back.pack(padx=30, pady=10)
        self.pack()