import pygame 
import sys 
from pygame.locals import *

class runner(pygame.sprite.Sprite):
    frames = [] 
        
    def __init__(self):
        super().__init__()
        self.currentframe = 0
        self.animationstate = "running"
        self.image = runner.frames[self.currentframe]
        self.rect = self.image.get_rect()
        self.rect.left = 0  # Starting position of the character
        self.rect.top = 600 // 2 # Starting position of the character and 600 because that is the screen height

    def update(self):
        if self.animationstate == "running":
            self.currentframe += 1
            if self.currentframe >= len(runner.frames):
                self.currentframe = 0

        self.image = runner.frames[self.current_frame]


