import tkinter as tk
from tkinter import ttk
from pygame_frame import PygameFrame


class AppController:
    def __init__(self, root):
        self.root = root
        self.notebook = ttk.Notebook(root)

        self.tkinter_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.tkinter_frame, text="Náš PyLand")


        self.tkinter_label = tk.Label(self.tkinter_frame, text="text", wraplength=900)
        self.tkinter_label.pack(padx=10, pady=250)  # pady určuje odsazení z vrchní a spodní strany

        # Zobrazení notebooku
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Přidání záložek do notebooku
        self.pygame_frame = PygameFrame(self.notebook, self)
        self.notebook.add(self.pygame_frame, text="Naše PyLand dobrodružství")
