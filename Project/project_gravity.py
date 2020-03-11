import pygame
import pygame.mixer

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
m_width = 2000
m_height = 1000
map1 = (m_width, m_height)
width = 700
height = 500
size = (width, height)
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
    def __init__(self, width, height, color, x_ref, y_ref, speed, jump, gravity):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.speed = speed
        self.jump = jump
        self.gravity = gravity
        

    def update(self):
        #self.rect.x += self.speed    ##causes constant movement
        self.rect.y += self.gravity
        if touching == True:
            self.gravity = 0
            #self.vertical()
        elif touching == False:
            self.gravity = 2

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
crumbling_list = pygame.sprite.Group()

block1 = Block(GREY, 300, 30, 0, 360, 0, False)
block_list.add(block1)
all_sprites_list.add(block1)
crumbling_block = Block(GREY, 500, 30, 270, 300, 180, True)
block_list.add(crumbling_block)
all_sprites_list.add(crumbling_block)
lava = Block(RED, 700, 30, 0, 470, 0, False)
all_sprites_list.add(lava)

player = Player(30, 30, BLUE, 60, 330, 0, 0, 1)
all_sprites_list.add(player)

touching = False
jumping = False
hades = Chaser("HADES.png", 30, 90, 0, 240, 1)
all_sprites_list.add(hades)

#f = open("map.json", "rt")
#maze = json.load(f)
#f.close()
count = 0

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
            jumping = True
        else:
            player.vertical(0)
 
    contact_list = pygame.sprite.spritecollide(player, block_list, False)
   # break_list = pygame.sprite.spritecollide(player, crumbling_list, False)

    touching = False

    for x in contact_list:
        touching = True
        player.vertical(0)
        player.gravity = 0

    for block in block_list:
        if block.rect.y < player.rect.y:
                player.vertical(-1)
                
            
            
            

        
    if player.rect.y > 470:
        pygame.mixer.Sound.play(death)
        pygame.time.wait(1000)
        pygame.quit()



        
    if player.rect.x >= 600:
        shift_x = player.rect.x - 600
        player.rect.x = 600
        for block in block_list:
            block.rect.x += -shift_x
        
        

                
        
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
     
