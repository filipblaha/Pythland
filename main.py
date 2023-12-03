import tkinter as tk
from tkinter import ttk
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
        self.canvas.delete("all")

        # Vykreslení hráče
        self.canvas.create_rectangle(
            self.player_x - 10, self.player_y - 10,
            self.player_x + 10, self.player_y + 10,
            fill="blue"
        )

        # Vykreslení cíle
        self.canvas.create_rectangle(
            self.goal_x - 5, self.goal_y - 5,
            self.goal_x + 5, self.goal_y + 5,
            fill="red"
        )

        self.check_goal()

        self.after(30, self.update_canvas)

    def move_player(self, direction):
        if self.collision:
            return
        if direction == "w":
            self.player_y -= self.player_speed
        elif direction == "s":
            self.player_y += self.player_speed
        elif direction == "a":
            self.player_x -= self.player_speed
        elif direction == "d":
            self.player_x += self.player_speed

    def check_goal(self):
        if (
            self.player_x >= self.goal_x - 10 and
            self.player_x <= self.goal_x + 10 and
            self.player_y >= self.goal_y - 10 and
            self.player_y <= self.goal_y + 10
        ):

            self.text_widget.config(state=tk.NORMAL)
            self.collision = True

        else:

            self.text_widget.config(state=tk.DISABLED)
            self.collision = False

class AppController:
    def __init__(self, root):
        self.root = root
        self.notebook = ttk.Notebook(root)

        self.tkinter_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.tkinter_frame, text="Our PyLand")

        # Label a text pro Tkinter frame
        self.tkinter_label = tk.Label(self.tkinter_frame, text="Tady bude zadání")
        self.tkinter_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        # Zobrazení notebooku
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Přidání záložek do notebooku
        self.pygame_frame = PygameFrame(self.notebook, self)
        self.notebook.add(self.pygame_frame, text="PyLand Adventure")


    def save_text(self):
        text_to_save = self.pygame_frame.text_widget.get("1.0", tk.END)  # Získání textu z widgetu
        with open("saved_text.txt", "w") as file:  # Otevření souboru pro zápis
            file.write(text_to_save)  # Uložení textu do souboru

if __name__ == "__main__":
    root = tk.Tk()
    root.title("PythLand")
    app_controller = AppController(root)

    def on_key_press(event):
        if event.keysym in ["w", "s", "a", "d"]:  # pohyb hráče
            app_controller.pygame_frame.move_player(event.keysym)
        elif event.keysym in ["c", "p"]:  # uložení txt souboru napsaného kódu (jako commit a push (haha))
            app_controller.save_text()
        elif event.keysym == "r":  # reset polohy hráče
            app_controller.pygame_frame.player_x, app_controller.pygame_frame.player_y = 200, 150

    root.bind("<Key>", on_key_press)
    root.mainloop()
