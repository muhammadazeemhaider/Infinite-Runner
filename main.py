import pygame
from pygame.locals import *
from BackgroundScreen import Background
from runner import runner
from enemy import Goblin
from block import Block
import sys
import random

pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Infinite Runner: Phew Phew")

# Game clock
clock = pygame.time.Clock()

# Load background image
background_image = pygame.image.load("images/background/background.jpg")
background_rect = background_image.get_rect()
background_x = 0

# Background
BackGround = Background(background_image, [0, 0])

# Initialize the runner and the goblin enemy
goblin = Goblin(screen_width, screen_height)
Runner = runner(goblin)
Runner.rect.x = 100
Runner.rect.y = 500

# Player sprite group
player_list = pygame.sprite.Group()
player_list.add(Runner)
steps = 4

# Enemy sprite group
enemy_list = pygame.sprite.Group()
enemy_list.add(goblin)

# --- Initialize the blocks ---
block_list = pygame.sprite.Group()
min_distance = 200  # Minimum distance between platforms

def create_block(x, y):
    block_width = random.randint(100, 300)
    block_height = 30
    block = Block(block_width, block_height)
    block.set_pos(x, y)
    return block

# Create initial set of blocks
x = screen_width
while x < screen_width * 2:
    y = random.randint(screen_height // 2, screen_height - 100)
    block = create_block(x, y)
    block_list.add(block)
    x += block.rect.width + random.randint(min_distance, min_distance * 2)

# Game running flag
game_is_running = True

while game_is_running:
    clock.tick(30)

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            game_is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    game_is_running = False
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

    # Move background
    background_x -= 3
    if background_x <= -background_rect.width:
        background_x = 0

    # --- Block movement and management ---
    for block in block_list:
        block.update()  # Move blocks to the left
        if block.rect.right < 0:
            block_list.remove(block)

    # Add new blocks if needed
    if len(block_list) < 5:
        last_block = max(block_list, key=lambda b: b.rect.right)
        new_x = max(screen_width, last_block.rect.right + min_distance)
        new_y = random.randint(screen_height // 2, screen_height - 100)
        new_block = create_block(new_x, new_y)
        block_list.add(new_block)

    # --- Collision Detection with Blocks ---
    if Runner.movey > 0:  # Only check for collisions when falling
        collided_blocks = pygame.sprite.spritecollide(Runner, block_list, False)
        if collided_blocks:
            lowest_block = min(collided_blocks, key=lambda b: b.rect.top)
            # Ensure the runner is falling onto the top of the block and not hitting its side
            if Runner.rect.bottom <= lowest_block.rect.top + Runner.movey:
                Runner.rect.bottom = lowest_block.rect.top
                Runner.movey = 0  # Stop vertical movement
                Runner.gravity = 0  # Stop applying gravity when on a platform
                Runner.on_block = True  # Indicate that the runner is on a block
            else:
                Runner.on_block = False  # Not on top of the block
        else:
            Runner.on_block = False

    # If the runner is on a block and starts jumping (moving up)
    if Runner.on_block and Runner.movey < 0:  # If jumping off the block
        Runner.on_block = False  # Reset the on_block flag
        Runner.gravity = 0.9  # Reapply gravity when leaving the block

    # --- Collision Detection with Enemies ---
    collided_enemies = pygame.sprite.spritecollide(Runner, enemy_list, False)
    if collided_enemies:
        print("Collision occurred between penguin and goblin")
        game_is_running = False

    # Update player and enemy
    Runner.update()  # Update player position
    goblin.update()  # Update enemy position
    goblin.animate()  # Animate goblin

    # Goblin collision with the runner
    goblin.collide_with_runner(Runner)

    # Goblin attack logic
    if goblin.is_attacking:
        goblin.animate_attack()
    elif goblin.is_running:
        goblin.animate()

    # Goblin movement logic
    if goblin.is_running:
        if goblin.rect.right < 0:  # If the goblin goes off-screen (left side)
            goblin.rect.left = screen_width  # Respawn at the right side of the screen
            goblin.rect.y = screen_height - goblin.rect.height  # Adjust goblin's Y position if needed
        else:
            goblin.rect.x -= 3  # Move the goblin to the left

    # Calculate the distance between the goblin and the runner
    distance = abs(Runner.rect.x - goblin.rect.x)

    # Define the threshold distance to trigger goblin running
    threshold_distance = 300

    # Trigger running sequence if goblin is near runner
    if distance < threshold_distance or goblin.rect.x < Runner.rect.x:
        goblin.is_running = True
    else:
        goblin.is_running = False

    # --- Ensure the Runner stays on screen ---
    if Runner.rect.left < 0:
        Runner.rect.left = 0
    if Runner.rect.right > screen_width:
        Runner.rect.right = screen_width
    if Runner.rect.top < 0:
        Runner.rect.top = 0
    if Runner.rect.bottom > screen_height:
        Runner.rect.bottom = screen_height

    # --- Draw everything ---
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + background_rect.width, 0))
    player_list.draw(screen)
    enemy_list.draw(screen)
    block_list.draw(screen)  # Draw the blocks

    # Update display
    pygame.display.flip()

pygame.quit()