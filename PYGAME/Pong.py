import pygame
import pygame.mixer


# -- Global Constants
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("Disco_Sting.mp3")
pygame.mixer.music.play(-1)

hit_sound = pygame.mixer.Sound("BOUNCE+1.wav")
hit_sound_2 = pygame.mixer.Sound("BOUNCE+1.wav")
fail = pygame.mixer.Sound("Sad_Trombone.wav")
applause = pygame.mixer.Sound("applause_y.wav")

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

text_colour1 = WHITE
text_colour2 = WHITE


# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
# -- Title of new window/screen
pygame.display.set_caption("My Window")
# -- Exit game flag set to false
game_over = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

width = 640
height = 480

r_paddle_x = 600
r_paddle_y = 320
l_paddle_x = 20
l_paddle_y = 320

scoreA = 0
scoreB = 0

player_score = 0

advantage = 0
collision = 0

speed = 5
direction = 0
direction_2 = 0

ball_width = 10
x_val = 320
y_val = 240
x_direction = 5
y_direction = 5

choice = "MENU"

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
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_1:
                choice = "SINGLEPLAYER"
            elif event.key == pygame.K_2:
                choice = "MULTIPLAYER"
            if event.key == pygame.K_m:
                pygame.mixer.init()
                pygame.mixer.music.load("Disco_Sting.mp3")
                pygame.mixer.music.play(1)
        elif event.type == pygame.KEYUP:
                direction = 0
                direction_2 = 0
                pygame.mixer.music.stop
        elif event.type == pygame.MOUSEMOTION:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse = pygame.mouse.get_pos()        
    #Next event
    # -- Game logic goes after this comment



    def background():
        global r_paddle_x
        global r_paddle_y
        global l_paddle_x
        global l_paddle_y, ball_width
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (r_paddle_x, r_paddle_y,20,100))
        pygame.draw.rect(screen, WHITE, (l_paddle_x, l_paddle_y,20,100))
        pygame.draw.circle(screen, WHITE, (x_val, y_val), ball_width, 0)

    def Constrictions():
        global l_paddle_y, l_paddle_x
        global r_paddle_y, r_paddle_x
        
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
    #endprocedure        

    def Ball_movement():
        global y_val
        global x_val
        global y_direction, x_direction
        global l_paddle_y, l_paddle_x
        global r_paddle_y, r_paddle_x
        global collision

        x_val = x_val + x_direction
        y_val = y_val + y_direction
        
        if y_val > 480 or y_val < 0:
            y_direction = y_direction * -1
            x_direction = x_direction
        #endif


        r_paddle_y = r_paddle_y + direction * speed
        l_paddle_y = l_paddle_y + direction_2 * speed



        if (x_val +10 >= r_paddle_x and y_val in range(r_paddle_y, r_paddle_y + 100)):
            pygame.mixer.Sound.play(hit_sound)
            if y_direction < 0 or x_direction < 0:
                y_direction = y_direction -1
                x_direction = (x_direction + 1) * -1 
            else:    
                x_direction = (x_direction + 1) * -1 
                y_direction = y_direction + 1
        #endif
            
        if  (x_val - 10 <= l_paddle_x +20 and y_val in range(l_paddle_y, l_paddle_y + 100)):
            if y_direction < 0 or x_direction < 0:
                y_direction = y_direction 
                x_direction = (x_direction ) * -1  
            else:
                x_direction = (x_direction + 1) * -1
                y_direction = y_direction + 1
            pygame.mixer.Sound.play(hit_sound)
            collision = collision + 1
        #endif
    #endprocedure        

    def high_score():
        score_f = open("high_score.txt", "rt")
        high_score = int(score_f.read())
        score_f.close()
        return high_score
    #endprocedure    

    def new_high_score():
        score_f = open("high_score.txt", "wt")
        score_f.write(str(player_score))
        score_f.close()
    #endprocedure    

