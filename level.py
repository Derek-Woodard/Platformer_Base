import pygame
from settings import *

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

    def run(self):
        # run the entire level
        pass