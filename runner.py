import pygame
from pygame.locals import *
import os

class runner(pygame.sprite.Sprite):
    
    def __init__(self):
        ALPHA = (0, 255, 0)
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0 # count frames
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images', 'Hero', 'hero' + str(i) + '.png')).convert_alpha()
            # Scale the image to the desired size
            img = pygame.transform.scale(img, (100, 100))  # Adjust the size as needed
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        self.gravity = 0.9  # Gravity value
        self.jump_power = -20  # Initial jump power

    def update(self):
        self.apply_gravity()  # Apply gravity to vertical movement
        self.rect.x += self.movex # move along X
        self.rect.y += self.movey # move along Y

        ani = 4 # animation cycles
        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]
    
    def control(self,x,y):
        self.movex += x 
        self.movey += y

    def apply_gravity(self):
        self.movey += self.gravity

    def jump(self):
        self.movey = self.jump_power