import pygame
import os
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice



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
                'boundary': import_csv_layout('map/zelda_FloorBlocks.csv'),
                'grass': import_csv_layout('map/zelda_Grass.csv'),
                'object': import_csv_layout('map/zelda_Objects.csv'),
        }
        graphics = {
                'grass': import_folder('map/Grass'),
                'object': import_folder('map/Object')
        }

        for style,layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x, y),[self.obstacle_sprite],'invinsible')

                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x, y),[self.visible_sprites,self.obstacle_sprite],'grass',random_grass_image)

                        if style == 'object':
                            if int(col) == 198:  # Přiřazení obrázku pouze k polím s hodnotou 198
                                image_name = 'TilesetNature_listnaty_strom_1-1.png'
                                image_path = os.path.join('map', 'Object', image_name)
                                surf = pygame.image.load(image_path).convert_alpha()
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprite], 'object', surf)
                            if style == 'object':
                                if int(col) == 199:  # Přiřazení obrázku pouze k polím s hodnotou 199
                                    image_name = 'TilesetNature_listnaty_strom_1-2.png'
                                    image_path = os.path.join('map', 'Object', image_name)
                                    surf = pygame.image.load(image_path).convert_alpha()
                                    Tile((x, y), [self.visible_sprites, self.obstacle_sprite], 'object', surf)
                            if style == 'object':
                                if int(col) == 222:  # Přiřazení obrázku pouze k polím s hodnotou 222
                                    image_name = 'TilesetNature_listnaty_strom_2-1.png'
                                    image_path = os.path.join('map', 'Object', image_name)
                                    surf = pygame.image.load(image_path).convert_alpha()
                                    Tile((x, y), [self.visible_sprites, self.obstacle_sprite], 'object', surf)
                            if style == 'object':
                                if int(col) == 223:  # Přiřazení obrázku pouze k polím s hodnotou 198
                                    image_name = 'TilesetNature_listnaty_strom_2-2.png'
                                    image_path = os.path.join('map', 'Object', image_name)
                                    surf = pygame.image.load(image_path).convert_alpha()
                                    Tile((x, y), [self.visible_sprites, self.obstacle_sprite], 'object', surf)
                            else:
                                # V případě jiné hodnoty než 198 můžete provést jiné akce nebo ignorovat
                                pass

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
        self.zoom_level = 1.0  # Úroveň přiblížení

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