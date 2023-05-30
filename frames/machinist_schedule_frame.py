import customtkinter as tk
from base_frame import BaseFrame

from frames.scrollable_frame import *

class ShowSchedule(BaseFrame):

    def create_widgets(self, controller):
        self.main_window_label_info = tk.CTkLabel(self, text="Ваши рейсы", font=("Arial Bold", 24))
        self.main_window_label_info.pack(padx=20, pady=5)

        self.content_panel = ScrollableFrame(self)
        self.content_panel.pack(fill=tk.BOTH)

        self.controller.show_routes_for_machinist()

        self.exit_submit = tk.CTkButton(self, text="В главное меню",
                                                                 fg_color="#FF6347",
                                                                 font=("Arial Bold", 15),
                                                                 command=lambda: controller.click_back_to_main_menu_machinist())

        self.exit_submit.pack(side = tk.LEFT, padx = 30, pady = 10)


        self.pack()