################################MENU####################################

    def Menu():
        global width
        global x_val, x_direction
        global y_val, y_direction
        global r_paddle_x
        global r_paddle_y
        global l_paddle_x
        global l_paddle_y, ball_width

        background()

        font = pygame.font.Font("freesansbold.ttf", 115)
        text = font.render("PONG", True, BLUE)
        TextRect = text.get_rect()
        TextRect.center = (width//2, 200)
        screen.blit(text, TextRect)
        pygame.display.flip()

        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render("SINGLEPLAYER", True, text_colour1)
        TextRect1 = text.get_rect()
        TextRect1.center = (width//2, 300)
        screen.blit(text, TextRect1)
        pygame.display.flip()

        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render("MULTIPLAYER", True, text_colour2)
        TextRect2 = text.get_rect()
        TextRect2.center = (width//2, 400)
        screen.blit(text, TextRect2)
        pygame.display.flip()   
        
        mouse = pygame.mouse.get_pos()


        if x_val < 0:
            x_val = 320
            y_val = 240
            x_direction = 5
            y_direction = 5
        #endif     

        if x_val > 640:
            x_val = 320
            y_val = 240
            x_direction = 5
            y_direction = 5
        #endif    

        x_val = x_val + x_direction
        y_val = y_val + y_direction
        
        if y_val > 480 or y_val < 0:
            y_direction = y_direction * -1
            x_direction = x_direction
        #endif


        r_paddle_y = r_paddle_y + direction * speed
        l_paddle_y = l_paddle_y + direction_2 * speed



        if (x_val +10 >= r_paddle_x and y_val in range(r_paddle_y, r_paddle_y + 100)):

                x_direction = (x_direction) * -1 
                y_direction = y_direction 
        #endif
            
        if  (x_val - 10 <= l_paddle_x +20 and y_val in range(l_paddle_y, l_paddle_y + 100)):
            x_direction = x_direction * -1
            y_direction = y_direction
        #endif 
    
        if y_val < l_paddle_y:
            l_paddle_y = y_val
        elif y_val > l_paddle_y:
            l_paddle_y = y_val

        if y_val < r_paddle_y:
            r_paddle_y = y_val
        elif y_val > r_paddle_y:
            r_paddle_y = y_val - 10

        Constrictions()
             
   #endprocedure          

################################CHOICE####################################

    if choice == "MENU":
        Menu()
    elif choice == "SINGLEPLAYER" or TextRect1.collidepoint(mouse):    
        text_colour1 = YELLOW
        Singleplayer()
    elif choice == "MULTIPLAYER":
        text_colour2 = YELLOW
        Multiplayer()
    #endif    

################################SINGLEPLAYER####################################
    def Singleplayer():
        pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
        pygame.mixer.music.stop()
        background()
        
        global player_score, high_score
        global x_val, x_direction
        global y_val, y_direction
        global r_paddle_x
        global r_paddle_y
        global l_paddle_x
        global l_paddle_y
        global width, height
        global collision, advantage


        if x_val < 0:
            x_val = 320
            y_val = 240
            player_score += 1
            x_direction = 2
            y_direction = 2
        #endif     


        Ball_movement()

        if collision == 5:
            advantage = 4
        elif collision == 7:
            advantage = 3

        if y_val < l_paddle_y:
            l_paddle_y = y_val - advantage
        elif y_val > l_paddle_y:
            l_paddle_y = y_val


        Constrictions()   



        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render(str(player_score), True, WHITE)
        screen.blit(text, (320,10))

          
        if x_val > 640:
            high_score = high_score()
            if player_score > high_score:
                pygame.mixer.Sound.play(applause)
                new_high_score()
                font = pygame.font.Font("freesansbold.ttf", 74)
                text = font.render("NEW HIGH SCORE", True, BLUE)
                center = (100,(height/2))
                screen.blit(text, center)
                pygame.display.flip
                pygame.time.wait(5000)
            else:    
                pygame.mixer.Sound.play(fail)
                font = pygame.font.Font("freesansbold.ttf", 74)
                text = font.render("GAME OVER...", True, RED)
                center = (100,(height/2))
                screen.blit(text, center)
                pygame.display.flip()
                pygame.time.wait(5000)
            pygame.quit()
            #endif
        #endif
    #endprocedure        

################################MULTIPLAYER####################################
            
    def Multiplayer():
        pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
        background()
        pygame.mixer.music.stop()
        
        global x_direction, y_direction
        global scoreA, scoreB
        global x_val
        global y_val
        global r_paddle_x
        global r_paddle_y
        global l_paddle_x
        global l_paddle_y

        if x_val > 640:
            x_val = 320
            y_val = 240
            scoreA = scoreA + 1
            x_direction = 3
            y_direction = 3                  
    #endif

        if x_val < 0:
           x_val = 320
           y_val = 240
           scoreB = scoreB + 1
           x_direction = 3
           y_direction = 3


        Ball_movement()
                
        Constrictions()

        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render(str(scoreB), True, WHITE)
        screen.blit(text, (400, 10))

        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render(str(scoreA), True, WHITE)
        screen.blit(text, (200, 10))

        if scoreB == 3:
            pygame.mixer.Sound.play(applause)
            font = pygame.font.Font("freesansbold.ttf", 50)
            text = font.render("Right Wins", True, BLUE)
            screen.blit(text, (320, 240))
            pygame.display.flip()
        elif scoreA == 3:
            pygame.mixer.Sound.play(applause)
            font = pygame.font.Font("freesansbold.ttf", 50)
            text = font.render("Left Wins", True, BLUE)
            screen.blit(text, (220, 240))
            pygame.display.flip()
            
    #endprocedure
            
    # -- flip display to reveal new position of objects
    pygame.display.update()

    #endwhile    
            
    # -- The clock ticks over
    clock.tick(60)
    
#End While - End of game loop
pygame.quit()  
