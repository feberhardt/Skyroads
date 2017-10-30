"""
Created on Thursday Oct 15, 2017
SkyRoads: MiniProject 4

@authors: Felix Eberhardt & Shreya Rangarajan
"""
from threading import Timer
import time
import random
import os, sys, time
import pygame
from pygame.locals import *

if not pygame.font:
    print('Warning, fonts disabled')

running = True
speed = 3

"""
Define all the inital variables
"""
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 0)
red = (255, 0, 0)
green2 = (0, 255, 0)
blue = (0, 0, 255)
brown = (165, 42, 42)

car = "audi_1.png"
barrier = "concrete.png"
road = "road.png"
barrier2 = "concrete.png"

display_width = 1024
display_height = 750

background_size = (display_width, display_height)
car_size = (100, 67)

"""
Initialize the game
"""
pygame.init()
myfont = pygame.font.SysFont("monospace", 40)

screen = pygame.display.set_mode(background_size)
clock = pygame.time.Clock()
timer = pygame.time.get_ticks()
barrier_limit = random.randint(1,4)

background_image = pygame.image.load(road).convert()
player_image = pygame.image.load(car).convert()
player_image_rect = player_image.get_rect()
barriers_list = []
barriers_list_rect = []
barriers_list_pos = []
concrete_img = pygame.image.load(barrier)
barriers_list.append(concrete_img)
barriers_list_pos.append([420,100])
concrete_img_rect = concrete_img.get_rect()
barriers_list_rect.append(concrete_img_rect)

"""
Initialize images
"""
background_colour = (white)
pygame.display.set_caption('Skyroads')
screen.fill(background_colour)
player_image.set_colorkey(white)
concrete_img.set_colorkey(white)
screen.blit(background_image, (0, 0))
pygame.display.flip()

def text_objects(text, font):
    """display a text interface"""
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def return_message(text):
    """Create text output """
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()
def barriers():
    """Randomized barriers falling down at different times """
    global timer
    global barrier_limit
    current_time = pygame.time.get_ticks()
    timer_run = (current_time - timer)/1000

    if timer_run > barrier_limit:
        barrier_x = random.randint(325,575)
        barrier_y = 0
        concrete = pygame.image.load(barrier)
        concrete_rectangle = concrete.get_rect()

        global barriers_list
        barriers_list.append(concrete)
        global barriers_list_rect
        barriers_list_rect.append(concrete_rectangle)
        global barriers_list_pos
        barriers_list_pos.append([barrier_x,barrier_y])
        timer = pygame.time.get_ticks()
        barrier_limit = random.randint(1,4)

def crash():
    """return message if crashed & remove barriers to restart game"""
    return_message('Game Over')

    global barriers_list
    barriers_list = []
    global barriers_list_rect
    barriers_list_rect = []
    global barriers_list_pos
    barriers_list_pos = []
    time.sleep(2)

def score_count(score):
    """count up the score with every loop """
    score += 1
    scoretext = myfont.render("Score {0}".format(score), 1, (red))
    screen.blit(scoretext, (5, 10))

def button(msg,x,y,w,h,ic,ac,action=None):
    """Create a button"""

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
        else:
            pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("monospace",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def game_intro():
    """ Create a startmenu"""
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        largeText = pygame.font.SysFont("monospace",115)
        TextSurf, TextRect = text_objects("Play Skyroads!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        button("Play now!",(display_width/2-150),(display_width/2),300,100,green2,green2,game_loop)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    """
    Run the game
    """

    running = True
    speed = 8
    # Initialize game variables
    score = 0
    x_speed_coord = 0
    y_speed_coord = 0
    concrete_motion = 6
    # Initialize position
    x_car_coord = 420
    y_car_initial = 10
    dx = 10
    dy = 20

    while running:
        for event in pygame.event.get():
        # Check if player quits the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so adjust speed.
                if event.key == pygame.K_LEFT:
                    x_speed_coord = -speed
                elif event.key == pygame.K_RIGHT:
                    x_speed_coord = speed
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
        x_car_coord += x_speed_coord
        if x_car_coord > 555:
            x_car_coord = 555
        if x_car_coord < 320:
            x_car_coord = 320
        y_car_coord = background_size[1]*0.98 - car_size[1]

        screen.blit(background_image, (0, 0))
        screen.blit(player_image, [x_car_coord, y_car_coord])
        player_image_rect.x = x_car_coord
        player_image_rect.y = y_car_coord

        for i in range(0,len(barriers_list_rect)):
            # Update barrier position in the position list
            barriers_list_pos[i][1] = barriers_list_pos[i][1] + concrete_motion
            screen.blit(barriers_list[i], [barriers_list_pos[i][0], barriers_list_pos[i][1]])
            barriers_list_rect[i].x = barriers_list_pos[i][0]
            barriers_list_rect[i].y = barriers_list_pos[i][1]

        # add score
        score += 1
        scoretext = myfont.render("Score {0}".format(score), 1, (red))
        screen.blit(scoretext, (5, 10))

        pygame.display.flip()
        clock.tick(60)
        if x_car_coord <= 0 or x_car_coord >= background_size[0]- car_size[0]:
            crash()

        for i in range(0,len(barriers_list_rect)):
            hit = player_image_rect.colliderect(barriers_list_rect[i])
            if hit:
                crash()
                game_intro()
                break

        barriers()

"""
Run the game
"""
game_intro()
pygame.quit()
quit()
