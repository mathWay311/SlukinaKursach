import customtkinter as tk
from base_frame import BaseFrame


class CashierFrame(BaseFrame):
    def create_widgets(self, controller):
        # XD бля не могу с этих cashier_main_window_label_info_pentagon_vzlomat_unichtozhit_label_computer_linux_windows_select_transaqt_bmw_audi_magnitola
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

class CashierRegistrationFrame(BaseFrame):
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
                                                    command=lambda :controller.click_registration_for_cashier())
        self.registration_button_submit.pack(padx=30, pady=20)

        self.registration_button_back = tk.CTkButton(self, text="Назад", fg_color="#FF6347",
                                                     width=200,
                                                     height=35,
                                                     font = ("Arial Bold", 15),
                                                     command=lambda :controller.click_back_to_main_menu_admin())
        self.registration_button_back.pack(padx=30, pady=10)
        self.pack()