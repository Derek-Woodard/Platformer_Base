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
        self.visible_sprites = CameraGroup()
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
                    self.player = Player((x,y),[self.visible_sprites,self.active_sprites],self.collision_sprites)

    def run(self):
        # run the entire level
        self.active_sprites.update()
        self.visible_sprites.custom_draw(self.player)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100,300)

        # player centered camera setup
        # self.half_w = self.display_surface.get_size()[0] //2
        # self.half_h = self.display_surface.get_size()[1] //2

        # camera box
        

    def custom_draw(self,player):

        # get player offset for centered camera
        self.offset.x = player.rect.centerx - self.half_w
        self.offset.y = player.rect.centery - self.half_h

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)