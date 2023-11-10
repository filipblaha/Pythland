import pygame


class Screen:
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name
        self.display = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN | pygame.SCALED)
        pygame.display.set_caption(self.name)

    def hranice(self, hrac, border_L, border_R, border_U, border_D):
        if hrac.x < border_L:
            hrac.x = border_L
        elif hrac.x > border_R:
            hrac.x = border_R

        if hrac.y < border_U:
            hrac.y = border_U
        elif hrac.y > border_D:
            hrac.y = border_D

