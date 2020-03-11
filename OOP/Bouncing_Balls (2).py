import pygame
import random
# -- Global Constants

# -- Colours
BLACK = (0,0,0)

WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
L_BLUE = (102,255,255)
PURPLE = (102,0,102)
ORANGE = (255,28,0)
GREEN = (0,255,0)

col = (WHITE, BLUE, YELLOW, RED, L_BLUE, PURPLE, ORANGE, GREEN)
spd = (1, 2, 3, 5, 6, 7, 10)
direction = (-1, 1)
BallSize = [5, 10, 15, 20, 25, 30]

#MY Classes

class Ball():
    def __init__(self, x, y, speed, colour, direction_x, direction_y, size):
        self.x = x
        self.y = y
        self.speed = speed
        self.colour = colour
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.size = size
        
    
    def move(self):
        self.x = self.x + (self.direction_x * self.speed)
        self.y = self.y + (self.direction_y * self.speed)
            

        if self.x > size[0] or self.x < 0:
            self.direction_x = self.direction_x * -1
            self.direction_y = self.direction_y
        if self.y > size[1] or self.y < 0:
            self.direction_x = self.direction_x
            self.direction_y = self.direction_y * -1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction_x = self.direction_x * - 1
        if keys[pygame.K_DOWN]:
            if self.size == 5:
                self.size = self.size
            else:
                self.size = self.size - 1
        if keys[pygame.K_UP]:
            if self.size == 30:
                self.size = self.size
            else:
                self.size = self.size + 1
            
            

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)
        
        
    
        

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My First Flipbook")

num = random.randint(1,20)
blocks = []
game_over = False
for i in range(0, int(num)):
    speed_val = spd[random.randint(0,len(spd) - 1)]
    colour_val = col[random.randint(0,len(col) - 1)]
    dir_x = direction[random.randint(0,len(direction) - 1)]
    dir_y = direction[random.randint(0,len(direction) - 1)]
    sz = BallSize[random.randint(0,len(BallSize) - 1)]
    x_val = random.randint(0,640)
    y_val = random.randint(0,480)
    ball = Ball(x_val, y_val, speed_val, colour_val, dir_x, dir_y, sz)
    blocks.append(ball)             
#next

game_over = False
### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
        
    #Next event

            
    # -- Game logic goes after this comment

    for block in blocks:
        block.move()
    
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
   # pygame.draw.rect(screen, WHITE, (size[0]//2, 0, 10, size[1]))
   # pygame.draw.rect(screen, WHITE, (0, size[1]//2, size[0], 10))

    for block in blocks:
        block.draw()


    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
