import customtkinter as tk
import database as db
import utility

# <--Фреймы-->
from frames.authorization_frame import AuthFrame
from frames.entry_frame import EntryFrame
from frames.registration_frame import RegistrationFrame
from frames.users_frame import UserFrame
from frames.machinist_Frame import MachinistFrame
from frames.cashier_frame import CashierFrame

from tkinter import messagebox

class FrameHandler:
    def __init__(self, root_window, database):
        self.root = root_window
        self.showed_frame = ""
        self.database = database
        self.title_dict = {
            "AuthFrame": "Железнодорожный вокзал",
            "EntryFrame": "Войти",
            "RegistrationFrame": "Регистрация",
            "UserFrame": "Пользователь",
            "MachinistFrame": "Машинист",
            "CashierFrame": "Кассир"
        }

        self.showed_frame = AuthFrame(root_window, self)
        self.showed_frame.create_widgets(self)



        # Сменить фрейм по имени
    def switch_to_frame(self, frame_name_show):
        self.showed_frame.destroy()
        frame_class = globals()[frame_name_show]
        self.showed_frame = frame_class(self.root, self)
        self.showed_frame.create_widgets(self)
        self.change_title(self.title_dict[frame_name_show])

    def change_title(self, title):
        self.root.title(title)

#   < ---------------------------КОМАНДЫ----------------------------->



    def click_back_to_main_from_account(self):
        self.answer = messagebox.askyesno(
            title="Подтверждение",
            message="Вы уверены?")
        if self.answer:
            self.switch_to_frame("AuthFrame")


    def click_registration_submit(self):
        login = self.showed_frame.registration_field_login.get()
        password = self.showed_frame.registration_field_password.get()
        password_proof = self.showed_frame.registration_field_password_proof.get()

        code = utility.check_login_and_password_for_register(login, password, password_proof)
        if code == 100:
            result = self.database.user_registration(login, password)
            if result == True:
                messagebox.showinfo("Уведомление", "Вы успешно зарегистрировались")
                self.switch_to_frame("AuthFrame")
            else:
                messagebox.showerror("Предупреждение", "Такой логин уже существует")
        else:
            messagebox.showerror("Ошибка", utility.errorcodes_descriptions[code])

    # По нажатию на кнопку Войти
    def click_entry_submit(self):
        # Получаем из полей ввода данные
        login = self.showed_frame.entry_field_login.get()
        password = self.showed_frame.entry_field_password.get()

        # Просим базу данных чекнуть есть ли такая запись о пользователе.
        result = self.database.check_login(login, password)

        if result == 101:
            self.switch_to_frame("UserFrame")
            self.showed_frame.user_main_window_label_info.configure(
                text="Добро пожаловать, " + login + "\n" + "Вы вошли в систему как администратор")
        elif result == 102:
            self.switch_to_frame("UserFrame")
            self.showed_frame.user_main_window_label_info.configure(
                text="Добро пожаловать, " + login + "\n" + "Вы вошли в систему как пассажир")
        elif result == 103:
            self.switch_to_frame("CashierFrame")
            self.showed_frame.cashier_main_window_label_info.configure(
                text="Добро пожаловать, " + login + "\n" + "Вы вошли в систему как кассир")
        elif result == 104:
            self.switch_to_frame("MachinistFrame")
            self.showed_frame.machinist_main_window_label_info.configure(
                text="Добро пожаловать, " + login + "\n" + "Вы вошли в систему как машинист")
        else:
            messagebox.showerror("Ошибка!", "Такого пользователя не существует или пароль неверный")


class MainWindow():
    def __init__ (self):
        self.window = tk.CTk()
        self.window.title('Железнодорожный вокзал')
        self.window.geometry("600x500")
        self.window.resizable(True, True)

        self.database = db.DataBase("users.db")

        self.frame_handler = FrameHandler(self.window, self.database) # Создаём диспетчера фреймов описанного выше
        self.window.mainloop()

