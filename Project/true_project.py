import pygame
import pygame.mixer
import json

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
screen = (2000, 1000)
size = (700,500)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My Window")
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

        def update(self):
            self.rect.x = self.rect.x + self.speed
            
class Player(pygame.sprite.Sprite):
    def __init__(self, face, width, height, color, x_ref, y_ref, speed, jump, gravity):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.face = face
        self.image = pygame.image.load(self.face).convert()
        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.speed = speed
        self.jump = jump
        self.gravity = gravity
        

    def update(self):
        #self.rect.x += self.speed    ##causes constanr movement
        self.rect.y += self.gravity
        if touching == True:
            self.gravity = 0
        else:
            self.gravity = 1

    def horizontal(self, val):
        self.speed = val
        self.rect.x += self.speed

    def vertical(self,val):
        self.jump = val
        #for x in range(val):
        self.rect.y = self.rect.y + self.jump

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
#lava_list = pygame.sprite.Group()
#count = 0

f = open("map01.json", "rt")
level01 = json.load(f)
f.close()

for y in range(20):
    for x in range(54):
        if level01[y][x] == 1:
            my_block = Block(GREY, 30, 30, x*30, y*30, 0, False)
            block_list.add(my_block)
            all_sprites_list.add(my_block)
            
block1 = Block(GREY, 120, 30, 0, 360, 0, False)
block_list.add(block1)
all_sprites_list.add(block1)
lava = Block(RED, 1500, 30, 0, 470, 0, False)
block_list.add(lava)
all_sprites_list.add(lava)


player = Player("character.png", 30, 30, BLUE, 60, 330, 0, 0, 0)
all_sprites_list.add(player)

touching = False     
hades = Chaser("HADES.png", 30, 90, 0, 240, 1)
all_sprites_list.add(hades)

width = 30
height = 30
p_height = 0

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
        player.horizontal(2)        
    if keys[pygame.K_LEFT]:
        player.horizontal(-2)        
    if keys[pygame.K_SPACE]:
        if touching == True:
            player.vertical(-90)
        else:
            player.vertical(0)
 
    contact_list = pygame.sprite.spritecollide(player, block_list, False)
    #death_list = pygame.sprite.spritecollide(lava_list, player, True)

    touching = False

    for x in contact_list:
        touching = True
        
        #if player.speed > 0:
        #    player.rect.right = x.rect.left
        #elif player.speed < 0:
         #   player.rect.left = x.rect.right

        if player.gravity > 0:
            player.rect.bottom = x.rect.top
        elif player.gravity < 0:
            player.rect.top = x.rect.bottom
        
        for block in block_list:
            if block.dying == True:
                block.life += -1
                if block.life < 0:
                    all_sprites_list.remove(block)
                    all_sprites_list.update()

   # for x in break_list:
    #    touching = True
     #   player.vertical(-1)
      #  crumbling_block.life = crumbling_block.life - 1
        #cb2.life += -1
       # if crumbling_block.life < 0:
        #    all_sprites_list.remove(crumbling_block)
         #   all_sprites_list.update()
        #elif cb2.life < 0:
         #   all_sprite_list.remove(cb2)
          #  all_sprite_list.update()

    #for block in block_list:
     #   if player.rect.x > 600:
      #      block.rect.x += 30
    #all_sprites_list.update()

    if player.rect.y == lava.rect.y - 30:
        for i in range(2):
            p_height += 10
            new_height = height - p_height
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
        for block in block_list:
            block.rect.y -= shift_y
        


    if player.rect.x >= 600:
        shift_x = player.rect.x - 600
        player.rect.x = 600
        for block in block_list:
            block.rect.x -= shift_x
    elif player.rect.x <= 50:
        shift_x = 50 - player.rect.x
        player.rect.x = 50
        for block in block_list:
            block.rect.x += shift_x


    
        
    all_sprites_list.update()
    # -- Screen background is BLACK
    screen.fill(BLACK)
    
    # -- Draw here
    all_sprites_list.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # -- The clock ticks over
    clock.tick(60)
    
#End While - End of game loop
pygame.quit()     
      
