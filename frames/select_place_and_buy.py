from tkinter import messagebox

import customtkinter as tk
from base_frame import BaseFrame
from tkinter import *


class SelectPlaceAndBuy(BaseFrame):

    def create_widgets(self, controller):


        self.label_info = tk.CTkLabel(self, text="Покупка билета", font=("Arial Bold", 14))
        self.label_info.pack(padx=10)

        self.label_name = tk.CTkLabel(self, text="Имя", font=("Arial Bold", 15))
        self.label_name.pack()

        self.name_entry = tk.CTkEntry(self, width=150)
        self.name_entry.pack()

        self.label_surname = tk.CTkLabel(self, text="Фамилия", font=("Arial Bold", 15))
        self.label_surname.pack()

        self.surname_entry = tk.CTkEntry(self, width=150)
        self.surname_entry.pack()

        self.label_patronymic = tk.CTkLabel(self, text="Отчество", font=("Arial Bold", 15))
        self.label_patronymic.pack()

        self.patronymic_entry = tk.CTkEntry(self, width=150)
        self.patronymic_entry.pack()

        self.label_seria = tk.CTkLabel(self, text="Серия паспорта", font=("Arial Bold", 15))
        self.label_seria.pack()

        self.seria_entry = tk.CTkEntry(self, width=150)
        self.seria_entry.pack()

        self.label_number = tk.CTkLabel(self, text="Номер паспорта", font=("Arial Bold", 15))
        self.label_number.pack()

        self.number_entry = tk.CTkEntry(self, width=150)
        self.number_entry.pack()

        selroute = self.controller.selected_route

        self.label_route = tk.CTkLabel(self, text="Рейс: " + selroute , font=("Arial Bold", 15))
        self.label_route.pack()

        train_ID = self.controller.get_trainID_of_route(selroute)

        avail_wagons = self.controller.get_all_wagons(train_ID)


        avail_wagons_strlist = []
        for wagon in avail_wagons:
            avail_wagons_strlist.append(wagon.number + " " + wagon.type)
        print(avail_wagons_strlist)

        self.label_wagon = tk.CTkLabel(self, text="Номер вагона", font=("Arial Bold", 15))
        self.label_wagon.pack()

        self.wagon_select = tk.CTkComboBox(self, width=300, values=avail_wagons_strlist)
        self.wagon_select.set("")
        self.wagon_select.configure(command=self.view_places)
        self.wagon_select.pack()

        self.label_place = tk.CTkLabel(self, text="Номер места", font=("Arial Bold", 15))
        self.label_place.pack()



        self.place_select = tk.CTkComboBox(self, width=300, values=[])
        self.place_select.set("")

        self.place_select.pack()


        self.button_submit_next = tk.CTkButton(self, text="Купить билет", font=("Arial Bold", 15), fg_color="#FF7F50",
                                               command= lambda : self.buy_ticket())
        self.button_submit_next.pack(padx=8, pady=10)

        self.timetable_button_submit = tk.CTkButton(self, text="Вернуться назад", fg_color="#FF6347",
                                                               font=("Arial Bold", 15), command= lambda : self.controller.switch_to_frame("BuyTicket"))
        self.timetable_button_submit.pack(padx=100, pady=10)


        self.pack()

    def view_places(self, choice):
        seats = self.controller.get_avail_seats(choice.split(" ")[0])
        print(seats)
        self.place_select.set("")
        self.place_select.configure(values=seats)

    def buy_ticket(self):
        if len(self.wagon_select.get().strip()) == 0 or len(self.place_select.get().strip()) == 0 or \
                len(self.name_entry.get().strip()) == 0 or len(self.surname_entry.get().strip()) == 0 or len(self.patronymic_entry.get().strip()) == 0:
            messagebox.showerror("Ошибка", "Поле не может быть пустым")
            return
        self.controller.add_new_ticket()