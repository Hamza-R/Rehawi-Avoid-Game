import pygame 
from pygame.locals import *

#Defining some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


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

powerupspawnrate = 0

##playerx_speed = 0
##playery_speed = 0

x_coord = 350
y_coord = 490




##def move(self):
##
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                x_coord = x_coord - 3
##            if event.key == pygame.K_RIGHT:
##                x_coord = x_coord + 3
##            if event.ket == pygame.K_UP:
##                y_coord = y_coord - 5
##            if event.key == pygame.K_DOWN:
##                y_coord = y_coord + 5
##
##            
##        if event.type == pygame.KEYUP:
##            if event.key == pygame.K_LEFT:
##                x_coord = x_coord + 0
##            if event.key == pygame.K_RIGHT:
##                x_coord = x_coord + 0
##            if event.key == pygame.K_UP:
##                y_coord = y_coord + 0
##            if event.key == pygame.K_DOWN:
##                y_coord = y_coord + 0        

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT):
                x_coord = x_coord - 3
            if (event.key == pygame.K_RIGHT):
                x_coord = x_coord + 3
            if (event.key == pygame.K_UP):
                y_coord = y_coord - 5
            if (event.key == pygame.K_DOWN):
                y_coord = y_coord + 5

            
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT):
                x_coord = x_coord + 0
            if (event.key == pygame.K_RIGHT):
                x_coord = x_coord + 0
            if (event.key == pygame.K_UP):
                y_coord = y_coord + 0
            if (event.key == pygame.K_DOWN):
                y_coord = y_coord + 0        

    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, BLACK, [x_coord,y_coord,10,10])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
