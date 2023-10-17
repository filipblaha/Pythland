import pygame
import time
import random

pygame.init()


class Screen:
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.toggle_fullscreen()
        pygame.display.set_caption(self.name)


class Object:
    def __init__(self, png, width, height, x, y, speed):
        self.sprite = pygame.image.load(png)
        self.sprite = pygame.transform.scale(self.sprite, (width, height))
        self.x = x
        self.y = y
        self.speed = speed

    def movement(self, key1, key2, key3, key4):
        if key1:
            self.x -= self.speed
        if key2:
            self.x += self.speed
        if key3:
            self.y -= self.speed
        if key4:
            self.y += self.speed


class Text:
    def __init__(self, font_name, size):
        self.f = pygame.font.SysFont(font_name, size)

    def render(self, text_to_render, x, y):
        text_surf = self.f.render(text_to_render, True, (255, 255, 255))
        screen.display.blit(text_surf, (x - text_surf.get_width() // 2, y - text_surf.get_height() // 2))


screen = Screen(1920, 1080, "Pythland")
player = Object('player.png', 50, 50, 600, 300, 1)
puzzle_window = Object('blank_window.png', 800, 800, 0, 0, 0)
text = Text("Arial", 36)
clock = pygame.time.Clock()

start_time = time.time()
game_over = False
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # FPS
    clock.tick(140)
    keys = pygame.key.get_pressed()

    screen.display.fill((0, 0, 0))
    player.movement(keys[pygame.K_a], keys[pygame.K_d], keys[pygame.K_w], keys[pygame.K_s])
    # screen.display.blit(puzzle_window.sprite, (puzzle_window.x, puzzle_window.y))
    pygame.draw.rect(screen.display, (255, 255, 255), (550, 50, 840, 750), 5)
    screen.display.blit(player.sprite, (player.x, player.y))

    text.render(str(player.x), 200, 200)
    text.render(str(player.y), 200, 240)

    pygame.display.update()

pygame.quit()
