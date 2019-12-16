import pygame
import math
import json

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
size = (800,800)
screen = pygame.display.set_mode(size)

class tile(pygame.sprite.Sprite):
# Define the constructor for invader
    def __init__(self, color, width, height, x_ref, y_ref):
# Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, x_ref, y_ref, xspeed, yspeed):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load('L-PAC.png').convert()
        self.image = pygame.transform.scale(self.image, (width,height))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.xspeed = xspeed
        self.yspeed = yspeed
        
    #endprocedure
  #  def player_speed_update(self, val, val2):
       # self.rect.x = self.rect.x + self.xspeed
        #self.rect.y = self.rect.y + self.yspeed
   #     xspeed = val
    #    yspeed = val2
     #   self.rect.x = self.rect.x + self.xspeed
      #  self.rect.y = self.rect.y + self.yspeed
    #endprocedure

    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed

    def vertical(self,val):
        self.yspeed = val
        self.rect.y = self.rect.y + self.yspeed
        
    def horizontal(self, val):
        self.xspeed = val
        self.rect.x = self.rect.x + self.xspeed

all_sprites_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

pacman = Player( 30, 30, 30, 30, 0, 0)
all_sprites_list.add(pacman)


f = open("map.json", "rt")
maze = json.load(f)
f.close()

for y in range(25):
    for x in range(25):
        if maze[y][x] == 1:
            my_wall = tile(BLUE, 30, 30, x*30, y*30)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)


Node_List = [(180,30),(30,30)]


done = False

### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event
            
    # -- Game logic goes after this comment
    pos = (pacman.rect.x, pacman.rect.y)
    if pos == Node_List():
        print(pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        pacman.horizontal(1)
        pacman.vertical(0)
    if keys[pygame.K_LEFT]: 
        pacman.horizontal(-1)
        pacman.vertical(0)
    if keys[pygame.K_UP]:
        pacman.vertical(-1)
        pacman.horizontal(0)
    if keys[pygame.K_DOWN]:
        pacman.vertical(1)
        pacman.horizontal(0)
        
    player_hit_list = pygame.sprite.spritecollide(pacman, wall_list, False)

    for foo in player_hit_list:
        pacman.vertical(0)
        pacman.horizontal(0)
        pacman.rect.x = pacman_old_x
        pacman.rect.y = pacman_old_y
        # Run the update function for all sprites
    pacman_old_x = pacman.rect.x
    pacman_old_y = pacman.rect.y

    all_sprites_list.update()
    # -- Screen background is BLACK
    screen.fill (BLACK)
    

    # -- Draw here
    all_sprites_list.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
