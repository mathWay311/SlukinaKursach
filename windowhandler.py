import customtkinter as tk
import database as db

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

from frames.train_frame import ShowTrain
from frames.route_frame import ShowRoute

from frames.utility.view_train import TrainView
from frames.utility.view_route import RouteView

from frames.select_place_and_buy import SelectPlaceAndBuy
from frames.show_tickets_frame import ShowTicketsFrame

from frames.return_ticket_user_frame import ReturnTicketUser
from frames.machinist_schedule_frame import ShowSchedule

from frames.scrollable_frame import ScrollableFrame

from frames.utility.view_machinist_routes import RouteMachinistView

from tkinter import messagebox

class FrameHandler:
    def __init__(self, root_window, database):
        self.bd = bd.DB()
        root_window.config(bg='#FFBDA0')
       # tk.set_default_color_theme("blue")
        self.root = root_window
        self.showed_frame = ""
        self.database = database

        self.title_dict = {
            "AuthFrame": "Железнодорожный вокзал",
            "EntryFrame": "Войти",
            "RegistrationFrame": "Регистрация",
            "UserFrame": "Пользователь",
            "MachinistFrame": "Машинист",
            "MachinistRegistrationFrame": "Регистрация машиниста",
            "CashierRegistrationFrame": "Регистрация кассира",
            "CashierFrame": "Кассир",
            "AdminFrame": "Администратор",
            "BuyTicket": "Покупка билета",
            "ShowTrain": "Поезда",
            "ShowRoute": "Рейсы",
            "ReturnTicket": "Возврат билета кассиром",
            "AddNewRoute": "Добавление нового рейса",
            "AddNewTrain": "Добавление нового поезда",
            "SelectPlaceAndBuy": "Заполните информацию",
            "ShowTicketsFrame" : "Ваши билеты",
            "ReturnTicketUser" : "Верните ваш билет",
            "ShowSchedule" : "Расписание"
        }

        self.showed_frame = AuthFrame(root_window, self)
        self.showed_frame.create_widgets(self)

        self.login_entry = ""
        self.role = ""


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
        result = messagebox.askyesno("Вы уверены?", "Удалённые данные будут потеряны безвозвратно")
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

    def click_back_to_main_from_account(self):
        if self.message_to_confirm_transition():
            self.switch_to_frame("AuthFrame")

