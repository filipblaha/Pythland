import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):

        #get the display surface
        self.display_surface = pygame.display.get_surface()

        #sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprite = pygame.sprite.Group()

        #sprite setup
        self.creat_map()
    def creat_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == '221':
                    Tile((x,y),[self.visible_sprites, self.obstacle_sprite])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprite)


    def run(self):
        #update and draw the game
        self.visible_sprites.custum_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)

class YSortCameraGroup (pygame.sprite.Group):
    def __init__(self):

        # zakladni nastaveni - NASTAVENI KAMERY
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
    def custum_draw(self,player):

        # ziskani offsetu
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(),key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)