import pygame
import sys

from level import Level
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((20, 20), pygame.FULLSCREEN)
        pygame.display.set_caption('Pyland')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.level.toggle_menu()

        self.screen.fill((0, 0, 0))
        self.level.run()
        pygame.display.update()
        self.clock.tick(FPS)
