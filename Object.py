import pygame


class Object:
    def __init__(self, png, width, height, x, y):
        self.sprite = pygame.image.load(png)
        self.sprite = pygame.transform.scale(self.sprite, (width, height))
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
