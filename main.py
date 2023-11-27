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
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button.rect.collidepoint(mouse_x, mouse_y):
                pygame.time.set_timer(pygame.USEREVENT, 500)
        elif event.type == pygame.USEREVENT:
            player.change_animation()
    return pygame.key.get_pressed()


def logic(action_from_input):
    global run
    if not action:
        run = False
    #else:
        #player.movement(action_from_input)


def render_game():
    clock.tick(140)
    screen.display.fill((100, 100, 100))
    screen.display.blit(code.sprite, code.rect)
    screen.display.blit(border.sprite, border.rect)
    screen.display.blit(enemy.sprite, enemy.rect)
    screen.display.blit(button.sprite, button.rect)

    for a in range(player.animation_status):
        hearthd = hearth[a]
        screen.display.blit(hearthd.sprite, hearthd.rect)

    # text.render(screen, str(player.rect.x), 200, 200)
    # text.render(screen, str(player.rect.y), 200, 240)


def update():
    player.update(border)


screen = Screen(1920, 1080, "Pythland")
player = Player('player.png', 50, 50, 800, 300, 1)
border = Object('forest.png', 1180, 980, 700, 50)
enemy = Object('goblin.png', 250, 300, 1200, 600)
code = Object('code.png', 600, 750, 50, 50)
button = Object('check_button.png', 400, 150, 150, 830)

hearth = [None] * 10
for i in range(10):
    hearth[i] = Object('hearth.png', 50, 50, 1050+i*+55, 550)

text = Text("Arial", 36)

while run:
    action = player_input()
    logic(action)
    render_game()
    update()

    pygame.display.update()

pygame.quit()
