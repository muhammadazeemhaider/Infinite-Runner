import pygame
from pygame.locals import *
from BackgroundScreen import Background
from runner import runner

pygame.init()

screen_width, screen_height = 1150, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Infinite Runner: Phew Phew")

clock = pygame.time.Clock()

sprite_sheet_image = pygame.image.load("maincharacter.jpg")
background_image = pygame.image.load("background.jpg")
background_rect = background_image.get_rect()
background_x = 0

BackGround = Background(background_image, [0, 0])
Runner = runner()

frame_width = 64
frame_height = 64

for x in range(0, sprite_sheet_image.get_width(), frame_width):
    frame = sprite_sheet_image.subsurface(pygame.Rect(x, 0, frame_width, frame_height))
    Runner.frames.append(frame)

game_is_running = True

while game_is_running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            game_is_running = False

    background_x -= 3

    if background_x <= -background_rect.width:
        background_x = 0

    runner.update()

    screen.fill((0, 0, 0))
    screen.blit(background_image, (background_x, 0))
    screen.blit(Runner.image, Runner.rect)
    screen.blit(background_image, (background_x + background_rect.width, 0))

    pygame.display.flip()

pygame.quit()
