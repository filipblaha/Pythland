import pygame
from appcontroller import AppController
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    root.title("PythLand")
    app_controller = AppController(root)


    def on_key_press(event):
        global button_press_time  # aktualizace aby to valilo
        if event.keysym in ["w", "s", "a", "d"]:
            app_controller.pygame_frame.move_player(event.keysym)
            button_press_time = pygame.time.get_ticks()  # Pohyb hráče
        elif event.keysym in ["a", "c", "p"]:
            app_controller.save_text()  # Uložení pozice
        elif event.keysym == "r":
            current_time = pygame.time.get_ticks()  # Reset hráče
            if current_time - button_press_time > 3000:
                app_controller.pygame_frame.player_x, app_controller.pygame_frame.player_y = 200, 150

    root.bind("<Key>", on_key_press)

    root.mainloop()