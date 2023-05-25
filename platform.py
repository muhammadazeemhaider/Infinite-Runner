import pygame
import os
from pygame.locals import *
from random import randint

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        self.images = []
