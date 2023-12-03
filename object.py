import pygame

class Object:
    def __init__(self, png, width, height, x, y, speed):
        self.sprite = pygame.image.load(png)
        self.sprite = pygame.transform.scale(self.sprite, (width, height))
        self.x = x
        self.y = y
        self.speed = speed

    def movement(self, direction):
        if direction == "up":
            self.player_y -= 10
        elif direction == "down":
            self.player_y += 10
        elif direction == "left":
            self.player_x -= 10
        elif direction == "right":
            self.player_x += 10

