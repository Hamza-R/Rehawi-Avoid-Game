import pygame 
from pygame.locals import *
import random
import math

#Defining some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

#Setting width and height of screen
Size = (700, 500)
screen = pygame.display.set_mode(Size)

FPS = 30




pygame.display.set_caption("Evasion")
#Set the mouse cursor to invisble so it doesn't get in the way of the game
pygame.mouse.set_visible(False)

#Continuously run until the user clicks the close button
done = False

#Manage speed of screen updates
clock = pygame.time.Clock()

#Setting up of constants

##enemyminsize = 10
##enemyminsize = 40
##enemyminspeed = 1
##enemymaxspeed = 8
##enemyspawnrate = 6
##
##powerupspawnrate = 0

##playerx_speed = 0
##playery_speed = 0

x_coord = 350
y_coord = 490

x_speed = 0
y_speed = 0



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
    
enemy_group = pygame.sprite.Group()
#List of all sprites
all_sprites_group = pygame.sprite.Group()

enemynumber = 25
for x in range (enemynumber):
    my_enemy = Enemy(BLACK, 10, 10, 5)
    enemy_group.add(my_enemy)
    all_sprites_group.add (my_enemy)

my_evader = Evader(RED, 10, 10)
all_sprites_group.add (my_evader)


##def update(self):
##    self.rect.y = self.rect.y + self.speed


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

            
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT):
                x_speed=0
            if (event.key == pygame.K_RIGHT):
                x_speed=0
            if (event.key == pygame.K_UP):
                y_speed=0
            if (event.key == pygame.K_DOWN):
                y_speed=0       

    # --- Game logic should go here
    all_sprites_group.update()
    my_evader.x_speed=x_speed
    my_evader.y_speed=y_speed
    evader_hit_group = pygame.sprite.spritecollide(Evader, my_enemy, True)
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)
 
    # --- Drawing code should go here
    #pygame.draw.rect(screen, BLACK, [x_coord,y_coord,10,10])
    all_sprites_group.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second 
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

##playerx_speed = 0
##playery_speed = 0
##
##
##
##def move(self):
##
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                playerx_speed = -3
##            if event.key == pygame.K_RIGHT:
##                playerx_speed = 3
##            if event.ket == pygame.K_UP:
##                playery_speed = 3
##            if event.key == pygame.K_DOWN:
##                playery_speed = -3
##
##            
##        if event.type == pygame.KEYUP:
##            if event.key == pygame.K_LEFT:
##                playerx_speed=0
##            if event.key == pygame.K_RIGHT:
##                playerx_speed=0
##            if event.key == pygame.K_UP:
##                playery_speed = 0
##            if event.key == pygame.K_DOWN:
##                playery_speed = 0 
