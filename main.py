import pygame
from pygame.locals import *
from BackgroundScreen import Background
from runner import runner
from enemy import Goblin
import sys
from pygame.sprite import spritecollide

pygame.init()

screen_width, screen_height = 1150, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Infinite Runner: Phew Phew")

clock = pygame.time.Clock()

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

enemy_list = pygame.sprite.Group()  # Create a group for enemies
goblin = Goblin(screen_width, screen_height)
enemy_list.add(goblin)  # Add the goblin to the enemy group

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

    Runner.update()  # update player position
    goblin.update()  # update enemy position
    goblin.animate()  # animate goblin

    # Check for collision between the goblin and the main character
    goblin.collide_with_runner(Runner)

    if goblin.rect.right < 0:  # Respawn goblin when it goes off the screen
        goblin.rect.left = screen_width
        goblin.rect.y = screen_height - goblin.rect.height

    # Calculate the distance between the goblin and the main character
    distance = abs(Runner.rect.x - goblin.rect.x)

    # Define the threshold distance to trigger the running sequence
    threshold_distance = 400  # Adjust as needed

    if distance < threshold_distance:
        # Trigger the running sequence
        goblin.is_running = True
    else:
        # Reset the goblin's state
        goblin.is_running = False

    if pygame.sprite.spritecollideany(Runner, enemy_list):
        # Trigger the attacking sequence
        goblin.is_attacking = True
    else:
        # Reset the goblin's state
        goblin.is_attacking = False

    if Runner.rect.left < 0:
        Runner.rect.left = 0
    if Runner.rect.right > screen_width:
        Runner.rect.right = screen_width
    if Runner.rect.top < 0:
        Runner.rect.top = 0
    if Runner.rect.bottom > screen_height:
        Runner.rect.bottom = screen_height

    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + background_rect.width, 0))
    player_list.draw(screen)
    enemy_list.draw(screen)

    pygame.display.flip()

pygame.quit()
