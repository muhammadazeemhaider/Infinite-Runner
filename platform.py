import pygame
import os
from pygame.locals import *
from random import randrange

class Platform(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.frame = 0
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('images', 'Platform', 'platform' + str(i) + '.png')).convert_alpha()
            self.images.append(img)
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = randrange(screen_width)  # Set the x position randomly
        self.rect.y = randrange(screen_height)  # Set the y position to the bottom of the screen

    def update(self, speed):
        # Move the platform horizontally based on the speed
        self.rect.x -= speed

        # Check if the platform is out of the screen
        if self.rect.right < 0:
            self.kill()
