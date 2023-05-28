import customtkinter as tk
import database as db
import routebase as rb
import buyersbase as bb
import use_BD as bd
import utility
from models import *



# <--Фреймы-->


# <--РОЛИ-->
from frames.machinist_frame import *
from frames.cashier_frame import *
from frames.admin_frame import AdminFrame
from frames.users_frame import UserFrame
# <--РОЛИ-->

from frames.authorization_frame import AuthFrame
from frames.entry_frame import EntryFrame
from frames.registration_frame import RegistrationFrame


from frames.buy_ticket_frame import BuyTicket
from frames.return_ticket_frame import ReturnTicket

from frames.add_new_route_frame import AddNewRoute
from frames.add_new_train_frame import AddNewTrain

from frames.scrollable_frame import ScrollableFrame

from tkinter import messagebox

class FrameHandler:
    def __init__(self, root_window, database, routebase, buyersbase):
        self.bd = bd.DB()
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
            "MachinistRegistrationFrame": "Регистрация машиниста",
            "CashierRegistrationFrame": "Регистрация машиниста",
            "CashierFrame": "Кассир",
            "AdminFrame": "Администратор",
            "BuyTicket": "Покупка билета",
            "ReturnTicket": "Возврат билета кассиром",
            "AddNewRoute": "Добавление нового рейса",
            "AddNewTrain": "Добавление нового поезда"
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

    def delete_by_id(self, table, id):
        result = messagebox.askokcancel("Вы уверены?", "Удалённые данные будут потеряны безвозвратно")
        if result:
            self.bd.delete_by_id(table, id)
            #self.refresh()

# <-- Клик "В главное меню" для каждой роли -->

    def click_back_to_main_menu_cashier(self):
        self.switch_to_frame("CashierFrame")
        self.showed_frame.cashier_main_window_label_info.configure(
            text="Добро пожаловать, " + self.login_entry + "\n" + "Вы вошли в систему как кассир")

    def click_back_to_main_menu_user(self):
        self.switch_to_frame("UserFrame")
        self.showed_frame.user_main_window_label_info.configure(
            text="Добро пожаловать, " + self.login_entry + "\n" + "Вы вошли в систему как пассажир")

    def click_back_to_main_menu_admin(self):
        self.switch_to_frame("AdminFrame")
        self.showed_frame.admin_main_window_label_info.configure(
            text="Добро пожаловать, " + self.login_entry + "\n" + "Вы вошли в систему как администратор")


    def click_back_to_main_menu_machinist(self):
        self.switch_to_frame("MachinistFrame")
        self.showed_frame.machinist_main_window_label_info.configure(
            text="Добро пожаловать, " + self.login_entry + "\n" + "Вы вошли в систему как машинист")

# <------------>

    def click_back_to_main_from_account(self):
        if self.message_to_confirm_transition():
            self.switch_to_frame("AuthFrame")

    def add_new_route(self):
        _data = self.showed_frame.add_route_main_window_entry_data.get()
        _city_beg = self.showed_frame.add_route_main_window_entry_city_beg.get()
        _city_end = self.showed_frame.add_route_main_window_entry_city_end.get()
        _name_train = self.showed_frame.add_route_main_window_entry_name_train.get()

        code = utility.check_route_for_register(_city_beg, _city_end)

        if code == 100:
            result = self.bd.add_new_route("route", _data + ";" + _city_beg + ";" + _city_end + ";" + _name_train)
            if result == True:
                messagebox.showinfo("Уведомление", "Успешно")
            else:
                messagebox.showerror("Ошибка", "Ошибка записи")
        else:
            messagebox.showerror("Ошибка", utility.errorcodes_descriptions[code])

    def add_new_train(self):


    def populate_panel_with_content(self, content_name):
        """
        Заполнить поле для контента обьектами из базы

        Args:
            content_name:
                Название контента для заполнения в формате "table", то есть то же имя, что и у файла таблицы БД
        """
        self.current_content = content_name
        models = self.bd.get_all_from(content_name)
        self.showed_frame.content_panel.destroy()
        self.showed_frame.content_panel = ScrollableFrame(self.showed_frame)
        scrollbar = tk.CTkScrollbar

        for model in models:
            if content_name == "machinist":
                dir = MachinistModel(model, self, self.showed_frame.content_panel.scrollable_frame)

        self.showed_frame.content_panel.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)



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
        login_ = self.showed_frame.registration_field_login.get()
        password_ = self.showed_frame.registration_field_password.get()
        password_proof_ = self.showed_frame.registration_field_password_proof.get()

        code = utility.check_login_and_password_for_register(login_, password_, password_proof_)
        if code == 100:
            result = self.database.registration(login_, password_, "cashier")
            if result == True:
                messagebox.showinfo("Уведомление", "Кассир зарегистрирован")
                self.switch_to_frame("AdminFrame")
            else:
                messagebox.showerror("Предупреждение", "Такое имя(логин) уже зарегистрировано")
        else:
            messagebox.showerror("Ошибка", utility.errorcodes_descriptions[code])


    def click_registration_for_machinist(self):
        login_ = self.showed_frame.registration_field_login.get()
        password_ = self.showed_frame.registration_field_password.get()
        password_proof_ = self.showed_frame.registration_field_password_proof.get()
        code = utility.check_login_and_password_for_register(login_, password_, password_proof_)
        if code == 100:
            result = self.database.registration(login_, password_, "machinist")
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
        self.login_entry = self.showed_frame.entry_field_login.get()
        password = self.showed_frame.entry_field_password.get()

        # Просим базу данных чекнуть есть ли такая запись о пользователе.
        result = self.database.check_login(self.login_entry, password)

        if result == 101:
            self.click_back_to_main_menu_admin()
        elif result == 102:
            self.click_back_to_main_menu_user()
        elif result == 103:
            self.click_back_to_main_menu_cashier()
        elif result == 104:
            self.click_back_to_main_menu_machinist()
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


   # def populate_panel_with_content(self, content_name):
      #  if content_name == "route":
        #    self.current_content = "route"
         #   lines = self.bd.get_all_from("route")

          #  self.showed_frame.content_panel.destroy()
           # self.showed_frame.content_panel = ScrollableFrame(self.showed_frame)
           # scrollbar = tk.CTkScrollbar

           # for i in range(len(lines)):
            #    line = lines[i].split(";")
            #    dir = Direction(line, self, self.showed_frame.content_panel.scrollable_frame, line[0])

           # self.showed_frame.content_panel.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)


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

