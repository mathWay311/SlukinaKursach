import tkinter as tk
import database as db
from tkinter import ttk
from tkinter import messagebox

import utility


class FrameHandler:

    # Описание всех фреймов ---->

    # Главное меню
    def create_main_frame(self, root_window):
        self.main_window_frame = tk.Frame(root_window) #Создаём фрейм

        self.main_label_welcome = tk.Label(self.main_window_frame, text="Добро пожаловать!", font=("Arial Bold", 20)) # Создаём лэйбел, первым параметром указываем какому фрейму принадлежит
        self.main_label_welcome.place(x=75, y=30) # Помещаем в пространстве, хотя как я понял это необязательно при использовании фреймов
        self.main_label_welcome.pack(padx=30, pady=20) # Упаковываем лэйбел в фрэйм, говорим что отступ о иксу от других элементов - 30, по игреку - 20

        self.main_button_entry = tk.Button(self.main_window_frame, text="Войти", width=40, height=2, fg="#A62A00",
                                           command=self.click_enter)
        self.main_button_entry.place(x=55, y=100)
        self.main_button_entry.pack(padx=30, pady=20)

        self.main_button_registration = tk.Button(self.main_window_frame, text="Регистрация", width=40, height=2, fg="#A62A00",
                                                  command=self.click_registration)
        self.main_button_registration.place(x=55, y=180)
        self.main_button_registration.pack(padx=30, pady=20)

        self.main_window_frame.pack() # Наконец, упаковываем весь фрейм для отображения на экране.

    # Меню входа
    def create_entry_frame(self, root_window):
        self.entry_window_frame = tk.Frame(root_window)  # Создаём фрейм, указывая к какому окну он принадлежит

        self.entry_label_info = tk.Label(self.entry_window_frame, text="Вход", font=("Arial Bold", 20))
        self.entry_label_info.place(x=165, y=45)
        self.entry_label_info.pack()

        self.entry_label_login = tk.Label(self.entry_window_frame, text="Логин:", font=("Arial Bold", 15))
        self.entry_label_login.place(x=65, y=125)
        self.entry_label_login.pack()

        self.entry_field_login = tk.Entry(self.entry_window_frame, width=30)
        self.entry_field_login.place(x=150, y=130)
        self.entry_field_login.pack()

        self.entry_label_password = tk.Label(self.entry_window_frame, text="Пароль:", font=("Arial Bold", 15))
        self.entry_label_password.place(x=60, y=195)
        self.entry_label_password.pack()

        self.entry_field_password = tk.Entry(self.entry_window_frame, width=30, show="*")
        self.entry_field_password.place(x=150, y=200)
        self.entry_field_password.pack()

        self.entry_button_submit = tk.Button(self.entry_window_frame, text="Войти", width=40,
                                                    height=2,
                                                    fg="#A62A00",
                                                    command=self.click_entry_submit)
        self.entry_button_submit.place(x=55, y=100)
        self.entry_button_submit.pack(padx=30, pady=20)

        self.entry_button_back = tk.Button(self.entry_window_frame, text="Назад", width=40, height=2,
                                                  fg="#A62A00",
                                                  command=self.click_back_to_main)
        self.entry_button_back.place(x=55, y=100)
        self.entry_button_back.pack(padx=30, pady=20)

        #self.entry_window_frame.pack()  Здесь ничего паковать не надо, потому  что при входе мы не видим этого фрейма.

    # Меню регистрации
    def create_registration_frame(self, root_window):
        self.registration_window_frame = tk.Frame(root_window)

        self.registration_label_info = tk.Label(self.registration_window_frame, text="Регистрация", font=("Arial Bold", 20))
        self.registration_label_info.place(x=120, y=45)
        self.registration_label_info.pack()

        self.registration_label_login = tk.Label(self.registration_window_frame, text="Логин:", font=("Arial Bold", 15))
        self.registration_label_login.place(x=65, y=125)
        self.registration_label_login.pack()

        self.registration_field_login = ttk.Entry(self.registration_window_frame, width=30)
        self.registration_field_login.place(x=150, y=130)
        self.registration_field_login.pack()

        self.registration_label_password = tk.Label(self.registration_window_frame, text="Пароль:", font=("Arial Bold", 15))
        self.registration_label_password.place(x=60, y=195)
        self.registration_label_password.pack()

        self.registration_field_password = ttk.Entry(self.registration_window_frame, width=30, show="*")
        self.registration_field_password.place(x=150, y=200)
        self.registration_field_password.pack()

        self.registration_label_password_proof = tk.Label(self.registration_window_frame, text="Подтвердите пароль:",
                                                    font=("Arial Bold", 15))
        self.registration_label_password_proof.place(x=60, y=195)
        self.registration_label_password_proof.pack()

        self.registration_field_password_proof = ttk.Entry(self.registration_window_frame, width=30, show="*")
        self.registration_field_password_proof.place(x=150, y=200)
        self.registration_field_password_proof.pack()

        self.registration_button_submit = tk.Button(self.registration_window_frame, text="Зарегистрироваться", width=40, height=2,
                                                  fg="#A62A00",
                                                  command=self.click_registration_submit)
        self.registration_button_submit.place(x=55, y=100)
        self.registration_button_submit.pack(padx=30, pady=20)

        self.registration_button_back = tk.Button(self.registration_window_frame, text="Назад", width=40, height=2, fg="#A62A00",
                                           command=self.click_back_to_main)
        self.registration_button_back.place(x=55, y=100)
        self.registration_button_back.pack(padx=30, pady=20)

    # Основное окно машиниста

    def create_machinist_main_window(self, root_window):
        self.machinist_window_frame = tk.Frame(root_window)

        self.machinist_main_window_label_info = tk.Label(self.machinist_window_frame, font=("Arial Bold", 15))
        self.machinist_main_window_label_info.place(x=120, y=45)
        self.machinist_main_window_label_info.pack()

        self.machinist_timetable_button_submit = tk.Button(self.machinist_window_frame, text="Выйти из системы", width=40,
                                                    height=2,
                                                    fg="#A62A00",
                                                    command=self.click_back_to_main_from_account)
        self.machinist_timetable_button_submit.place(x=55, y=100)
        self.machinist_timetable_button_submit.pack(padx=30, pady=20)


    #Логика нажатия вкладок


    def create_cashier_main_window(self, root_window):

        self.notebook_frame = ttk.Notebook()
        self.notebook_frame.pack(expand=True)

        self.cashier_window_frame = tk.Frame(self.notebook_frame)

        # Первая вкладка
        self.buy_ticket_main_window = tk.Frame(self.notebook_frame)
        self.buy_ticket_main_window.pack(expand=True)

        self.buy_ticket_main_window_label_info = tk.Label(self.buy_ticket_main_window, text="Поздравляю!",
                                                          font=("Arial Bold", 15))
        self.buy_ticket_main_window_label_info.place(x=120, y=150)
        self.buy_ticket_main_window_label_info.pack()

        # Вторая вкладка
        self.return_ticket_main_window = tk.Frame(self.notebook_frame)
        self.return_ticket_main_window.pack(expand=True)

        self.notebook_frame.add(self.buy_ticket_main_window, text="Купить билет")
        self.notebook_frame.add(self.return_ticket_main_window, text="Вернуть билет")

        self.cashier_main_window_label_info = tk.Label(self.cashier_window_frame, font=("Arial Bold", 15))
        self.cashier_main_window_label_info.place(x=120, y=45)
        self.cashier_main_window_label_info.pack()

        self.cashier_timetable_button_submit = tk.Button(self.cashier_window_frame, text="Выйти из системы",
                                                           width=40,
                                                           height=2,
                                                           fg="#A62A00",
                                                           command=self.click_back_to_main_from_account)
        self.cashier_timetable_button_submit.place(x=55, y=100)
        self.cashier_timetable_button_submit.pack(padx=30, pady=20)




    # Основное окно пользователя
    def create_users_main_window(self, root_window):
        self.user_main_window = tk.Frame(root_window)

        self.user_main_window_label_info = tk.Label(self.user_main_window, text="",
                                                font=("Arial Bold", 16))
        self.user_main_window_label_info.place(x=120, y=45)
        self.user_main_window_label_info.pack()

        self.user_timetable_button_submit = tk.Button(self.user_main_window, text="Выйти из системы",
                                                         width=40,
                                                         height=2,
                                                         fg="#A62A00",
                                                         command=self.click_back_to_main_from_account)
        self.user_timetable_button_submit.place(x=55, y=100)
        self.user_timetable_button_submit.pack(padx=30, pady=20)



    # Сменить фрейм по имени
    def switch_to_frame(self, frame_name):
        self.frame_dictionary[self.current_frame_name].pack_forget() # Убираем текущий фрейм
        self.frame_dictionary[frame_name].pack() # Показываем желаемый фрейм
        self.current_frame_name = frame_name


    def __init__(self, root_window, database):
        self.create_main_frame(root_window)
        self.create_entry_frame(root_window)
        self.create_registration_frame(root_window)

        self.create_users_main_window(root_window)
        self.create_machinist_main_window(root_window)
        # self.create_notebook_frame(root_window)
        self.create_cashier_main_window(root_window)

        self.database = database

        self.current_frame_name = "MAIN_FRAME" # Создаём переменную для хранения названия текущего фрейма
        self.frame_dictionary = {"MAIN_FRAME": self.main_window_frame,
                                 "ENTRY_FRAME": self.entry_window_frame,
                                 "REGISTRATION_FRAME": self.registration_window_frame,
                                 "USER_MAIN_FRAME": self.user_main_window,
                                 "MACHINIST_MAIN_FRAME": self.machinist_window_frame,
                                 "CASHIER_MAIN_FRAME": self.cashier_window_frame,
                                 "BUY_TICKET_MAIN_FRAME": self.buy_ticket_main_window} # Создаём структуру данных для удобного обращения к фреймам по строковому имени

    # Логика нажатия кнопок -------->

    def click_registration(self):
        self.switch_to_frame("REGISTRATION_FRAME")

    def click_enter(self):
        self.switch_to_frame("ENTRY_FRAME")

    def click_back_to_main(self):
            self.switch_to_frame("MAIN_FRAME")
            self.registration_field_login.delete(first=0, last=len(self.registration_field_login.get()))
            self.registration_field_password.delete(first=0, last=len(self.registration_field_password.get()))
            self.registration_field_password_proof.delete(first=0, last=len(self.registration_field_password_proof.get()))
            self.entry_field_login.delete(first=0, last=len(self.entry_field_login.get()))
            self.entry_field_password.delete(first=0, last=len(self.entry_field_password.get()))


    def click_back_to_main_from_account(self):
        self.answer = messagebox.askyesno(
            title="Подтверждение",
            message="Вы уверены?")
        if self.answer:
            self.switch_to_frame("MAIN_FRAME")
            self.entry_field_login.delete(first=0, last=len(self.entry_field_login.get()))
            self.entry_field_password.delete(first=0, last=len(self.entry_field_password.get()))


    def click_registration_submit(self):
        login = self.registration_field_login.get()
        password = self.registration_field_password.get()
        password_proof = self.registration_field_password_proof.get()

        code = utility.check_login_and_password_for_register(login, password, password_proof)
        if code == 100:
            result = self.database.user_registration(login, password)
            if result == True:
                messagebox.showinfo("Уведомление", "Вы успешно зарегистрировались")
                self.registration_field_login.delete(first=0, last=len(login))
                self.registration_field_password.delete(first=0, last=len(password))
                self.registration_field_password_proof.delete(first=0, last=len(password_proof))
            else:
                messagebox.showerror("Предупреждение", "Такой логин уже существует")
        else:
            messagebox.showerror("Ошибка", utility.errorcodes_descriptions[code])


    # По нажатию на кнопку Войти
    def click_entry_submit(self):
        # Получаем из полей ввода данные
        login = self.entry_field_login.get()
        password = self.entry_field_password.get()

        # Просим базу данных чекнуть есть ли такая запись о пользователе.
        result = self.database.check_login(login, password)

        if result == 101:
            self.switch_to_frame("USER_MAIN_FRAME")
            self.user_main_window_label_info.config(text = "Добро пожаловать, " + login + "\n" + "Вы вошли в систему как администратор")
        elif result == 102:
            self.switch_to_frame("USER_MAIN_FRAME")
            self.user_main_window_label_info.config(text="Добро пожаловать, " + login + "\n" + "Вы вошли в систему как пассажир")
        elif result == 103:
            self.switch_to_frame("CASHIER_MAIN_FRAME")
            self.cashier_main_window_label_info.config(text="Добро пожаловать, " + login + "\n" + "Вы вошли в систему как кассир")
        elif result == 104:
            self.switch_to_frame("MACHINIST_MAIN_FRAME")
            self.machinist_main_window_label_info.config(text="Добро пожаловать, " + login + "\n" + "Вы вошли в систему как машинист")
        else:
            messagebox.showerror("Ошибка!", "Такого пользователя не существует или пароль неверный")




class MainWindow():
    def __init__ (self):
        self.window = tk.Tk()
        self.window.title('Железнодорожный вокзал')
        self.window.geometry("600x500")
        self.window.resizable(True, True)

        self.database = db.DataBase("users.db")

        self.frame_handler = FrameHandler(self.window, self.database) # Создаём диспетчера фреймов описанного выше
        self.window.mainloop()

