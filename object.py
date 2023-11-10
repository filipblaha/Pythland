import pygame
from screen import Screen

class Object:
    def __init__(self, png, width, height, x, y, speed):
        self.sprite = pygame.image.load(png)
        self.sprite = pygame.transform.scale(self.sprite, (width, height))
        self.x = x
        self.y = y
        self.speed = speed

    def movement(self, keys):
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed

