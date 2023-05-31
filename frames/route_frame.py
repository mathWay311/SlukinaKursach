import customtkinter as tk
from base_frame import BaseFrame

from frames.scrollable_frame import *

class ShowRoute(BaseFrame):

    def create_widgets(self, controller):
        self.main_window_label_info = tk.CTkLabel(self, text="Рейсы", font=("Arial Bold", 24))
        self.main_window_label_info.pack(padx=20, pady=5)

        self.content_panel = ScrollableFrame(self)
        self.content_panel.pack(fill=tk.BOTH)

        #self.controller.populate_panel_with_content("train")

        self.exit_submit = tk.CTkButton(self, text="В главное меню",
                                                                 fg_color="#FF6347",
                                                                 width=100,
                                                                 height=40,
                                                                 font=("Arial Bold", 15),
                                                                 command=lambda: controller.click_back_to_main_menu_admin())

        self.exit_submit.pack(side = tk.LEFT, padx = 30, pady = 10)

        self.add_route = tk.CTkButton(self, text="Создать рейс",
                                                                 fg_color="#FF6347",
                                                                 width=100,
                                                                 height=40,
                                                                 font=("Arial Bold", 15),
                                                                 command=lambda: controller.switch_to_frame("AddNewRoute"))
        self.add_route.pack(side = tk.RIGHT, padx = 30, pady = 10)
        self.pack()
