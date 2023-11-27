import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, png, width, height, x, y, *groups):
        super().__init__(*groups)
        self.sprite = pygame.image.load(png)
        self.sprite = pygame.transform.scale(self.sprite, (width, height))
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
