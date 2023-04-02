import pygame
from settings import *
from tile import Tile
from player import Player


class Level:

    def __init__(self):

        # Level setup
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        # only group that draws sprites
        self.visible_sprites = pygame.sprite.Group()
        # only group that updates sprites
        self.active_sprites = pygame.sprite.Group()
        # sprites in this group can collide with the player
        self.collision_sprites = pygame.sprite.Group()

        self.setup_level()


    def setup_level(self):
        for row_index,row in enumerate(LEVEL_MAP):
           for col_index,col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if col == 'X':
                    Tile((x,y),[self.visible_sprites,self.collision_sprites])
                if col == 'P':
                    Player((x,y),[self.visible_sprites,self.active_sprites],self.collision_sprites)

    def run(self):
        # run the entire level
        self.active_sprites.update()
        self.visible_sprites.draw(self.display_surface)