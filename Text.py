import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, font_name, size, *groups):
        super().__init__(*groups)
        self.f = pygame.font.SysFont(font_name, size)

    def render(self, render_to, text_to_render, x, y):
        text_surf = self.f.render(text_to_render, True, (255, 255, 255))
        render_to.display.blit(text_surf, (x - text_surf.get_width() // 2, y - text_surf.get_height() // 2))
