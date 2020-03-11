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
size = (750,750)
screen = pygame.display.set_mode(size)

class Tile(pygame.sprite.Sprite):
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
    def __init__(self, width, height, direction, x_ref, y_ref, xspeed, yspeed):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.direction = direction
        self.image = pygame.image.load(self.direction).convert()
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

    def face(self, val):
        self.direction = val
        self.image = pygame.Surface([30,30])
        self.image = pygame.image.load(self.direction).convert()
        self.image = pygame.transform.scale(self.image, (30,30))
        self.image.set_colorkey(BLACK)

class Ghost(pygame.sprite.Sprite):
    def __init__(self, width, height, x_ref, y_ref, xspeed, yspeed):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load('Blinky.png').convert()
        self.image = pygame.transform.scale(self.image, (width,height))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.xspeed = xspeed
        self.yspeed = yspeed

    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed

    def vertical(self,val):
        self.yspeed = val
        self.rect.y = self.rect.y + self.yspeed
        
    def horizontal(self, val):
        self.xspeed = val
        self.rect.x = self.rect.x + self.xspeed

class Junctions(pygame.sprite.Sprite):
    def __init__(self, x_ref, y_ref, up, down, left, right):
        self.x = x_ref
        self.y = y_ref
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def CanGoUp(self):
        return self.up

    def CanGoDown(self):
        return self.down

    def CanGoLeft(self):
        return self.left

    def CanGoRight(self):
        return self.right

all_sprites_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
blocked_x = []
blocked_y = []

left = 'L-PAC.png'
right = 'R-PAC.png'
direction = left

pacman = Player( 30, 30, direction, 30, 30, 0, 0)
all_sprites_list.add(pacman)

Blinky = Ghost(30, 30, 690, 690, 1, 0)
all_sprites_list.add(Blinky)

ghost_group = pygame.sprite.Group()
ghost_group.add(Blinky)

ghost_hit_list = pygame.sprite.Group()
collision = pygame.sprite.Group()

pacman_life = 3


f = open("map.json", "rt")
maze = json.load(f)
f.close()

for y in range(25):
    for x in range(25):
        if maze[y][x] == 1:
            my_wall = Tile(BLUE, 30, 30, x*30, y*30)
            wall_list.add(my_wall)
            blocked_x.append(x*30)
            blocked_y.append(y*30)
            all_sprites_list.add(my_wall)

junction_A = Junctions(30, 30, False, True, False, True)
junction_B = Junctions(180, 30, False, True, True, True)
junction_C = Junctions(330, 30, False, True, True, False)
junction_D = Junctions(390, 30, False, True, False, True)
junction_E = Junctions(540, 30, False, True, True, True)
junction_F = Junctions(690, 30, False, True, True, False)
junction_G = Junctions(30, 120, True, True, False, True)
junction_H = Junctions(180, 120, True, True, True, True)
junction_I = Junctions(240, 120, False, True, True, True)
junction_J = Junctions(330, 120, True, False, True, True)
junction_K = Junctions(390, 120, True, False, True, True)
junction_L = Junctions(480, 120, False, True, True, True)
junction_M = Junctions(540, 120, True, True, True, True)
junction_N = Junctions(690, 120, True, True, True, False)
junction_O = Junctions(30, 180, True, False, False, True)
junction_P = Junctions(180, 180, True, True, True, False)
junction_Q = Junctions(540, 180, True, True, False, True)
junction_R = Junctions(690, 180, True, False, True, False)
junction_S = Junctions(240, 210, True, False, False, True)
junction_T = Junctions(330, 210, False, True, True, False)
junction_U = Junctions(390, 210, False, True, False, True)
junction_V = Junctions(480, 210, True, False, True, False)
junction_W = Junctions(240, 270, False, True, False, True)
junction_X = Junctions(330, 270, True, False, True, True)
junction_Y = Junctions(360, 270, False, True, True, True)
junction_Z = Junctions(390, 270, True, False, True, True)
junction_A2 = Junctions(480, 270, False, True, True, False)
junction_B2 = Junctions(180, 330, True, True, True, True)
junction_C2 = Junctions(240, 330, True, True, True, False)
junction_D2 = Junctions(300, 330, False, True, False, True)
junction_E2 = Junctions(360, 330, True, True, True, True)
junction_F2 = Junctions(180, 330, True, False, True, False)
junction_G2 = Junctions(180, 330, True, False, True, False)
junction_H2 = Junctions(180, 330, True, False, True, False)






Node_List = [(30,30),(180,30),(330,30),(390,30),(540,30),(690,30),
             (30,120),(180,120),(240,120),(330,120),(390,120),(480,120),(540,120),(690,120),
             (30,180),(180,180), (540,180), (690,180),
             (240,210),(330,210),(390,210),(480,210),
             (240,270),(330,270),(360,270),(390,270),(480,270),
             (180,330),(240,330),(300,330),(360,330),(420,330),(480,330),(540,330),
             (300,360),(360,360),(420,360),
             (240,420),(480,420),
             (30,480),(180,480),(240,480),(330,480),(390,480),(480,480),(540,480),(690,480),
             (30,540),(90,540),(180,540),(240,540),(330,540),(390,540),(480,540),(540,540),(630,540),(690,540),
             (30,600),(90,600),(180,600),(240,600),(330,600),(390,600),(480,600),(540,600),(630,600),(690,600),
             (30,690),(330,690),(540,690),(690,690)
             ]

done = False
#print(blocked_x)


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


    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and pos in Node_List:
        pacman.horizontal(1)
        pacman.vertical(0)
        pacman.face(right)
    if keys[pygame.K_LEFT] and pos in Node_List: 
        pacman.horizontal(-1)
        pacman.vertical(0)
        pacman.face(left)
    if keys[pygame.K_UP] and pos in Node_List:
        pacman.vertical(-1)
        pacman.horizontal(0)
    if keys[pygame.K_DOWN] and pos in Node_List:
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

    ghost_hit_list = pygame.sprite.spritecollide(Blinky, wall_list, False)
    #ghost_hit_list = pygame.sprite.groupcollide(ghost_group, wall_list, False, False)

    for g in ghost_hit_list:
        Blinky.vertical(0)
        Blinky.horizontal(0)
        Blinky.rect.x = Blinky_old_x
        Blinky.rect.y = Blinky_old_y
    Blinky_old_x = Blinky.rect.x
    Blinky_old_y = Blinky.rect.y


    #collision = pygame.sprite.spritecollide(ghost_group, pacman, True)
    if Blinky.rect.x == pacman.rect.x and Blinky.rect.y == pacman.rect.y:
        pacman_life = pacman_life - 1
        Blinky.rect.x = 330
        Blinky.rect.y = 330
        pacman.rect.x = 30
        pacman.rect.y = 30

    Blinky_pos = (Blinky.rect.x, Blinky.rect.y)

#    if Blinky_pos in Node_List:




            
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
