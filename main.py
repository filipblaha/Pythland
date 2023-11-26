import pygame
import time
import random
from object import Object
from screen import Screen
from text import Text

pygame.init()

clock = pygame.time.Clock()
start_time = time.time()
run = True


def player_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return False
    return pygame.key.get_pressed()


def logic(action_from_input):
    global run
    if not action:
        run = False
    else:
        player.movement(action_from_input)


def render_game():
    clock.tick(140)
    screen.display.fill((0, 0, 0))
    pygame.draw.rect(screen.display, (255, 255, 255), (550, 50, 840, 750), 5)
    screen.display.blit(player.sprite, (player.x, player.y))
    text.render(screen, str(player.x), 200, 200)
    text.render(screen, str(player.y), 200, 240)
    

screen = Screen(1920, 1080, "Pythland")
player = Object('player.png', 50, 50, 600, 300, 1)
text = Text("Arial", 36)

while run:

    action = player_input()
    logic(action)
    render_game()

    pygame.display.update()

pygame.quit()
