import pygame 
import sys 
from pygame.locals import *

class enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/goblinHead.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

    # def update():

