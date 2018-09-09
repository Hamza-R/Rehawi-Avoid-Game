import pygame 
from pygame.locals import *

#Defining some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BackgroundColour = (255, 255, 255)

pygame.init()

#Setting width and height of screen
Size = (700, 500)
screen = pygame.display.set_mode(Size)

FPS = 30

pygame.display.set_caption("My Game")
#Set the mouse cursor to invisble so it doesn't get in the way of the game
pygame.mouse.set_visible(False)

#Continuously run until the user clicks the close button
done = False

#Manage speed of screen updates
clock = pygame.time.Clock()

#Setting up of constants

enemyminsize = 10
enemyminsize = 40
enemyminspeed = 1
enemymaxspeed = 8
enemyspawnrate = 6

playerx_speed = 0
playery_speed = 0



def move(self):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_speed = -3
            if event.key == pygame.K_RIGHT:
                playerx_speed = 3
            if event.ket == pygame.K_UP:
                playery_speed = 3
            if event.key == pygame.K_DOWN:
                playery_speed = -3

            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerx_speed=0
            if event.key == pygame.K_RIGHT:
                playerx_speed=0
            if event.key == pygame.K_UP:
                playery_speed = 0
            if event.key == pygame.K_DOWN:
                playery_speed = 0

                                 
