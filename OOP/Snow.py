import pygame
import random
import math
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

#create a class
class Snow(pygame.sprite.Sprite):
    #Define the constructor
    def __init__(self, color, width, height, speed):
        #call the constrcutor
        super().__init__()
        #create a sprite and fill it
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        #set sprites position
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0,400)
        #speed of sprite
        self.speed = speed
    #endprocedure

    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y > 640:  #resets snow
            self.rect.y = 0
        #endif
    #endprocedure
#endclass


done = False

#List of snow blocks
snow_group = pygame.sprite.Group()
#List of all sprites
all_sprites_group = pygame.sprite.Group()

#Create Snoeflakes
num_of_flakes = 50
for x in range(num_of_flakes):
    my_snow = Snow(WHITE, 5, 5, 1) 
    snow_group.add(my_snow)
    all_sprites_group.add(my_snow)
#next x    

### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event
            
    # -- Game logic goes after this comment
    all_sprites_group.update()
    
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    all_sprites_group.draw(screen)
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
