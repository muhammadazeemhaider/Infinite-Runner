'''
This file contains logic for platforms that will appear 
in the game with a variable length and height.
'''

import pygame
import random

class Block(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.platform_image = pygame.image.load("images/Platform/platform0.png").convert_alpha()
        self.update_image()

    def update_image(self):
        self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        for x in range(0, self.width, self.platform_image.get_width()):
            self.image.blit(self.platform_image, (x, 0))

    def update(self):
        self.rect.x -= 3

    def reset_pos(self, screen_width, screen_height):
        self.rect.y = random.randrange(screen_height // 2, screen_height - 100)
        self.rect.x = screen_width + random.randint(100, 300)

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_size(self, width, height):
        self.width = width
        self.height = height
        self.update_image()
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
