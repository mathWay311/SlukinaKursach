import customtkinter as tk
from base_frame import BaseFrame

class AuthFrame(BaseFrame):
    def create_widgets(self, controller):

        self.main_label_welcome = tk.CTkLabel(self, text="Добро пожаловать!")  # Создаём лэйбел, первым параметром указываем какому фрейму принадлежит
        self.main_label_welcome.place(x=75,
                                      y=30)
        self.main_label_welcome.pack(padx=30,
                                     pady=20)

        self.main_button_entry = tk.CTkButton(self, text="Войти", width=40, height=2,
                                           command= lambda : controller.switch_to_frame("EntryFrame"))
        self.main_button_entry.place(x=55, y=100)
        self.main_button_entry.pack(padx=30, pady=20)

        self.main_button_registration = tk.CTkButton(self, text="Регистрация", width=40, height=2,
                                                  command=lambda : controller.switch_to_frame("RegistrationFrame"))
        self.main_button_registration.place(x=55, y=180)
        self.main_button_registration.pack(padx=30, pady=20)

        self.pack()  # Наконец, упаковываем весь фрейм для отображения на экране.