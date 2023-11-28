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
        self.obsticle_sprite = pygame.sprite.Group()

        #sprite setup
        self.creat_map()
    def creat_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == '221':
                    Tile((x,y),[self.visible_sprites, self.obsticle_sprite])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obsticle_sprite)


    def run(self):
        #update and draw the game
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # zakladni nastaveni
        super().__init__()
