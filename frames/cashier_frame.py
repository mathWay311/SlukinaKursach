from base_frame import BaseFrame


class CashierFrame(BaseFrame):
    def create_widgets(self, controller):
        '''


        self.notebook_frame = tk.CTkNotebook()
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
        '''