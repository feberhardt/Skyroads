import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

# Setup
pygame.init()

# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key

        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
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

    # --- Drawing Code

    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    draw_stick_figure(screen, x_coord, y_coord)


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()


# Create an 800x600 sized screen
# screen = pygame.display.set_mode([800, 600])
# # This sets the name of the window
# pygame.display.set_caption('CMSC 150 is cool')
# # clock = pygame.time.Clock()

# Set positions of graphics
# background_position = [0, 0]
# # Load and set up graphics.
# background_image = pygame.image.load("apocalypse red sky.jpg").convert()
# # player_image = pygame.image.load("playerShip1_orange.png").convert()
# player_image.set_colorkey(BLACK)
# done = False
# while not done:
#     # for event in pygame.event.get():
#     #     if event.type == pygame.QUIT:
#     #         done = True
#     #     elif event.type == pygame.MOUSEBUTTONDOWN:
#     #         click_sound.play()
#     # Copy image to screen:
#     screen.blit(background_image, background_position)
#     # Get the current mouse position. This returns the position
#     # as a list of two numbers.
#     # player_position = pygame.mouse.get_pos()
#     x = player_position[0]
#     y = player_position[1]
#     # Copy image to screen:
#     screen.blit(player_image, [x, y])
#     pygame.display.flip()
#     clock.tick(60)
#
# pygame.quit()
# pygame.mouse.set_visible(0)
#
# background = pygame.Surface(screen.get_size())
# background = background.convert()
# background.fill((250, 250, 250))
#





# # Put Text On The Background, Centered
# if pygame.font:
#     font = pygame.font.Font(None, 36)
#     text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
#     textpos = text.get_rect(centerx=background.get_width()/2)
#     background.blit(text, textpos)
#
# # Display The Background While Setup Finishes
# screen.blit(background, (0, 0))
# pygame.display.flip()
#
# # prepare game objects
# whiff_sound = load_sound('whiff.wav')
# punch_sound = load_sound('punch.wav')
# chimp = Chimp()
# fist = Fist()
# allsprites = pygame.sprite.RenderPlain((fist, chimp))
# clock = pygame.time.Clock()
#
# # Main loop
# while 1:
#     clock.tick(60)
#
# # handle all input events
# for event in pygame.event.get():
#     if event.type == QUIT:
#         return
#     elif event.type == KEYDOWN and event.key == K_ESCAPE:
#         return
#     elif event.type == MOUSEBUTTONDOWN:
#         if fist.punch(chimp):
#             punch_sound.play() #punch
#             chimp.punched()
#         else:
#             whiff_sound.play() #miss
#     elif event.type == MOUSEBUTTONUP:
#         fist.unpunch()
#
# allsprites.update()
#
# # draw all objects
# screen.blit(background, (0, 0))
# allsprites.draw(screen)
# pygame.display.flip()
def get_init():
    """return true if the pygame module has been initialized."""
    # return "sys" in sys.modules
    pass

def load_image(name, colorkey=None):
    """Loading Resources"""
#     fullname = os.path.join('data', name)
#     try:
#         image = pygame.image.load(fullname)
#     except(pygame.error, message):
#         print('Cannot load image:', name)
#         raise(SystemExit, message)
#     image = image.convert()
#     if colorkey is not None:
#         if colorkey is -1:
#             colorkey = image.get_at((0,0))
#         image.set_colorkey(colorkey, RLEACCEL)
#     return image, image.get_rect()
    pass
