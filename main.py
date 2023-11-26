import pygame
import time
from Player import Player
from Screen import Screen
from Text import Text
from Object import Object

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
    screen.display.fill((100, 100, 100))
    screen.display.blit(border.sprite, border.rect)
    screen.display.blit(player.sprite, player.rect)
    text.render(screen, str(player.rect.x), 200, 200)
    text.render(screen, str(player.rect.y), 200, 240)


def update():
    player.update(border)


screen = Screen(1920, 1080, "Pythland")
player = Player('player.png', 50, 50, 800, 300, 1)
border = Object('maze.png', 1180, 980, 700, 50)
text = Text("Arial", 36)

while run:
    action = player_input()
    logic(action)
    render_game()
    update()

    pygame.display.update()

pygame.quit()
