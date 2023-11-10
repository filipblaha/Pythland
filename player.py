import pygame as pg




class Postava:
    def __init__(self, cesta_k_obrazku, x, y, rychlost):
        self.png = pg.image.load(cesta_k_obrazku)
        self.x = x
        self.y = y
        self.rychlost = rychlost

    def update(self):
        if self.x < 700:
            self.x += 2
        elif self.x == 700:
            self.x = -10