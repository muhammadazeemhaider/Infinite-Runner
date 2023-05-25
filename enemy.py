import pygame 
import sys 
import os
from pygame.locals import *

class Goblin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1,4):
            img = pygame.image.load(os.path.join('images', 'goblinidle', 'goblinidle' + str(i) + '.png')).convert_alpha()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def update(self):
        


