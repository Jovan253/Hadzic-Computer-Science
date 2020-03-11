### SRC - This is good code, but the sun is moving too
### quickly. This is because the dimensions of the
### screen are small comapared to the velocity.
### You need to create a larger virtual world and then
### shrink to fit the screen.

import pygame

# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My Window")
# -- Exit game flag set to false
game_over = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

x_pos = 30
y_pos = 235

x_dir = 1
y_dir = -1
x_speed = 10
y_speed = 10
gravity = 10
# -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event
    # -- Game logic goes after this comment

    if x_pos > 640 or y_pos > 480:
        x_pos = 30
        y_pos = 235
    else:
        x_pos = x_pos + x_dir * x_speed
        y_pos = y_pos + y_dir * y_speed
        x_pos = x_pos + 1
#        y_pos = 20 + ((x_pos - 320) ** 2)
        print(x_pos, y_pos)    
    
    # -- Screen background is BLACK
    screen.fill(BLACK)
    
    # -- Draw here
    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.circle(screen, YELLOW, (x_pos,y_pos),40,0)
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # -- The clock ticks over
    clock.tick(60)
    
#End While - End of game loop
pygame.quit()     
     
