import pygame


class Screen(pygame.sprite.Sprite):
    def __init__(self, width, height, name, *groups):
        super().__init__(*groups)
        self.width = width
        self.height = height
        self.name = name
        self.display = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN | pygame.SCALED)
        pygame.display.set_caption(self.name)
