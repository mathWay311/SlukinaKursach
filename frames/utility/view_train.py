import customtkinter as tk

from models import TrainModel

class TrainView():
    def __init__(self, train_model : TrainModel, controller, parent_frame):
        self.model = train_model


        dir_rect = tk.CTkFrame(parent_frame, height=50, width=385)


        label_name = tk.CTkLabel(dir_rect, text=self.model.name, font=("Roboto", 16))



        edit_button = tk.CTkButton(dir_rect, text="Удалить", font=("Roboto", 16), text_color="#FFFFFF", fg_color="#FF7F50", command=lambda :controller.click_delete_train_submit(self.model))
        edit_button.place(relheight = 1, relx = 0.6)
        label_name.place(relheight=1, x=30)

        dir_rect.pack(fill=tk.X, pady=1)