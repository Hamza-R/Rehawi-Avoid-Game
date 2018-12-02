import pygame 
from pygame.locals import *
import random
import math

  #Defining some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (30, 144,255)
DBLUE = (72, 61, 139)
PINK = (255, 20, 147)
GOLD = (218, 165, 32) #CoinColour

TEXTCOLOUR = (255, 255, 255)

pygame.init()

#Setting width and height of screen
Size = (700, 500)
screen = pygame.display.set_mode(Size)

FPS = 60

#Method to draw any text to our screen
def drawText(text, font, surface, x, y):

    textobject = font.render(text, 1, TEXTCOLOUR)
    textrect = textobject.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobject, textrect) 

    
#Font Choice
font = pygame.font.SysFont(None, 30)


#Press Key to stare game - main menu still needs to be created
def PressKeyToStart():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    done = True
                return


            
#Text for main menu of game
drawText('Evasion', font, screen, (345), (250) ) # X pos/Y pos of Evasion text
drawText('Press a key to start.', font, screen, (345) , (270) ) #X pos/Y pos of rest text
pygame.display.update()
PressKeyToStart()

        
pygame.display.set_caption("Evasion")
#Set the mouse cursor to invisble so it doesn't get in the way of the game
pygame.mouse.set_visible(False)

#Continuously run until the user clicks the close button
done = False

#Manage speed of screen updates
clock = pygame.time.Clock()

x_coord = 350
y_coord = 490

x_speed = 0
y_speed = 0

score = 0
scoreincrease = False
ammo = 50
gameover = False


class Enemy(pygame.sprite.Sprite):

    def __init__(self, color, width, height, speed,evader, gameover):
        super().__init__()

        self.speed_x = 0
        self.speed_y = speed
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 400)
        self.evader = evader
        self.gameover = gameover

    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        if self.rect.y > 500:
            self.reset_pos()

        sprite_collide_list = pygame.sprite.spritecollide(self, self.evader,True)
        for x in sprite_collide_list:  
            print("playercollide")
            gameover = True
            
        
    def reset_pos(self):
         self.rect.x = random.randrange (0,680)
         self.rect.y=0

         
class Evader(pygame.sprite.Sprite):

    def __init__ (self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x_speed = 0
        self.y_speed = 0
        self.rect.x = 345
        self.rect.y = 490


    def get_X(self):
         return self.rect.x

    def update(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.x > 690:
            self.rect.x = 690
        elif self.rect.y > 490:
            self.rect.y = 490
        else:
            self.rect.x = self.rect.x + x_speed
            self.rect.y = self.rect.y + y_speed

    def shoot_bullet(self):
        if spacebar == True:

            my_bullet = Bullet (PINK, 5, 5, 5, my_evader.rect.x +2.5, my_evader.rect.y, enemy_group)
            all_sprites_group.add(my_bullet)
            
class Bullet(pygame.sprite.Sprite):

    def __init__ (self, color, width, height, yspeed, xposition, yposition, enemy):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.enemy = enemy
        self.rect = self.image.get_rect()
        self.rect.x = xposition
        self.rect.y = yposition
        self.yspeed = -5

    def update(self):
        self.rect.y = self.rect.y + self.yspeed
        sprite_collide_list = pygame.sprite.spritecollide(self, self.enemy,True)
        for x in sprite_collide_list: 
            print("enemyshot")            
            scoreincrease = True        

#PowerUp class area
class Power_up(pygame.sprite.Sprite):

    def __init__ (self, color, width, height):
        super().__init__()

        self.image = pygame.Surface
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 400)

class Coins(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        
class Power_up_Bullet(Power_up):
    def __init__(self):
        super().__init__()
        
        
class Power_up_Invunerability(Power_up):
    def __init__(self):
        super().__init__()
        
class Power_up_SpeedUp(Power_up):
    def __init__(self):
        super().__init__()


evader_group =pygame.sprite.Group()        
enemy_group = pygame.sprite.Group()
#List of all sprites
all_sprites_group = pygame.sprite.Group()

enemy_number = 25
for x in range (enemy_number):
    my_enemy = Enemy(BLACK, 10, 10, 5, evader_group,gameover)
    enemy_group.add(my_enemy)
    all_sprites_group.add (my_enemy)

my_evader = Evader(RED, 10, 10)
all_sprites_group.add (my_evader)
evader_group.add(my_evader)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT):
                x_speed = -3
            if (event.key == pygame.K_RIGHT):
                x_speed = 3
            if (event.key == pygame.K_UP):
                y_speed = -3
            if (event.key == pygame.K_DOWN):
                y_speed = 3
            if (event.key == pygame.K_SPACE):
                if ammo > 0:
                    spacebar = True
                    ammo -= 1
                    Evader.shoot_bullet(Bullet)

            
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT):
                x_speed=0
            if (event.key == pygame.K_RIGHT):
                x_speed=0
            if (event.key == pygame.K_UP):
                y_speed=0
            if (event.key == pygame.K_DOWN):
                y_speed=0
            if (event.key == pygame.K_SPACE):
                spacebar = False
               


         
    # --- Game logic should go here
    all_sprites_group.update()
    my_evader.x_speed=x_speed
    my_evader.y_speed=y_speed
 
    score = score + 1 

    if scoreincrease == True:
        score = score + 50
    else:
        score = score 

    if gameover == True:
        score = score

        drawText("GAME OVER", font, screen,(320), (25))
        aScore = "Score: %s" %(score)
        drawText(aScore, font, screen, (350), (50))
        screen.fill(BLACK)
        pygame.display.update()
        
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(DBLUE)
 
    # --- Drawing code should go here
    #pygame.draw.rect(screen, BLACK, [x_coord,y_coord,10,10])
    all_sprites_group.draw(screen)
    aScore = "Score: %s" %(score)
    drawText(aScore, font, screen, (565), (5))
    aAmmo = "Ammo: %s" %(ammo)
    drawText (aAmmo, font, screen, (565), (25))
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second 
    clock.tick(FPS)
 
# Close the window and quit.
pygame.quit()




#SET SCORE AS CLASS METHOD FOR SCORE INCREASE INSTEAD OF VARIABLE AS VARIABLE IS IMMUTABLE ETC ETC
#PERHAPS EVEN SET OVERALL AS GAME CLASS TO TRACK ALL OF THE GAMES IMPORTANT VARIABLES AND ETC
