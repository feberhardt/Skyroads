import os, sys
import pygame
from pygame.locals import *

if not pygame.font:
    print('Warning, fonts disabled')

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# initializing
pygame.init()
screen = pygame.display.set_mode((1024, 771))
clock = pygame.time.Clock()
background_image = pygame.image.load("apocalypse red sky.jpg").convert()
# track = pygame.image.load("apocalypse red sky.jpg").convert()
player_image = pygame.image.load("audi_1.png").convert()

background_colour = (WHITE)

pygame.display.set_caption('Skyroads')

screen.fill(background_colour)
player_image.set_colorkey(WHITE)

screen.blit(background_image, (0, 0))
pygame.display.flip()
running = True
# player_position = 0

x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

    # Speed in pixels per frame
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
            # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
        # --- Game Logic
        # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, [x_coord, y_coord])
    pygame.display.flip()
    clock.tick(60)
    pygame.mouse.set_visible(0)
