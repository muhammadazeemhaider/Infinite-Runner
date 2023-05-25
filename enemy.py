import pygame
import os
from pygame.locals import *
from random import randint

class Goblin(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.frame = 0
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('images', 'goblinidle', 'goblinidle' + str(i) + '.png')).convert_alpha()
            self.images.append(pygame.transform.flip(img, True, False))  # Flipping the image horizontally
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = screen_width - self.rect.width  # Set the x position to the right side of the screen
        self.rect.y = screen_height - self.rect.height  # Set the y position to the bottom of the screen

    def update(self):
        # Randomly move the Goblin horizontally
        self.rect.x += randint(-3, 0)

        # Check if the Goblin is out of the screen
        if self.rect.right < 0:
            self.rect.left = pygame.display.get_surface().get_width()
        elif self.rect.left > pygame.display.get_surface().get_width():
            self.rect.right = 0

    def animate(self):
        # Animate the Goblin by cycling through the images
        self.frame = int(pygame.time.get_ticks() * 0.005) % len(self.images)  # Calculate the current frame index
        self.image = self.images[self.frame]
