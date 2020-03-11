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

block_x = size[0] // 2
block_y = size[1] // 2
speed = 0
direction = 0

# -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = -1
            elif event.key == pygame.K_DOWN:
                direction = 1
        #End If
        elif event.type == pygame.KEYUP:
            direction = 0
    #Next event
    # -- Game logic goes after this comment
    block_y = block_y + direction * speed
    


    
    # -- Screen background is BLACK
    screen.fill(BLACK)
    
    # -- Draw here
    pygame.draw.rect(screen, RED, ((block_x, block_y),50,50))
    
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # -- The clock ticks over
    clock.tick(60)
    
#End While - End of game loop
pygame.quit()  
