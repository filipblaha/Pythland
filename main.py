import pygame
import time
import random
from object import Object
from screen import Screen
from text import Text

pygame.init()

screen = Screen(1920, 1080, "Pythland")
player = Object('player.png', 50, 50, 600, 300, 1)
puzzle_window = Object('blank_window.png', 800, 800, 0, 0, 0)
text = Text("Arial", 36)

clock = pygame.time.Clock()
start_time = time.time()
run = True

while run:

    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    # logic
    player.movement(pygame.key.get_pressed())

    # render
    clock.tick(140)
    screen.display.fill((0, 0, 0))
    pygame.draw.rect(screen.display, (255, 255, 255), (550, 50, 840, 750), 5)
    screen.display.blit(player.sprite, (player.x, player.y))
    text.render(screen, str(player.x), 200, 200)
    text.render(screen, str(player.y), 200, 240)

    pygame.display.update()

pygame.quit()
