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

car = "audi_1.png"
barrier = "concrete.png"
# road = "road1.jpg"
# road = "road2.jpg"
road = "road.png"

background_size = (1024, 750)
car_size = (150, 100)
concrete = (200,113)

# initializing
pygame.init()
myfont = pygame.font.SysFont("monospace", 40)

screen = pygame.display.set_mode(background_size)
clock = pygame.time.Clock()
background_image = pygame.image.load(road).convert()
player_image = pygame.image.load(car).convert()
concrete_img = pygame.image.load(barrier).convert()

background_colour = (WHITE)
pygame.display.set_caption('Skyroads')
screen.fill(background_colour)
player_image.set_colorkey(WHITE)
screen.blit(background_image, (0, 0))
pygame.display.flip()
running = True
speed = 3
# Starting variables
score = 0
x_speed_coord = 0
y_speed_coord = 0
x_speed_concrete = 0
y_speed_concrete = 0

# Initial position
x_car_coord = 420
y_car_coord = 10
x_concrete_coord = 420
y_concrete_coord = 1024

#Initial direction
dx = 2
dy = 5

# Speed in pixels per frame
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed_coord = dx + speed
            elif event.key == pygame.K_RIGHT:
                x_speed_coord = abs(dx-speed)
            elif event.key == pygame.K_UP:
                y_speed_coord = dy + speed
            elif event.key == pygame.K_DOWN:
                y_speed_coord = abs(dy-speed)
            # press escape to get out of game
            elif event.key == pygame.K_ESCAPE:
                running = False
            # user leaves key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed_coord = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed_coord = 0
        # --- Game Logic
        # Move the object according to the speed vector.
    x_coord = x_car_coord + x_speed_coord
    # y_coord = y_coord + y_speed
    y_coord = background_size[1]*0.98 - car_size[1]
    #player_image.x = x_coord
    #player_image.y = y_coord

    screen.blit(background_image, (0, 0))
    # print(x_coord, y_coord)
    screen.blit(player_image, [x_coord, y_coord])

    # add score
    score += 1
    scoretext = myfont.render("Score {0}".format(score), 1, (RED))
    screen.blit(scoretext, (5, 10))

    pygame.display.flip()
    clock.tick(60)
    pygame.mouse.set_visible(0)
    if x_coord <= 0 or x_coord >= background_size[0]- car_size[0]:
        running = False
