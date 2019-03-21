import pygame 
from pygame.locals import *
import random
import math

f = open("highscore.txt","rt")
data = f.read()
ingameHS = int(data)
f.close()

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
mainmenu = True

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
                done = True
                return

#Method that resets the game and its feature's when you press R to play again
def Reset():
    if True:
                my_evader.gameover = False
                score = 0
                ammo = 50
                my_evader.rect.x = 345
                my_evader.rect.y = 490




class Enemy(pygame.sprite.Sprite):

    def __init__(self, color, width, height, speed):
        super().__init__()

        self.speed_x = 0
        self.speed_y = speed
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 400)


    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        if self.rect.y > 500:
            self.reset_pos()

            
        
    def reset_pos(self):
         self.rect.x = random.randrange (0,680)
         self.rect.y=0

         
class Evader(pygame.sprite.Sprite):

    def __init__ (self, color, width, height, ammo, gameover, enemy_grp, Power_up_Bullet):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x_speed = 0
        self.y_speed = 0
        self.rect.x = 345
        self.rect.y = 490
        self.ammo = 10
        self.enemy_grp = enemy_grp
        self.gameover = gameover
        self.Power_up_Bullet = Power_up_Bullet


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

        sprite_collide_list = pygame.sprite.spritecollide(self, self.enemy_grp, False)
        for x in sprite_collide_list:  
##            print("playercollide")
            self.gameover = True
##            print(self.gameover)
        sprite_collide_list = pygame.sprite.spritecollide(self, power_up_group, True)
        for x in sprite_collide_list:
            my_evader.ammo += 25


    def shoot_bullet(self):
        if spacebar == True and my_evader.gameover == False:

            my_bullet = Bullet (PINK, 5, 5, 5, my_evader.rect.x +2.5, my_evader.rect.y, enemy_group)
            all_sprites_group.add(my_bullet)
##            print("BULLETSHOT")
            
class Bullet(pygame.sprite.Sprite):

    def __init__ (self, color, width, height, yspeed, xposition, yposition, Enemy):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.enemy = Enemy
        self.rect = self.image.get_rect()
        self.rect.x = xposition
        self.rect.y = yposition
        self.yspeed = -5
     

    def update(self):
        self.rect.y = self.rect.y + self.yspeed
        sprite_collide_list = pygame.sprite.spritecollide(self, self.enemy,True)
        for x in sprite_collide_list: 
            print("enemyshot")            
           

#PowerUp class area
class Power_up(pygame.sprite.Sprite):

    def __init__ (self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 400)


class Power_up_coins(Power_up):

    def __init__(self, color, width, height):
        super().__init__(color, width, height)
        
class Power_up_Bullet(Power_up):
    
    def __init__(self, color, width, height):
        super().__init__(color, width, height)       
                
class Power_up_Invunerability(Power_up):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
        
class Power_up_Speed(Power_up):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)

class Power_up_Shield(Power_up):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)

            
#Text for main menu of game
if mainmenu == True:
    drawText('Evasion', font, screen, (345), (250) ) # X pos/Y pos of Evasion text
    drawText('Press a key to start.', font, screen, (345) , (270) ) #X pos/Y pos of rest text
    pygame.display.update()
    PressKeyToStart()
else:
    done = True
pygame.display.set_caption("Evasion")

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
#ammo = 50

power_up_group = pygame.sprite.Group()


evader_group =pygame.sprite.Group()        

enemy_group = pygame.sprite.Group()

#List of all sprites
all_sprites_group = pygame.sprite.Group()

enemy_number = 5
for x in range (enemy_number):
    my_enemy = Enemy(BLACK, 10, 10, 1)
    enemy_group.add(my_enemy)
    all_sprites_group.add (my_enemy)

my_evader = Evader(RED, 10, 10, 0, False, enemy_group, Power_up_Bullet)
all_sprites_group.add (my_evader)
evader_group.add(my_evader)
done = False

num = 5
for x in range (num):
    my_Power_up_bullet = Power_up_Bullet(PINK, 7, 7)
    power_up_group.add(my_Power_up_bullet)
    all_sprites_group.add(my_Power_up_bullet)

    my_coin = Power_up_coins(GOLD, 7, 7)
    power_up_group.add(my_coin)
    all_sprites_group.add(my_coin)

    my_Power_up_Speed = Power_up_Speed(GREEN, 7 ,7)
    power_up_group.add (my_Power_up_Speed)
    all_sprites_group.add(my_Power_up_Speed)

    my_Power_up_Shield = Power_up_Shield(BLUE, 7, 7)
    power_up_group.add(my_Power_up_Shield)
    all_sprites_group.add(my_Power_up_Shield)

    my_Power_up_Invunerability = Power_up_Invunerability (WHITE, 7, 7)
    power_up_group.add(my_Power_up_Invunerability)
    all_sprites_group.add(my_Power_up_Invunerability)
                        
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
                if my_evader.ammo > 0:
                    spacebar = True
                    my_evader.ammo -= 1
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


    if my_evader.gameover == False:
        score = score + 1 
    else:
        score = score + 0


##    if scoreincrease == True:
##        score = score + 50


        
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(DBLUE)
 
    # --- Drawing code should go here
    #pygame.draw.rect(screen, BLACK, [x_coord,y_coord,10,10])
##    print("Decision" + str(my_evader.gameover))

    if my_evader.gameover == True:
        screen.fill(BLACK)
        drawText("GAME OVER", font, screen,(320), (250))
        aScore = "Score: %s" %(score)
        drawText(aScore, font, screen, (350), (270))
        drawText("Press R to play again", font, screen, (300), (290))
        drawText("Press M to return to the main menu", font, screen, (270), (310))
        

        highscore = int(data)
        if score > highscore:
            highscore = score
            data = str(highscore)
            f = open("highscore.txt","wt")
            f.write(data)
            f.close()
        hs = "HighScore %s" %(highscore)
        drawText(hs, font , screen, 300,350)

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_r):
                Reset()
            

##        if (event.key == pygame.K_m):
##          mainmenu = True
##    
##            print (mainmenu)
##        pygame.display.update()
        
    else:
        all_sprites_group.draw(screen)
        aScore = "Score: %s" %(score)
        drawText(aScore, font, screen, (565), (5))
        aAmmo = "Ammo: %s" %(my_evader.ammo)
        drawText (aAmmo, font, screen, (565), (25))
        HS = "HighScore %s" %(ingameHS)
        drawText(HS, font , screen, 545, (45))
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second 
    clock.tick(FPS)
 
# Close the window and quit.
pygame.quit()

#SET SCORE AS CLASS METHOD FOR SCORE INCREASE INSTEAD OF VARIABLE AS VARIABLE IS IMMUTABLE ETC ETC
#PERHAPS EVEN SET OVERALL AS GAME CLASS TO TRACK ALL OF THE GAMES IMPORTANT VARIABLES AND ETC
