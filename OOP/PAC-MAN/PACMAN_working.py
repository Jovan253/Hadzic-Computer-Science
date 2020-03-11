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

class Junctions:
    x = 0
    y = 0
    canGoUp = False
    canGoDown = False
    canGoLeft = False
    canGoRight = False
    
    def __init__(self, x_ref, y_ref, up, down, left, right):
        self.x = x_ref
        self.y = y_ref
        self.canGoUp = up
        self.canGoDown = down
        self.canGoLeft = left
        self.canGoRight = right

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
    def __init__(self, width, height, face, x_ref, y_ref, xspeed, yspeed, name):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.face = face
        self.image = pygame.image.load(self.face).convert()
        self.image = pygame.transform.scale(self.image, (width,height))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.name = name

    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.x > 750:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = 750

    def vertical(self,val):
        self.yspeed = val
        self.rect.y = self.rect.y + self.yspeed
        
    def horizontal(self, val):
        self.xspeed = val
        self.rect.x = self.rect.x + self.xspeed

    moving = ""
    name = ""

    def moveLeft(self):
        self.horizontal(-1)
        self.vertical(0)
        self.moving = "LEFT"
        #print("moving ", self.moving, self.rect.x, self.rect.y)

    def moveRight(self):
        self.horizontal(1)
        self.vertical(0)
        self.moving = "RIGHT"
        #print("moving ", self.moving, self.rect.x, self.rect.y)

    def moveUp(self):
        self.horizontal(0)
        self.vertical(-1)
        self.moving = "UP"
        #print("moving ", self.moving, self.rect.x, self.rect.y)

    def moveDown(self):
        self.horizontal(0)
        self.vertical(1)
        self.moving = "DOWN"
        #print("moving ", self.moving, self.rect.x, self.rect.y)

    def moveAtJunction(self, junction):
        GhostAtJunction = False
        if self.rect.x == junction.x and self.rect.y == junction.y:
            print(self.name, " at junction = ", junction.x, junction.y)
            GhostAtJunction = True

        if GhostAtJunction:

            if pacman.rect.x == self.rect.x and pacman.rect.y == self.rect.y:
                #do nothing
                print("do nothing")

            elif pacman.rect.x <= self.rect.x and pacman.rect.y <= self.rect.y:
                # packman in top left quadrant
                if junction.canGoUp and not self.moving == "DOWN":
                    self.moveUp()
                elif junction.canGoLeft and not self.moving == "RIGHT":
                    self.moveLeft()
                elif junction.canGoRight and not self.moving == "LEFT":
                    self.moveRight()
                elif junction.canGoDown and not self.moving == "UP":
                    self.moveDown()
                else:
                    print("stuck at junction ", junction.x, junction.y)

            elif pacman.rect.x <= self.rect.x and pacman.rect.y >= self.rect.y:
                # packman in bottom left quadrant
                if junction.canGoLeft and not self.moving == "RIGHT":
                    self.moveLeft()
                elif junction.canGoDown and not self.moving == "UP":
                    self.moveDown()
                elif junction.canGoRight and not self.moving == "LEFT":
                    self.moveRight()
                elif junction.canGoUp  and not self.moving == "DOWN":
                    self.moveUp()
                else:
                    print("stuck at junction ", junction.x, junction.y)

            elif pacman.rect.x >= Blinky.rect.x and pacman.rect.y <= Blinky.rect.y:
                # packman in top rigth quadrant
                if junction.canGoRight and not self.moving == "LEFT":
                    self.moveRight()
                elif junction.canGoUp and not self.moving == "DOWN":
                    self.moveUp()
                elif junction.canGoLeft and not self.moving == "RIGHT":
                    self.moveLeft()
                elif junction.canGoDown and not self.moving == "UP":
                    self.moveDown()
                else:
                    print("stuck at junction ", junction.x, junction.y)

            elif pacman.rect.x >= self.rect.x and pacman.rect.y >= self.rect.y:
                # packman in bottom rigth quadrant
                if junction.canGoRight and not self.moving == "LEFT":
                    self.moveRight()
                elif junction.canGoDown and not self.moving == "UP":
                    self.moveDown()
                elif junction.canGoLeft and not self.moving == "RIGHT":
                    self.moveLeft()
                elif junction.canGoUp and not self.moving == "DOWN":
                    self.moveUp()
                else:
                    print("stuck at junction ", junction.x, junction.y)

    def collide(self):        
        if self.rect.x == pacman.rect.x and self.rect.y == pacman.rect.y:
            pacman_life = pacman_life - 1
            pacman.rect.x = 30
            pacman.rect.y = 30
            #print(self.moving, self.rect.x, self.rect.y)
#endclass            
        

all_sprites_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
blocked_x = []
blocked_y = []

left = 'L-PAC.png'
right = 'R-PAC.png'
direction = left

pacman = Player( 30, 30, direction, 30, 30, 0, 0)
all_sprites_list.add(pacman)

Blinky = Ghost(30, 30,'Blinky.png', 690, 690, 1, 0, "Blinky")
#Pinky = Ghost(30, 30, 'Pinky.png', 330, 330, 1, 0, "Pinky")
#Clyde = Ghost(30, 30, 'Clyde.png', 30, 540, 1, 0, "Clyde")
all_sprites_list.add(Blinky)
#all_sprites_list.add(Pinky)
#all_sprites_list.add(Clyde)



pacman_life = 3

junction_list = []

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

