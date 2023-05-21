import customtkinter as tk
from base_frame import BaseFrame

class AuthFrame(BaseFrame):
    def create_widgets(self, controller):

        self.main_label_welcome = tk.CTkLabel(self, text="Добро пожаловать!", font=("Arial Bold", 20))  # Создаём лэйбел, первым параметром указываем какому фрейму принадлежит
        self.main_label_welcome.pack(padx=30,
                                     pady=20)

        self.main_button_entry = tk.CTkButton(self, text="Войти", width=200, height=35, font=("Arial Bold", 15),
                                           command= lambda : controller.switch_to_frame("EntryFrame"), fg_color="#FF7F50")
        self.main_button_entry.pack(padx=30, pady=20)

        self.main_button_registration = tk.CTkButton(self, text="Регистрация", width=200, height=35, font=("Arial Bold", 15), fg_color="#FF7F50",
                                                  command=lambda : controller.switch_to_frame("RegistrationFrame"))
        self.main_button_registration.pack(padx=30, pady=20)

        self.pack()  # Наконец, упаковываем весь фрейм для отображения на экране.