import math
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QScreen



def check_collision(player, prekazka, reset_x, reset_y):
    distance = math.sqrt((player.x - prekazka.x)**2 + (player.y - prekazka.y)**2)

    if distance <= 30:
        player.x = reset_x
        player.y = reset_y
