import customtkinter as tk
import database as db
import routebase as rb
import buyersbase as bb
import utility


# <--Фреймы-->
from frames.authorization_frame import AuthFrame
from frames.entry_frame import EntryFrame
from frames.registration_frame import RegistrationFrame
from frames.users_frame import UserFrame
from frames.machinist_frame import MachinistFrame
from frames.cashier_frame import CashierFrame
from frames.admin_frame import AdminFrame
from frames.buy_ticket_frame import BuyTicket
from frames.return_ticket_frame import ReturnTicket

from tkinter import messagebox

class FrameHandler:
    def __init__(self, root_window, database, routebase, buyersbase):
        root_window.config(bg='#FFBDA0')
       # tk.set_default_color_theme("blue")
        self.root = root_window
        self.showed_frame = ""
        self.database = database
        self.routebase = routebase
        self.buyersbase = buyersbase
        self.title_dict = {
            "AuthFrame": "Железнодорожный вокзал",
            "EntryFrame": "Войти",
            "RegistrationFrame": "Регистрация",
            "UserFrame": "Пользователь",
            "MachinistFrame": "Машинист",
            "CashierFrame": "Кассир",
            "AdminFrame": "Администратор",
            "BuyTicket": "Покупка билета",
            "ReturnTicket": "Возврат билета кассиром"
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

    def message_to_confirm_transition(self):
        self.answer = messagebox.askyesno(
            title="Подтверждение",
            message="Вы уверены?")
        return self.answer

    def click_back_to_main_menu_cashier(self):
        if self.message_to_confirm_transition():
            self.switch_to_frame("CashierFrame")

    def click_back_to_main_menu_user(self):
        if self.message_to_confirm_transition():
            self.switch_to_frame("UserFrame")


    def click_back_to_main_from_account(self):
        if self.message_to_confirm_transition():
            self.switch_to_frame("AuthFrame")

    def click_registration_submit(self):
        self.login = self.showed_frame.registration_field_login.get()
        self.password = self.showed_frame.registration_field_password.get()
        self.password_proof = self.showed_frame.registration_field_password_proof.get()

        code = utility.check_login_and_password_for_register(self.login, self.password, self.password_proof)
        if code == 100:
            result = self.database.registration(self.login, self.password, "user")
            if result == True:
                messagebox.showinfo("Уведомление", "Вы успешно зарегистрировались")
                self.switch_to_frame("AuthFrame")
            else:
                messagebox.showerror("Предупреждение", "Такой логин уже существует")
        else:
            messagebox.showerror("Ошибка", utility.errorcodes_descriptions[code])


    def click_registration_for_cashier(self):

        self.registration_label_login.configure(text="ФИО(Логин):")
        self.switch_to_frame("RegistrationFrame")

        code = utility.check_login_and_password_for_register(self.login, self.password, self.password_proof)
        if code == 100:
            result = self.database.registration(self.login, self.password, "cashier")
            if result == True:
                messagebox.showinfo("Уведомление", "Кассир зарегистрирован")
                self.switch_to_frame("AdminFrame")
            else:
                messagebox.showerror("Предупреждение", "Такое имя(логин) уже зарегистрировано")
        else:
            messagebox.showerror("Ошибка", utility.errorcodes_descriptions[code])


    def click_registration_for_machinist(self):

        self.registration_label_login.configure(text="ФИО(Логин):")
        self.switch_to_frame("RegistrationFrame")

        code = utility.check_login_and_password_for_register(self.login, self.password, self.password_proof)
        if code == 100:
            result = self.database.registration(self.login, self.password, "machinist")
            if result == True:
                messagebox.showinfo("Уведомление", "Машинист зарегистрирован")
                self.switch_to_frame("AdminFrame")
            else:
                messagebox.showerror("Предупреждение", "Такое имя(логин) уже зарегистрировано")
        else:
            messagebox.showerror("Ошибка", utility.errorcodes_descriptions[code])



    def click_registration_submit_cashier(self):
        pass


    def click_delete_ticket_submit(self):
        pass



    # По нажатию на кнопку Войти
    def click_entry_submit(self):
        # Получаем из полей ввода данные
        login = self.showed_frame.entry_field_login.get()
        password = self.showed_frame.entry_field_password.get()

        # Просим базу данных чекнуть есть ли такая запись о пользователе.
        result = self.database.check_login(login, password)

        if result == 101:
            self.switch_to_frame("AdminFrame")
            self.showed_frame.admin_main_window_label_info.configure(
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


    def click_buy_ticket_search(self):
        beg_city = self.showed_frame.buy_ticket_main_window_label_city_begin.get()
        end_city = self.showed_frame.buy_ticket_main_window_label_city_end.get()
        result = self.routebase.check_cities_when_buying(beg_city, end_city)
        while result:
            new_listbox = result
            self.showed_frame.list_to_route_buy_ticket.configure(listvariable=new_listbox)


    def click_return_ticket_search_for_cashier(self):
        surname = self.showed_frame.return_ticket_main_window_label_surname.get()
        name = self.showed_frame.return_ticket_main_window_label_name.get()
        patronymic = self.showed_frame.return_ticket_main_window_label_patronymic.get()





class MainWindow():
    def __init__ (self):
        self.window = tk.CTk()
        self.window.title('Железнодорожный вокзал')
        self.window.geometry("600x500")
        self.window.resizable(True, True)

        self.database = db.DataBase("BaseData/users.db")
        self.routebase = rb.RouteBase("BaseData/route.db")
        self.buyersbase = bb.BuyersBase("BaseData/buyers.db")

        self.frame_handler = FrameHandler(self.window, self.database, self.routebase, self.buyersbase) # Создаём диспетчера фреймов описанного выше
        self.window.mainloop()

