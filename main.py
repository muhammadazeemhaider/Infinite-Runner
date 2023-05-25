import pygame
from pygame.locals import *
from BackgroundScreen import Background
from runner import runner
from enemy import Goblin 
import sys

pygame.init()

screen_width, screen_height = 1150, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Infinite Runner: Phew Phew")

clock = pygame.time.Clock()

# sprite_sheet_image = pygame.image.load("maincharacter.jpg")
background_image = pygame.image.load("images/background/background.jpg")
background_rect = background_image.get_rect()
background_x = 0

BackGround = Background(background_image, [0, 0])

Runner = runner()  # spawn player
Runner.rect.x = 100  # go to x
Runner.rect.y = 500  # go to y
player_list = pygame.sprite.Group()
player_list.add(Runner)
steps = 7

# Enemy = enemy(500, 300) #spawns enemy
# Enemy_list = pygame.sprite.Group() # creates enemy group
# Enemy_list.add(Enemy) # adds enemy to the group

game_is_running = True

while game_is_running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            game_is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                Runner.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                Runner.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                Runner.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                Runner.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                Runner.control(-steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                Runner.control(0, steps * 2)

    background_x -= 3

    if background_x <= -background_rect.width:
        background_x = 0

    Runner.update() # update player position

    """
        The code below is to prevent the player from going off the screen
    """
    if Runner.rect.left < 0:
        Runner.rect.left = 0
    if Runner.rect.right > screen_width:
        Runner.rect.right = screen_width
    if Runner.rect.top < 0:
        Runner.rect.top = 0
    if Runner.rect.bottom > screen_height:
        Runner.rect.bottom = screen_height

    # screen.fill((0, 0, 0))
    screen.blit(background_image, (background_x, 0)) # adds the initial background image
    screen.blit(background_image, (background_x + background_rect.width, 0)) # blit the second image right after the first one making it look like an infinite never ending screen
    player_list.draw(screen) # Draw the player on the screen
    # Enemy_list.draw(screen) # Draw the enemy on the screen

    pygame.display.flip()

pygame.quit()