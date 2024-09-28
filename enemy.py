import pygame
import os

class Goblin(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.idle_images = []
        self.run_images = []
        self.attack_images = []
        self.frame = 0

        # Load idle images
        for i in range(3):  # Adjust the range based on the number of idle images
            img_idle = pygame.image.load(os.path.join('images', 'goblinidle', 'goblinidle' + str(i) + '.png')).convert_alpha()
            self.idle_images.append(pygame.transform.flip(img_idle, True, False))  # Flipping the image horizontally

        # Load run images
        for i in range(4):  # Adjust the range based on the number of run images
            img_run = pygame.image.load(os.path.join('images', 'goblinrun', 'goblinrun' + str(i) + '.png')).convert_alpha()
            self.run_images.append(pygame.transform.flip(img_run, True, False))  # Flipping the image horizontally

        # Load attack images
        for i in range(7):  # Adjust the range based on the number of attack images
            img_attack = pygame.image.load(os.path.join('images', 'goblinattack', 'goblinattack' + str(i) + '.png')).convert_alpha()
            self.attack_images.append(pygame.transform.flip(img_attack, True, False))  # Flipping the image horizontally

        self.image = self.idle_images[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = screen_width - self.rect.width  # Set the x position to the right side of the screen
        self.rect.y = screen_height - self.rect.height  # Set the y position to the bottom of the screen
        self.is_running = False
        self.is_attacking = False
        self.attack_cooldown = 0  # Cooldown timer for attacks
        self.attack_cooldown_duration = 1000  # Adjust as needed (in milliseconds)

    def update(self):
        if self.is_running:
            # Move the Goblin towards the main character
            if self.rect.x > 0:
                self.rect.x -= 5

        if self.is_attacking:
            # Implement the logic for attacking the main character
            if pygame.time.get_ticks() - self.attack_cooldown >= self.attack_cooldown_duration:
                self.attack_cooldown = pygame.time.get_ticks()
                # Add your attack code here

    def animate(self):
        if not self.is_running and not self.is_attacking:
            # Animate the Goblin with idle images
            self.frame = int(pygame.time.get_ticks() * 0.005) % len(self.idle_images)  # Calculate the current frame index
            self.image = self.idle_images[self.frame]
        elif self.is_running:
            # Animate the Goblin with running images
            self.frame = int(pygame.time.get_ticks() * 0.005) % len(self.run_images)  # Calculate the current frame index
            self.image = self.run_images[self.frame]
        elif self.is_attacking:
            # Animate the Goblin with attacking images
            self.frame = int(pygame.time.get_ticks() * 0.005) % len(self.attack_images)  # Calculate the current frame index
            self.image = self.attack_images[self.frame]

    def attack(self):
        self.is_attacking = True
        self.attack_cooldown = pygame.time.get_ticks()

    def animate_attack(self):
        self.frame = int(pygame.time.get_ticks() * 0.005) % len(self.attack_images)
        self.image = self.attack_images[self.frame]

    def collide_with_runner(self, runner):
        if pygame.sprite.collide_rect(self, runner):
            # Collision occurred between goblin and runner
            self.is_running = False  # Stop the goblin from running
            self.is_attacking = True  # Start the goblin's attack animation
        else:
            self.is_attacking = False  # Stop the goblin's attack animation