junction_list.append(Junctions(30, 30, False, True, False, True))
junction_list.append(Junctions(180, 30, False, True, True, True))
junction_list.append(Junctions(330, 30, False, True, True, False))
junction_list.append(Junctions(390, 30, False, True, False, True))
junction_list.append(Junctions(540, 30, False, True, True, True))
junction_list.append(Junctions(690, 30, False, True, True, False))
junction_list.append(Junctions(30, 120, True, True, False, True))
junction_list.append(Junctions(180, 120, True, True, True, True))
junction_list.append(Junctions(240, 120, False, True, True, True))
junction_list.append(Junctions(330, 120, True, False, True, True))
junction_list.append(Junctions(390, 120, True, False, True, True))
junction_list.append(Junctions(480, 120, False, True, True, True))
junction_list.append(Junctions(540, 120, True, True, True, True))
junction_list.append(Junctions(690, 120, True, True, True, False))
junction_list.append(Junctions(30, 180, True, False, False, True))
junction_list.append(Junctions(180, 180, True, True, True, False))
junction_list.append(Junctions(540, 180, True, True, False, True))
junction_list.append(Junctions(690, 180, True, False, True, False))
junction_list.append(Junctions(240, 210, True, False, False, True))
junction_list.append(Junctions(330, 210, False, True, True, False))
junction_list.append(Junctions(390, 210, False, True, False, True))
junction_list.append(Junctions(480, 210, True, False, True, False))
junction_list.append(Junctions(240, 270, False, True, False, True))
junction_list.append(Junctions(330, 270, True, False, True, True))
junction_list.append(Junctions(360, 270, False, True, True, True))
junction_list.append(Junctions(390, 270, True, False, True, True))
junction_list.append(Junctions(480, 270, False, True, True, False))
junction_list.append(Junctions(180, 330, True, True, True, True))
junction_list.append(Junctions(240, 330, True, True, True, False))
junction_list.append(Junctions(300, 330, False, True, False, True))
junction_list.append(Junctions(360, 330, True, True, True, True))
junction_list.append(Junctions(420, 330, False, True, True, False))
junction_list.append(Junctions(480, 330, True, True, False, True))
junction_list.append(Junctions(540, 330, True, True, True, True))
junction_list.append(Junctions(300, 360, True, False, False, True))
junction_list.append(Junctions(360, 360, True, False, True, True))
junction_list.append(Junctions(420, 360, True, False, True, False))
junction_list.append(Junctions(240, 420, True, True, False, True))
junction_list.append(Junctions(480, 420, True, True, True, False))
junction_list.append(Junctions(30, 480, False, True, False, True))
junction_list.append(Junctions(180, 480, True, True, False, True))
junction_list.append(Junctions(240, 480, True, False, True, True))
junction_list.append(Junctions(330, 480, False, True, True, False))
junction_list.append(Junctions(390, 480, False, True, False, True))
junction_list.append(Junctions(480, 480, True, False, True, True))
junction_list.append(Junctions(540, 480, True, True, True, True))
junction_list.append(Junctions(690, 480, False, True, True, False))
junction_list.append(Junctions(30, 540, True, False, False, True))
junction_list.append(Junctions(90, 540, False, True, True, False))
junction_list.append(Junctions(180, 540, True, True, True, False))
junction_list.append(Junctions(240, 540, False, True, True, True))
junction_list.append(Junctions(330, 540, True, False, True, True))
junction_list.append(Junctions(390, 540, True, False, True, True))
junction_list.append(Junctions(480, 540, False, True, True, True))
junction_list.append(Junctions(540, 540, True, True, True, False))
junction_list.append(Junctions(630, 540, False, True, False, True))
junction_list.append(Junctions(690, 540, True, False, True, False))
junction_list.append(Junctions(30, 600, False, True, False, True))
junction_list.append(Junctions(90, 600, True, False, True, True))
junction_list.append(Junctions(180, 600, True, False, True, False))
junction_list.append(Junctions(240, 600, True, False, False, True))
junction_list.append(Junctions(330, 600, False, True, True, False))
junction_list.append(Junctions(390, 600, False, True, False, True))
junction_list.append(Junctions(480, 600, True, False, True, False))
junction_list.append(Junctions(540, 600, True, False, False, True))
junction_list.append(Junctions(630, 600, True, False, True, True))
junction_list.append(Junctions(690, 600, False, True, True, False))
junction_list.append(Junctions(30, 690, True, False, False, True))
junction_list.append(Junctions(330, 690, True, False, True, True))
junction_list.append(Junctions(540, 690, True, False, True, True))
junction_list.append(Junctions(690, 690, True, False, True, False))

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

    if pacman.rect.x > 750:
        pacman.rect.x = 0
    elif pacman.rect.x < 0:
        pacman.rect.x = 750

    

    #if Ghost.rect.x == pacman.rect.x and Ghost.rect.y == pacman.rect.y:
     #   pacman_life = pacman_life - 1
      #  pacman.rect.x = 30
       # pacman.rect.y = 30
        

    for junction in junction_list:

        Blinky.moveAtJunction(junction)
        #Pinky.moveAtJunction(junction)
        #Clyde.moveAtJunction(junction)
        

    if pacman_life == 0:
        font = pygame.font.Font("freesansbold.ttf", 74)
        text = font.render("GAME OVER...", True, RED)
        TextRect = text.get_rect()
        TextRect.center = (width//2, height//2)
        screen.blit(text, TextRect)
        pygame.display.flip()

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
