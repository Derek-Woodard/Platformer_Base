import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        # automatically assign the group used to these sprites
        super().__init__(groups)
       
        self.image = pygame.surface((TILE_SIZE,TILE_SIZE))
        self.image.fill(TILE_COLOR)
        self.rect = self.image_get_rect(topleft = pos)
