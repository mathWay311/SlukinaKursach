import customtkinter as tk

class ScrollableFrame(tk.CTkFrame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.CTkCanvas(self, background="#FF7F50")
        scrollbar = tk.CTkScrollbar(self, orientation="vertical", command=canvas.yview)
        self.scrollable_frame = tk.CTkFrame(canvas, bg_color="#FF7F50")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")