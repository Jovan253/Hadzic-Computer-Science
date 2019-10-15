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
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
# -- Title of new window/screen
pygame.display.set_caption("My Window")
# -- Exit game flag set to false
game_over = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

r_paddle_x = 600
r_paddle_y = 320
l_paddle_x = 20
l_paddle_y = 320

scoreA = 0
scoreB = 0

speed = 5
direction = 0
direction_2 = 0

ball_width = 10
x_val = 320
y_val = 240
x_direction = 1
y_direction = 1


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
            if event.key == pygame.K_w:
                direction_2 = -1
            elif event.key == pygame.K_s:
                direction_2 = 1
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
        #End If
        elif event.type == pygame.KEYUP:
            direction = 0
            direction_2 = 0
    #Next event
    # -- Game logic goes after this comment

    x_val = x_val + x_direction
    y_val = y_val + y_direction
    
    if x_val > 640:
        x_val = 320
        y_val = 240
        scoreA = scoreA + 1
        x_direction = 1
        y_direction = 1
        
    #endif

    if x_val < 0:
        x_val = 320
        y_val = 240
        scoreB = scoreB + 1
        x_direction = 1
        y_direction = 1
    #endif    
        

    if y_val > 480 or y_val < 0:
        y_direction = y_direction * -1
        x_direction = x_direction
    #endif


    r_paddle_y = r_paddle_y + direction * speed
    l_paddle_y = l_paddle_y + direction_2 * speed



    if (x_val +10 >= r_paddle_x and y_val in range(r_paddle_y, r_paddle_y + 100)):
        if y_direction < 0 or x_direction<0:
            y_direction = y_direction -1
            x_direction = (x_direction + 1) * -1 
        else:    
            x_direction = (x_direction + 1) * -1 
            y_direction = y_direction + 1
        print(x_direction, y_direction)
        print(x_val, r_paddle_x, y_val, r_paddle_y)
    #endif
        
    if  (x_val - 10 <= l_paddle_x +20 and y_val in range(l_paddle_y, l_paddle_y + 100)):
        if y_direction < 0 or x_direction<0:
            y_direction = y_direction 
            x_direction = (x_direction ) * -1  
        else:
            x_direction = (x_direction + 1) * -1
            y_direction = y_direction + 1
        print(x_direction, y_direction)
        print(x_val, l_paddle_x,y_val, l_paddle_y)
    #endif



    if l_paddle_y > 380: 
        l_paddle_y = 380
    #endif    
    if r_paddle_y > 380:
        r_paddle_y = 380
    #endif
    if l_paddle_y < 0:
        l_paddle_y = 0
    #endif
    if r_paddle_y < 0:
        r_paddle_y = 0
    #endif
        
    # -- Screen background is BLACK
    screen.fill(BLACK)    
    
    # -- Draw here
    pygame.draw.rect(screen, WHITE, (r_paddle_x, r_paddle_y,20,100))
    pygame.draw.rect(screen, WHITE, (l_paddle_x, l_paddle_y,20,100))
    pygame.draw.circle(screen, WHITE, (x_val, y_val), ball_width, 0)
    
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render(str(scoreB), True, WHITE)
    screen.blit(text, (400, 10))

    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render(str(scoreA), True, WHITE)
    screen.blit(text, (200, 10))
    
    if scoreB == 3:
        font = pygame.font.Font("freesansbold.ttf", 50)
        text = font.render("Right Wins", True, BLUE)
        screen.blit(text, (320, 240))
        pygame.display.flip()
        pygame.quit()
    elif scoreA == 3:
        font = pygame.font.Font("freesansbold.ttf", 50)
        text = font.render("Left Wins", True, BLUE)
        screen.blit(text, (320, 240))
        pygame.display.flip()
        pygame.quit()
    else:    
    # -- flip display to reveal new position of objects
        pygame.display.flip()
    
    # -- The clock ticks over
    clock.tick(60)
    
#End While - End of game loop
pygame.quit()  
