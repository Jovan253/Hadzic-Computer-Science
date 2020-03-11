import pygame
import pygame.mixer
import json
import math

# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
GREY = (152, 152, 152)

# -- Initialise PyGame
pygame.init()

pygame.mixer.init()
#pygame.mixer.music.load()
death = pygame.mixer.Sound("Lava.wav")


# -- Blank Screen
#screen = (2000, 1000)
size = (700,500)
screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
# -- Title of new window/screen
pygame.display.set_caption("My Game")
# -- Exit game flag set to false
game_over = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

class Block(pygame.sprite.Sprite):
# Define the constructor for invader
    def __init__(self, color, width, height, x_ref, y_ref, life, dying):
# Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.life = life
        self.dying = dying
        #x_difference = 50
        #y_difference = 0
        #c_squared = 0 
        #distance = 0

    def update(self):
        for self in block_list:
            if self.dying == True:
                if self.rect.x - player.rect.x < 100:
                    #print("ello")
                    self.life += -1
                if self.life == 0:
                    all_sprites_list.remove(self)
                    block_list.remove(self)
                    all_sprites_list.update()

    #def destruction(self):
        #x_difference = self.rect.x - player.rect.x
        #y_difference = self.rect.y - player.rect.y
        #c_squared = (x_difference ^ 2) + (y_difference ^ 2)
        #distance = int(math.sqrt(c_squared))
        #print(distance)


        

class Chaser(pygame.sprite.Sprite):
# Define the constructor for invader
    def __init__(self, face, width, height, x_ref, y_ref, speed):
# Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.face = face
        self.image = pygame.image.load(self.face).convert()
        self.image = pygame.transform.scale(self.image, (width,height))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.speed = speed
        self.dt = 0
        self.time_since = 0

    def update(self):
        self.rect.x += self.speed

        #self.placement()
        
        self.dt = clock.tick()
        self.time_since += self.dt
        if self.time_since > 30:
            fireball = Circ_Projectile(RED, 5, self.rect.x + 30, self.rect.y, 3, 0)
            circles.append(fireball)
            self.time_since = 0
            #if player.rect.y > self.rect.y:
                #fireball.speed_x = 2
             #   fireball.speed_y = 2
            #elif player.rect.y < self.rect.y:
                #fireball.speed_x = 2
             #   fireball.speed_y = -2
            #elif player.rect.y == self.rect.y:
                #fireball.speed_x = 2
             #   fireball.speed_y = 0

        self.placement()

    def placement(self):
        if player.rect.y > self.rect.y:
            self.rect.y += 1
        elif player.rect.y < self.rect.y:
            self.rect.y += -1
        elif player.rect.y == self.rect.y:
            self.rect.y = player.rect.y
    

class Circ_Projectile(pygame.sprite.Sprite):
    def __init__(self, colour, radius, x_ref, y_ref, speed, thick):
        super().__init__()
        self.surface = screen
        self.colour = colour
        self.x = x_ref
        self.y = y_ref
        self.radius = radius
        self.speed = speed
        self.thick = thick

    def update(self):
        self.x += self.speed
        
    def draw(self):
        self.pos = (self.x, self.y)
        pygame.draw.circle(self.surface, self.colour, self.pos, self.radius, 0)





            
            
class Player(pygame.sprite.Sprite):
    def __init__(self, face, width, height, color, x_ref, y_ref, speed, gravity):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.face = face
        self.image = pygame.image.load(self.face).convert()
        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.speed = speed
        self.gravity = 0

    def update(self):
        #self.rect.x += self.speed    ##causes constanr movement
        self.rect.y += self.gravity
        #print(self.gravity)
        

        if touching == True:
            self.gravity = 0
        elif touching == False:
            
            if self.gravity == 0:
                self.gravity = 1
            else:
                self.gravity += .35



    def horizontal(self, val):
        self.speed = val
        self.rect.x += self.speed

    def jump(self):
        #self.rect.y = self.rect.y + self.jump
        #if touching == True:
        player.gravity = -8
        


#class Level(pygame.sprite.Sprite):
 #   def __init__(self):
 #       self.platform_list = pygame.sprite.Group()
  #      self.world_shift = 0
   #     
  #  def update(self):
   #     self.platform_list.update()

    #def draw(self, screen):
      #  screen.fill(BLACK)
     #   self.platform_list.draw(screen)


#class Level01(Level):
  #  def __init__(self):
 #       Level.__init__(self)

   #     level = [GREY, 90, 30, 0, 360, 0],
    
        

