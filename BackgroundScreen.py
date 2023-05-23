import pygame 
import sys 
from pygame.locals import *

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("background.jpg") # Load the image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0,0)
        