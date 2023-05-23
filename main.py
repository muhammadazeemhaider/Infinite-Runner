import pygame
from pygame.locals import *
from BackgroundScreen import Background

pygame.init()

screen_width, screen_height = 1150, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Infinite Runner: Phew Phew")

clock = pygame.time.Clock()

background_image = pygame.image.load("background.jpg")
background_rect = background_image.get_rect()
background_x = 0

BackGround = Background(background_image, [0, 0])

game_is_running = True

while game_is_running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            game_is_running = False

    background_x -= 3

    if background_x <= -background_rect.width:
        background_x = 0

    screen.fill((0, 0, 0))
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + background_rect.width, 0))

    pygame.display.flip()

pygame.quit()
