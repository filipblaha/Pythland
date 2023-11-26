import pygame


class Player:
    def __init__(self, png, width, height, x, y, speed):
        self.sprite = pygame.image.load(png)
        self.sprite = pygame.transform.scale(self.sprite, (width, height))
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.previous_rect = self.rect

    def movement(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def update(self, second_object):
        if not second_object.rect.contains(self.rect):
            self.rect = self.previous_rect

        self.previous_rect = self.rect.copy()
