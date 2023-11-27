import pygame, sys
from settings import *
from debug import debug
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption('Pyland')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()


# import pygame
# import time
# import random
# from screen import Screen
# from text import Text
# from level import Level
# from object import Player
#
#
# pygame.init()
#
# clock = pygame.time.Clock()
# start_time = time.time()
# run = True
#
#
# def player_input():
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#             return False
#     return pygame.key.get_pressed()
#
#
# def logic(action_from_input):
#     global run
#     if not action:
#         run = False
#     else:
#         player.movement(action_from_input)
#
#
# def render_game():
#     clock.tick(140)
#     screen.display.fill((0, 0, 0))
#     pygame.draw.rect(screen.display, (255, 255, 255), (550, 50, 840, 750), 5)
#     # screen.display.blit(player.sprite, (player.x, player.y))
#     # text.render(screen, str(player.x), 200, 200)
#     # text.render(screen, str(player.y), 200, 240)
#
#
# screen = Screen(1920, 1080, "Pythland")
# # player = Player('player.png', group, 'graphic/player.png')
# text = Text("Arial", 36)
#
# while run:
#
#     action = player_input()
#     logic(action)
#     render_game()
#
#     pygame.display.update()
#
# pygame.quit()
