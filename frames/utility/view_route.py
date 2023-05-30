import customtkinter as tk

from models import RouteModel

class RouteView():
    def __init__(self, train_model : RouteModel, controller, parent_frame):
        self.model = train_model


        dir_rect = tk.CTkFrame(parent_frame, height=50, width=385)


        label_name = tk.CTkLabel(dir_rect, text=self.model.from_ + " - " + self.model.to_ + " " + self.model.dept_time, font=("Roboto", 12))



        edit_button = tk.CTkButton(dir_rect, text="Отменить", font=("Roboto", 16), text_color="#FFFFFF", fg_color="#FF7F50", command=lambda :controller.click_delete_route_submit(self.model))
        edit_button.place(relheight = 1, relx = 0.6)
        label_name.place(relheight=1, x=30)

        dir_rect.pack(fill=tk.X, pady=1)