# <------------>



    def add_new_route(self):
        _data = self.showed_frame.entry_data.get()
        _city_beg = self.showed_frame.entry_city_beg.get()
        _city_end = self.showed_frame.entry_city_end.get()
        _name_train = self.showed_frame.entry_name_train.get()
        _name_machinist = self.showed_frame.entry_name_machinist.get()

        code = utility.check_route_for_register(_city_beg, _city_end)

        search = self.bd.search_model("route", "DeptTime", _data)

        if search:
            messagebox.showerror("Ошибка", "Время занято")
            return

        if code == 100:
            result = self.bd.add_new_record("route", _data + ";" + _city_beg + ";" + _city_end + ";" + _name_train + ";" + _name_machinist + ";")
            if result != False:
                messagebox.showinfo("Уведомление", "Успешно")
                self.click_back_to_main_menu_admin()
            else:
                messagebox.showerror("Ошибка", "Ошибка записи")
        else:
            messagebox.showerror("Ошибка", utility.errorcodes_descriptions[code])

    def add_new_train(self):
        _name = self.showed_frame.train_name.get()
        _num_of_wagons_coupe = self.showed_frame.coupe_wagon.get()
        _num_of_wagons_placcart = self.showed_frame.placcart_wagon.get()

        train = TrainModel([0, _name, 0])

        code = utility.check_train(_name)

        if code == 100:

            train_id = self.bd.add_new_record("train", train.db_add_string())
            num_coupe_last = 0
            for i in range(1, int(_num_of_wagons_coupe) + 1):
                coupe_model = WagonModel([0, "Купе", str(i), "", str(train_id)])
                self.bd.add_new_record("wagon", coupe_model.db_add_string())
                num_coupe_last = i
            num_coupe_last += 1
            for i in range(num_coupe_last, num_coupe_last + int(_num_of_wagons_placcart)):
                placcart_model = WagonModel([0, "Плацкарт", str(i), "", str(train_id)])
                self.bd.add_new_record("wagon", placcart_model.db_add_string())

            messagebox.showinfo("Уведомление", "Вы добавили поезд " + _name)
            self.click_back_to_main_menu_admin()
        else:
            messagebox.showerror("Ошибка", utility.errorcodes_descriptions[code])

    def add_new_ticket(self):

        name_ = self.showed_frame.name_entry.get()
        surname_ = self.showed_frame.surname_entry.get()
        patronymic_ = self.showed_frame.patronymic_entry.get()
        serial_ = self.showed_frame.seria_entry.get()
        number_ = self.showed_frame.number_entry.get()
        login_ = self.login_entry
        route_id_ = self.selected_route.split(" ")[0]
        wagon_num_ = self.showed_frame.wagon_select.get().split(" ")[0]
        place_ = self.showed_frame.place_select.get()

        code = utility.check_ticket(name_, surname_, patronymic_, serial_, number_, login_, route_id_, wagon_num_, place_)

        if code == 100:
            result = self.bd.add_new_record("buyers", name_ + ";" + surname_ + ";" +  patronymic_ + ";" +  serial_ + ";" +  number_ + ";" +  login_ + ";" +  route_id_ + ";" +  wagon_num_ + ";" +  place_ + ";")
            if result != False:
                messagebox.showinfo("Уведомление", "Успешно")
                self.switch_to_frame("BuyTicket")
            else:
                messagebox.showerror("Ошибка", "Ошибка записи")
        else:
            messagebox.showerror("Ошибка", utility.errorcodes_descriptions[code])

    def show_tickets_for_current_user(self):
        tickets = self.bd.get_all_from("buyers")
        ticket_model_list = []
        for ticket in tickets:
            if ticket.login == self.login_entry:
                ticket_model_list.append(ticket)

        strings = []
        for ticket in ticket_model_list:
            route = self.bd.search_model("route", "ID", ticket.routeID)
            print(ticket.wagonID)
            wagon = self.bd.search_model("wagon", "Number", ticket.wagonID)
            strings.append(route.dept_time + " " + route.from_ + " - " + route.to_ + " Вагон:" + wagon.type + " Номер " + str(ticket.wagonID) + " Место: " + ticket.place)
        return strings

    def show_routes_for_machinist(self):
        routes = self.bd.get_all_from("route")

        for route in routes:
            if route.machinistName == self.login_entry:
                route = RouteMachinistView(route, self, self.showed_frame.content_panel.scrollable_frame)
        self.showed_frame.content_panel.pack()

    def show_tickets_for_current_user_withIDS(self):
        tickets = self.bd.get_all_from("buyers")
        ticket_model_list = []
        for ticket in tickets:
            if ticket.login == self.login_entry:
                ticket_model_list.append(ticket)

        strings = []
        for ticket in ticket_model_list:
            route = self.bd.search_model("route", "ID", ticket.routeID)
            print(ticket.wagonID)
            wagon = self.bd.search_model("wagon", "Number", ticket.wagonID)
            strings.append(str(ticket.id) + " " + route.dept_time + " " + route.from_ + " - " + route.to_ + " Вагон:" + wagon.type + " Номер " + str(ticket.wagonID) + " Место: " + ticket.place)
        return strings

    def click_away_from_ticket_buy(self):
        if self.role == "user":
            self.click_back_to_main_menu_user()
        elif self.role == "cashier":
            self.click_back_to_main_menu_cashier()

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
            if content_name == "train":
                train = TrainView(model, self, self.showed_frame.content_panel.scrollable_frame)
            if content_name == "route":
                route = RouteView(model, self, self.showed_frame.content_panel.scrollable_frame)


        self.showed_frame.content_panel.pack()

    def show_trains(self):
        self.switch_to_frame("ShowTrain")
        self.populate_panel_with_content("train")
        self.showed_frame.add_train.pack_forget()
        self.showed_frame.exit_submit.pack_forget()
        self.showed_frame.add_train.pack(side = tk.RIGHT, padx = 30, pady = 10)
        self.showed_frame.exit_submit.pack(side = tk.LEFT, padx = 30, pady = 10)

    def show_routes(self):
        self.switch_to_frame("ShowRoute")
        self.populate_panel_with_content("route")
        self.showed_frame.add_route.pack_forget()
        self.showed_frame.exit_submit.pack_forget()
        self.showed_frame.add_route.pack(side = tk.RIGHT, padx = 30, pady = 10)
        self.showed_frame.exit_submit.pack(side = tk.LEFT, padx = 30, pady = 10)

    # <------получить доступные------>

    def get_available_machinists(self) -> list[UserModel]:
        models = self.bd.get_all_from("users")
        output = []
        for model in models:
            if model.role == "machinist":
                output.append(model)
        return output

    def get_available_trains(self) -> list[TrainModel]:
        """
        Получает список доступных поездов. То бишь не isOccupied.
        :return: Список обьектов класса TrainModel с флагом isOccupied == False
        """
        models = self.bd.get_all_from("train")
        output = []
        for model in models:
            if not model.isOccupied:
                output.append(model)
        return output

    def get_all_wagons(self, trainID: int) -> list[WagonModel]:
        """
        Получает список доступных вагонов для покупки билета.
        :param trainID: Айдишник поезда
        :return:
        """
        models = self.bd.get_all_from("wagon")
        output = []
        for model in models:
            if model.trainID == trainID:
                if not(model.seats_string.find("0") == -1):
                    output.append(model)
        return output

    def get_avail_seats(self, wagonName: str) -> list[str]:
        wagon_model = self.bd.search_model("wagon", "Number", wagonName)
        train_id = wagon_model.trainID
        train_name = self.bd.search_model("train", "ID", train_id).name
        route_model =  self.bd.search_model("route", "TrainName", train_name)


        max_places = 0
        if wagon_model.type == "Купе":
            max_places = 10
        if wagon_model.type == "Плацкарт":
            max_places = 20

        list_of_seats = [i for i in range(1, max_places + 1)]

        tickets = self.bd.get_all_from("buyers")
        for ticket in tickets:
            if ticket.routeID == route_model.id:
                if str(ticket.wagonID) == str(wagon_model.number):
                    list_of_seats.remove(int(ticket.place))

        for i in range(len(list_of_seats)):
            list_of_seats[i] = str(list_of_seats[i])
        return list_of_seats



    # <------получить доступные------>

    def get_trainID_of_route(self, route_string: str) -> int:
        """
        По указанной строке рейса находит айдишник поезда
        :param route_string:
        :return: ID (int)
        """
        id = route_string.split(" ")[0]
        train_name = self.bd.search_model("route", "ID", id).trainName
        return self.bd.search_model("train", "Name", train_name).id


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
                self.click_back_to_main_menu_admin()
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
                self.click_back_to_main_menu_admin()
            else:
                messagebox.showerror("Предупреждение", "Такое имя(логин) уже зарегистрировано")
        else:
            messagebox.showerror("Ошибка", utility.errorcodes_descriptions[code])



    def click_delete_train_submit(self, model : TrainModel):
        ans = messagebox.askyesno("Внимание", "Вы уверены?")
        if ans:
            self.bd.delete_train(model)
            self.show_trains()

    def click_delete_route_submit(self, model : RouteModel):
        ans = messagebox.askyesno("Внимание", "Вы уверены?")
        if ans:
            self.bd.delete_route(model)
            if self.role == "machinist":
                self.show_routes_for_machinist()
                self.switch_to_frame("ShowSchedule")
            else:
                self.show_routes()


    def click_entry_submit(self):

        self.login_entry = self.showed_frame.entry_field_login.get()
        password = self.showed_frame.entry_field_password.get()

        result = self.database.check_login(self.login_entry, password)

        if result == 101:
            self.click_back_to_main_menu_admin()
            self.role = "admin"
        elif result == 102:
            self.click_back_to_main_menu_user()
            self.role = "user"
        elif result == 103:
            self.click_back_to_main_menu_cashier()
            self.role = "cashier"
        elif result == 104:
            self.click_back_to_main_menu_machinist()
            self.role = "machinist"
        else:
            messagebox.showerror("Ошибка!", "Такого пользователя не существует или пароль неверный")

    def click_buy_ticket_search(self):
        """
        Вывод в комбобокс найденных по городу началу и городу конца рейсов.
        Поиск реализован через поиск подстроки в строке и работает только если оба условия выполняются.
        Замена на OR обеспечит слишком мягкий поиск. По сути при нахождении города отправления город конечный
        уже не будет ни на что влиять. Короче пусть так остаётся.

        Для поиска НЕОБХОДИМО вводить город начала и город конца (Хотя бы одну букву)

        :return:
        """
        beg_city = self.showed_frame.label_city_begin.get()
        end_city = self.showed_frame.label_city_end.get()

        # ---------------ПОИСК--------------
        result = []
        models = self.bd.get_all_from("route")
        for model in models:
            beg_city_flag = False
            end_city_flag = False
            if beg_city.strip() != "":
                beg_city_flag = (model.from_.find(beg_city ) != -1)
            if end_city.strip() != "":
                end_city_flag = (model.to_.find(end_city ) != -1)
            if beg_city_flag and end_city_flag:
                result.append(model)
        # ----------------------------------

        str_results = []
        for model in result:
            str_results.append(str(model.id) + " " + model.from_ + " - " + model.to_ + " ("+ model.dept_time + ")")

        if len(str_results):
            messagebox.showinfo("Поиск", "По вашему запросу найдено билетов: " + str(len(str_results)))
        else:
            messagebox.showerror("Поиск", "Ничего не найдено")
        self.showed_frame.list_to_route_buy_ticket.configure(values=str_results)

    def select_route_and_proceed(self):
        """
        Выбрать рейс и продолжить в следующее окно выбора места.
        :return:
        """
        self.selected_route = self.showed_frame.list_to_route_buy_ticket.get()
        self.switch_to_frame("SelectPlaceAndBuy")


    def click_return_ticket_search_for_cashier(self) -> list[BuyerModel]:


        surname = self.showed_frame.entry_name.get()
        name = self.showed_frame.entry_surname.get()
        patronymic = self.showed_frame.entry_patronymic.get()

        tickets = self.bd.get_all_from("buyers")

        tickets_to_output = []
        for ticket in tickets:
            if surname == ticket.surname and name == ticket.name and patronymic == ticket.patronymic:
                tickets_to_output.append(ticket)
            print(surname + " " + ticket.surname + " " + name + " " + ticket.name + " " + patronymic + " " + ticket.patronymic)

        list_str = []

        for ticket in tickets_to_output:
            route = self.bd.search_model("route", "ID", str(ticket.routeID))
            list_str.append(str(ticket.id) + " " + ticket.name + " " + ticket.surname + " " + ticket.patronymic + " " + ticket.pass_serial + " " + ticket.pass_number + " " + route.from_ + "-" + route.to_ + " " + route.dept_time)

        self.showed_frame.ticket_list.configure(values = list_str)

        if len(list_str):
            messagebox.showinfo("Найдены билеты", "Найдено " + str(len(list_str)) + " билетов")
        else:
            messagebox.showerror("Ошибка", "Билетов на ФИО не найдено")

    def click_delete_ticket(self):
        id = self.showed_frame.ticket_list.get().split()[0]
        ans = messagebox.askyesno("Вернуть билет", "Вы уверены?")
        if ans:
            self.bd.delete_by_id("buyers", id)
            self.showed_frame.ticket_list.set("")
            if self.role == "cashier":
                self.click_back_to_main_menu_cashier()
            else:
                self.click_back_to_main_menu_user()

class MainWindow():
    def __init__ (self):
        self.window = tk.CTk()
        self.window.title('Железнодорожный вокзал')
        self.window.geometry("600x550")
        self.window.resizable(True, True)

        self.database = db.DataBase("BaseData/users.db")


        self.frame_handler = FrameHandler(self.window, self.database)
        self.window.mainloop()