all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
circles = []
#lava_list = pygame.sprite.Group()
#count = 0

f = open("map01.json", "rt")
level01 = json.load(f)
f.close()

for y in range(20):
    for x in range(54):
        if level01[y][x] == 1:
            #num += 1
            #x_val = x*30
            #x_ordered.append(x_val)
            #x_ordered.sort()
            #y_val = y*30
            #y_ordered.append(y_val)
            #y_ordered.sort
            #print(num)
            #if num == 32:
                #for i in range(num):
                    #count += 10
                    #print(count)
            my_block = Block(GREY, 30, 30, x*30, y*30, 3000, True)
            block_list.add(my_block)
            all_sprites_list.add(my_block)
            


#print(ordered)
block1 = Block(GREY, 120, 30, 0, 360, 0, False)
block_list.add(block1)
all_sprites_list.add(block1)
lava = Block(RED, 2000, 30, 0, 470, 0, False)
block_list.add(lava)
all_sprites_list.add(lava)
end_block = Block(GREY, 30, 30, 1680, 200, 0, False)
block_list.add(end_block)
all_sprites_list.add(end_block)


player = Player("character.png", 30, 30, BLUE, 60, 330, 0, 0)
all_sprites_list.add(player)
hades = Chaser("HADES.png", 30, 90, 0, 240, 1)
all_sprites_list.add(hades)

touching = False
#shift = False


screen_height = 500
width = 30
height = 30
p_height = 0
#count = 0


# -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.horizontal(3)        
    if keys[pygame.K_LEFT]:
        player.horizontal(-3)        
    if keys[pygame.K_SPACE]:
        if touching == True:
            player.jump()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

        
 
    contact_list = pygame.sprite.spritecollide(player, block_list, False)
    #death_list = pygame.sprite.spritecollide(lava_list, player, True)

    touching = False
    #shift = False
    #old_y = player.rect.y
    

    for block in contact_list:
        touching = True
        player.rect.y = block.rect.y - 30
        player.gravity = 0
        if player.gravity > 0:
            #player.gravity = -1
            player.rect.bottom = block.rect.top
        elif player.gravity < 0:
            #player.gravity = 1
            if player.speed > 0:
                player.rect.right = block.rect.left
            elif player.speed < 0:
                player.rect.left = block.rect.right
            player.rect.top = block.rect.bottom
            
        #splayer.gravity = 0
        
    #for block in block_list:
     #   if block.dying == True:
      #      block.destruction()
            
            #block.life += -1
           # if block.life < 0:
             #   all_sprites_list.remove(block)
              #  all_sprites_list.update() 

    #if shift == False:
    #old_x = hades.rect.x
    #if shift == True:
     #   hades.rect.x = old_X


    if player.rect.y == lava.rect.y - 30:
        print("hit lava")
        for i in range(2):
            new_height = height - i * 10
            print(new_height)
            player.image = pygame.transform.scale(player.image, (30,new_height))
            pygame.time.wait(500)
            all_sprites_list.update()
        pygame.mixer.Sound.play(death)
        pygame.time.wait(1000)
        pygame.quit()

    if player.rect.y <= 100   :
        shift_y = 100 - player.rect.y
        player.rect.y = 100
        #all_sprites_list.remove(lava)
        for block in block_list:
            block.rect.y += shift_y
    elif player.rect.y >= 450 and lava.rect.x:
        shift_y = player.rect.y - 450
        player.rect.y = 450
       # shift = True
        for block in block_list:
            block.rect.y -= shift_y
        

    if player.rect.x >= 600:
        shift_x = player.rect.x - 600
        player.rect.x = 600
        hades.rect.x = 300
        for block in block_list:
            block.rect.x -= shift_x


    if player.rect.x == end_block.rect.x and player.rect.y == end_block.rect.y:
        print("hit")
        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render("Level Complete", True, BLUE)
        TextRect1 = text.get_rect()
        TextRect1.center = (width//2, 300)
        screen.blit(text, TextRect1)
        pygame.display.update()

   
    for circle in circles:
        circle.update()

    
        
    all_sprites_list.update()
    # -- Screen background is BLACK
    screen.fill(BLACK)
    
    # -- Draw here
    for circle in circles:
        circle.draw()
        
    all_sprites_list.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # -- The clock ticks over
    clock.tick(60)
    
#End While - End of game loop
pygame.quit()     
      
