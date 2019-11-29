import pygame
import random
import math
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen
size = (800,600)
screen = pygame.display.set_mode(size)

#creating invaders
class Invader(pygame.sprite.Sprite):
    #Define the constructor
    def __init__(self, width, height,  x_co, y_co):
        #call the constrcutor
        super().__init__()
        #create a sprite and fill it
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load('invaders.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width,height))
        #set sprites position
        self.rect = self.image.get_rect()
        self.rect.x = x_co
        self.rect.y = y_co
        #speed of sprite
        self.speed = 1
    #endprocedure

    def update(self):        
        self.rect.x = self.rect.x + self.speed
        if self.rect.x % 300 == 0 and self.rect.y % 30 == 0:
            invader_b = Bullet(WHITE, 5, 10 , 0, self.rect.x, self.rect.y)
            invader_bullet_group.add(invader_b)
            all_sprites_group.add(invader_b)
            invader_b.bullet_speed(-1)
       # if self.rect.x % 100 == 0:
        #    self.image = pygame.Surface([40, 40])
         #   self.image = pygame.image.load('invader2.png').convert_alpha()
          #  self.image = pygame.transform.scale(self.image, (40, 40))
        if self.rect.y < 300:
            if self.rect.x > 800:            
                self.speed = self.speed * -1
                self.rect.y = self.rect.y + 20
            elif self.rect.x < 0:
                self.rect.y = self.rect.y + 20
                self.speed = self.speed * -1
        else:
            if self.rect.x > 800:            
                self.speed = self.speed * -1
                self.rect.y = self.rect.y - 20
            elif self.rect.x < 0:
                self.rect.y = self.rect.y - 20
                self.speed = self.speed * -1
        
        #endif
    #endprocedure
#endclass

#creating a player
class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load('space_player.png').convert()
        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = size[0] // 2
        self.rect.y = size[1] - height - 10
        self.speed = 0
        self.lives = 5
        self.bullet_count = 100
        self.score = 0
    #endprocedure
        
    def update(self):
        self.rect.x = self.rect.x + self.speed
    #endprocedure
        
    def player_set_speed(self, val):
        self.speed = val
        if self.rect.x > 790:
            self.rect.x = 790
        elif self.rect.x < 0:
            self.rect.x = 0
        else:
            self.speed = val
        #endif
    #endprocedure
#endclass

#creating Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    #endprcoedure

    def update(self):
        self.rect.y = self.rect.y - self.speed
        
        

    def bullet_speed(self, val):
        self.speed = val
        
        
    


done = False

#keys = pygame.key.get_pressed()
#List of snow blocks
invader_group = pygame.sprite.Group()
#List of all sprites
all_sprites_group = pygame.sprite.Group()

#Create Invaders


invaders_n = 15
space = 0
y = 0
for x in range(invaders_n):
    space = space + 20
    y = y
    if x % 5 == 0:
        space = 0
        y = y + 30        
    else:
        y = y
        space = space + 20
    #endif        
    my_invader = Invader( 40, 40, space, y)
    invader_group.add(my_invader)
    all_sprites_group.add(my_invader)
#next x    

#Create a Player
player_hit_group = pygame.sprite.Group()

player = Player( 40, 40)

all_sprites_group.add(player)

#player_hit_group.add(player)
bullet_group = pygame.sprite.Group()
bullet_hit_group = pygame.sprite.Group()
invader_bullet_group = pygame.sprite.Group()

### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                player.player_set_speed(-3) # speed set to -3
            elif event.key == pygame.K_RIGHT: 
                player.player_set_speed(3) # speed set to 3
            if event.key == pygame.K_SPACE:
                if player.bullet_count > 0:
                    bullet = Bullet(WHITE, 5, 10, 0, size[0]//2, size[1] - height - 10)
                    bullet_group.add(bullet)
                    all_sprites_group.add(bullet)
                    bullet.bullet_speed(2)
                    player.bullet_count = player.bullet_count -1
                else:
                    break
        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0) #speed set to 0
        #End If
    #Next event
            
    # -- Game logic goes after this comment
                
    all_sprites_group.update()
   # player_hit_group = pygame.sprite.groupcollide(invader_bullet_group, player, True, True)

    bullet_hit_group = pygame.sprite.groupcollide(bullet_group, invader_group, True, True) 
        
    for f in player_hit_group:
        player.lives = player.lives - 1

    if player.lives == 0:
        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render("GAME OVER", True, RED)
        screen.blit(text,(400,10))
        done = True

    for i in bullet_hit_group:
        player.score = player.score + 1
        


    if player.score == 15:
        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render("LEVEL 2", True, BLUE)
        screen.blit(text,(400,10))
        invaders_n = 15
        for x in range(invaders_n):
            my_invader = Invader(20, 20, 3, space, y) 
            invader_group.add(my_invader)
            all_sprites_group.add(my_invader)
        
    # -- Screen background is BLACK
    screen.fill (BLACK) 

    # -- Draw here
    all_sprites_group.draw(screen)
    
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("LIVES: " + str(player.lives), True, WHITE)
    screen.blit(text,(0,10))

    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("BULLETS: " + str(player.bullet_count), True, WHITE)
    screen.blit(text,(0,30))

    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("SCORE: " + str(player.score), True, WHITE)
    screen.blit(text,(0,50))
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
