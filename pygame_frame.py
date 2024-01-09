import tkinter as tk
from tkinter import ttk
from GameOverworld import Game


class PygameFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.init_ui()
        self.collision = False


    def init_ui(self):
        self.canvas = tk.Canvas(self, width=950, height=500)
        self.canvas.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.text_widget = tk.Text(self)
        self.text_widget.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.text_widget.config(state=tk.DISABLED)

        with open('zadanix.txt', 'r') as zadani:
            zadani_cislox = zadani.read()

        self.tkinter_label = tk.Label(self, text=zadani_cislox)
        self.tkinter_label.grid(row=2, column=0, sticky="nsew")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.pack(fill=tk.BOTH, expand=True)
        self.player_x, self.player_y = 200, 150
        self.player_speed = 5
        self.goal_x, self.goal_y = 200, 200
        self.update_canvas()

    def update_canvas(self):
        game = Game()
        game.run()



    def save_text(self):
        text_to_save = self.pygame_frame.text_widget.get("1.0", tk.END)  # Získání textu z widgetu
        with open("saved_text.txt", "w") as file:  # Otevření souboru pro zápis
            file.write(text_to_save)  # Uložení textu do souboru

