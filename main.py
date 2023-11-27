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

font = pygame.font.Font(None, 36)


def player_input():
    for event in pygame.event.get():
        # user pressing ESC or X (CLOSE APP) to quit
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return False
        # user pressing button to check
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return "BUTTON_PRESSED"
        # the code is right
        elif event.type == pygame.USEREVENT:
            return "ANIMATION"
        # user pressing keys
        elif event.type == pygame.KEYDOWN:
            # pressed ENTER
            if event.key == pygame.K_RETURN:
                return "ENTER"
            # pressed BACKSPACE
            elif event.key == pygame.K_BACKSPACE:
                if text.user_text:
                    return "BACKSPACE"
            # pressed other keys
            else:
                if not text.user_text or event.key != pygame.K_KP_ENTER:
                    text.user_text[-1] += event.unicode
    return pygame.key.get_pressed()


def logic(action_from_input):
    global run
    if not action:
        run = False
    if action == "ENTER":
        text.user_text.append("")
    # pressed BACKSPACE
    elif action == "BACKSPACE":
        if text.user_text:
            text.user_text[-1] = text.user_text[-1][:-1]
    elif action == "BUTTON_PRESSED":
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button.rect.collidepoint(mouse_x, mouse_y):
            pygame.time.set_timer(pygame.USEREVENT, 500)
    elif action == "ANIMATION":
        player.change_animation()


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
    text.render_user_text(screen, 65, 55)
    # text_surface = font.render(text.user_text, True, (255, 255, 255))


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
    hearth[i] = Object('hearth.png', 50, 50, 1050 + i * +55, 550)

text = Text("Arial", 36)

while run:
    action = player_input()
    logic(action)
    render_game()
    update()

    pygame.display.update()

pygame.quit()
