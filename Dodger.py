import pygame 
from pygame.locals import *

#Defining some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BackgroundColour = (255, 255, 255)

pygame.init()

#Setting width and height of screen
ScreenWidth = (700)
ScreenHeight = (500)
screen = pygame.display.set_mode(ScreenWidth, ScreenHeight)

FPS = 30

pygame.display.set_caption("My Game")
#Set the mouse cursor to invisble so it doesn't get in the way of the game
pygame.mouse.set_visible(False)

#Continuously run until the user clicks the close button
done = False

#Manage speed of screen updates
clock = pygame.time.Clock()


                                 
