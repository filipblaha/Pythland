import pygame
import sys

pygame.init()

# Nastavení okna Pygame
sirka, vyska = 800, 600
okno = pygame.display.set_mode((sirka, vyska))

# Barvy
bila = (255, 255, 255)
cerna = (0, 0, 0)

# Font pro textový vstup
font = pygame.font.Font(None, 36)

# Proměnná pro ukládání textového vstupu
text = ""


def player_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode


while True:


    # Vykreslení pozadí
    okno.fill(bila)

    # Vykreslení textu
    text_surface = font.render(text, True, cerna)
    sirka_textu, vyska_textu = text_surface.get_size()
    okno.blit(text_surface, ((sirka - sirka_textu) // 2, (vyska - vyska_textu) // 2))

    # Aktualizace okna
    pygame.display.flip()