import os, sys
import pygame
from pygame.locals import *

if not pygame.font:
    print('Warning, fonts disabled')

"""
Define all the inital variables
"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

car = "audi_1.png"
barrier = "concrete.png"
road = "road.png"

background_size = (1024, 750)
car_size = (150, 100)

"""
Initialize the game
"""
pygame.init()
myfont = pygame.font.SysFont("monospace", 40)

screen = pygame.display.set_mode(background_size)
clock = pygame.time.Clock()
background_image = pygame.image.load(road).convert()
player_image = pygame.image.load(car).convert()
concrete_img = pygame.image.load(barrier).convert()

"""
Initialize images
"""
background_colour = (WHITE)
pygame.display.set_caption('Skyroads')
screen.fill(background_colour)
player_image.set_colorkey(WHITE)
concrete_img.set_colorkey(WHITE)
screen.blit(background_image, (0, 0))
pygame.display.flip()
running = True
speed = 3

"""
Initialize game variables
"""
score = 0
x_speed_coord = 0
y_speed_coord = 0
concrete_motion = 0

"""
Initialize position
"""
x_car_initial = 420
y_car_initial = 10
x_concrete_initial = 420
y_concrete_intial = 100
dx = 10
dy = 20


"""
Run the game
"""
while running:
    concrete_motion += 5
    for event in pygame.event.get():
        # Check if player quits the game
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

    # Move the car and barriers according to the speed vector.
    x_car_coord = x_car_initial + x_speed_coord
    y_car_coord = background_size[1]*0.98 - car_size[1]
    x_concrete_coord = x_concrete_initial
    y_concrete_coord = y_concrete_intial + concrete_motion

    screen.blit(background_image, (0, 0))
    screen.blit(player_image, [x_car_coord, y_car_coord])
    screen.blit(concrete_img, [x_concrete_coord, y_concrete_coord])

    # add score
    score += 1
    scoretext = myfont.render("Score {0}".format(score), 1, (RED))
    screen.blit(scoretext, (5, 10))

    pygame.display.flip()
    clock.tick(60)
    pygame.mouse.set_visible(0)
    if x_car_coord <= 0 or x_car_coord >= background_size[0]- car_size[0]:
        running = False
