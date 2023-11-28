import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from  support import *

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
        layout = {
                'boundary': import_csv_layout('map/zelda_FloorBlocks.csv')
        }

        for style,layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprite],'invinsible')
        #         if col == '221':
        #             Tile((x,y),[self.visible_sprites, self.obstacle_sprite])
        #         if col == 'p':
        #             self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprite)
        self.player = Player((195, 170), [self.visible_sprites], self.obstacle_sprite)



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

    #     vytvareni podlahy
        self.floor_surf = pygame.image.load('graphic/background.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
    def custum_draw(self,player):

        # ziskani offsetu
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # vykreslovani podlahy
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        for sprite in sorted(self.sprites(),key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)