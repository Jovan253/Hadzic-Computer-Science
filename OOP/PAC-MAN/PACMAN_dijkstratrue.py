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

A = (30,30)
B = (180, 30)
C = (330, 30)
D = (390, 30)
E = (540, 30)
F = (690, 30)

G = (30, 120)
H = (180, 120)
I = (240, 120)
J = (330, 120)
K = (390,120)
L = (480,120)
M = (540,120)
N = (690,120)

O = (30,180)
P = (180,180)
Q = (540,180)
R = (690,180)

S = (240,210)
T = (330,210)
U = (390,210)
V = (480,210)

W = (240,270)
X = (330,270)
Y = (360,270)
Z = (390, 270)
Z1 = (480,270)

A2 = (180,330)
B2 = (240,330)
C2 = (300,330)
D2 = (360,330)
E2 = (420,330)
F2 = (480,330)
G2 = (540,330)

H2 = (300,360)
I2 = (360,360)
J2 = (420,360)

K2 = (240,420)
L2 = (480,420)

M2 = (30,480)
N2 = (180,480)
O2 = (240,480)
P2 = (330,480)
Q2 = (390,480)
R2 = (480,480)
S2 = (540,480)
T2 = (690,480)

U2 = (30,540)
V2 = (90,540)
W2 = (180,540)
X2 = (240,540)
Y2 = (330,540)
Z2 = (390,540)
A3 = (480,540)
B3 = (540,540)
C3 = (630,540)
D3 = (690,540)

E3 = (30,600)
F3 = (90,600)
G3 = (180,600)
H3 = (240,600)
I3 = (330,600)
J3 = (390,600)
K3 = (480,600)
L3 = (540,600)
M3 = (630,600)
N3 = (690,600)

O3 = (30,690)
P3 = (330,690)
Q3 = (390,690)
R3 = (690,690)

graph = {
    A: {B: 5, G: 4},
    B: {A: 5, C:5, H:4},
    C: {B: 5, J: 4},
    D: {E: 5, K:4},
    E: {D: 5, F:5, M:4},
    F: {E: 5, N: 4},
    G: {A: 4, H:5, O:2},
    H: {B: 4, G:5, I:2, P:2 },
    I: {H:2, J:3, S:3},
    J: {C:4, I:3, K:2},
    K: {D:4, J:2, L:3},
    L: {K:3, M:2, V:3},
    M: {E:4, L:2, N:5, Q:2},
    N: {F:4, M:5, R:2},
    O: {G:2, P:5},
    P: {H:2, O:5, A2:5},
    Q: {M:2, R:5, G2:5},
    R: {N:2, Q:5},
    S: {I:3, T:3},
    T: {T:3, X:2},
    U: {V:3, Z:2},
    V: {L:3, U:3},
    W: {X:3, B2:2},
    X: {T:2, X:3, Y:1},
    Y: {X:1, Z:1, D2:2},
    Z: {U:2, Y:1, Z1:3},
    Z1: {Z:3, F2:2},

    A2: {P:5, B2:2, N2:5},
    B2: {W:2, A2:2, K2:3},
    C2: {D2:2, H2:2},
    D2: {Y:2, C2:2, E2:2, I2:2},
    E2: {D2:2, J2:2},
    F2: {Z1:2, G2:2, L2:3},
    G2: {Q:5, F2:2, S2:5},
    H2: {C2:2, I2:2},
    I2: {D2:2, H2:2, J2:2},
    J2: {E2:2, I2:2},
    K2: {B2:3, L2:6, O2:2},
    L2: {F2:3, K2:6, R2:2},
    M2: {N2:5, U2:2},
    N2: {A2:5, M2:5, O2:2, W2:2},
    O2: {K2:2, N2:2, P2:3},
    P2: {O2:3, Y2:2},
    Q2: {R2:3, Z2:2},
    R2: {L2:2, Q2:3, S2:2},
    S2: {G2:5, R2:2, T2:5, B3:2},
    T2: {S2:5, D3:2},
    U2: {M2:2, V2:2},
    V2: {V2:2, F3:2},
    W2: {N2:2, X2:2, G3:2},
    X2: {W2:2, Y2:3, H3:2},
    Y2: {P2:2, X2:3, Z2:2},
    Z2: {Q2:2, Y2:2, A3:3},

    A3: {Z2:3, K3:2, B3:2},
    B3: {S2:2, A3:2, L3:2},
    C3: {D3:2, M3:2},
    D3: {C3:2, T2:2},
    E3: {F3:2, O3:3},
    F3: {V2:2, E3:2, G3:3},
    G3: {W2:2, F3:3},
    H3: {X2:2, I3:3},
    I3: {H3:3, P3:3},
    J3: {K3:3, Q3:3},
    K3: {A3:2, J3:3},
    L3: {B3:2, M3:3},
    M3: {C3:2, L3:3, N3:2},
    N3: {M3:2, R3:3},
    O3: {E3:3, P3:10},
    P3: {I3:3, O3:10, Q3:2},
    Q3: {J3:3, P3:2, R3:10},
    R3: {N3:3, Q3:10},
    
}

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
