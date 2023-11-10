import subprocess

def check_collision(player_x, player_y, x_prekazka, y_prekazka, player_width, player_height):
    if (
        player_x < x_prekazka + 30
        and player_x + player_width > x_prekazka
        and player_y < y_prekazka + 30
        and player_y + player_height > y_prekazka
    ):
        # Otevření textového dokumentu
        text_file_path = "example.txt"
        try:
            subprocess.run(["open", text_file_path], check=True)
        except Exception as e:
            print(f"Chyba při otevírání textového dokumentu: {e}")


#    gui.check_collision(player_x, player_y, x_prekazka, y_prekazka, player_width, player_height)
