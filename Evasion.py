import pygame 
from pygame.locals import *
import random
import math
import time

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

POWERUP_SECONDS = 10

score = 0
my_evader_shield = None
enemy_group = pygame.sprite.Group()
pygame.init()

def main():

    f = open("highscore.txt","rt")
    data = f.read()
    ingameHS = int(data)
    f.close()
    
    #Setting width and height of screen
    Size = (700, 500)
    screen = pygame.display.set_mode(Size)

    FPS = 60
    mainmenu = True
    
    #Help screen which can ba accessed on main menu
    def Help():
        
        
        print("entering help")
        screen.fill(BLACK)
        drawText("Help", font, screen, (340), (10))
        
        drawText("The aim of the game is to dodge the enemies and survive for as", font, screen, (10), (60))
        drawText("long as possible.You can do this in multiple ways.", font, screen, (10), (80))
        drawText("To move use the arrow keys.You can move in any direction", font, screen, (10), (100))
        drawText("you desire. The player also can collect power ups,", font, screen, (10), (120))
        drawText("these powerups will help you survive.There are four different", font, screen, (10), (140))
        drawText("powerups: A coin that gives you an extra fifty score,", font, screen, (10), (160))
        drawText("a powerup that will increase your speed for a limited time,", font, screen, (10), (180))
        drawText("an ammo refill, to shoot when you have ammo press the spacebar, and", font, screen, (10), (200))
        drawText("a shield powerup that will destroy any enemies that collide with it", font, screen, (10), (220))
        drawText("preventing you from dying", font, screen, (10), (240))        
        
        drawText("Press m to return to the Main Menu", font , screen, (270), (430))
        drawText('Press p to Play', font, screen, (270) , (450) ) #X pos/Y pos of rest text
        drawText('Press s for High Score', font, screen, (270) , (470) )
        pygame.display.update()

       

    #Highscores screen which can be accessed on main menu
    def Highscore():

        print("entering Score")
        screen.fill(BLACK)
        drawText("Highest Score", font, screen,(270), (10))
        HS = "HighScore %s" %(ingameHS)
        drawText(HS, font , screen, (270), (230))
        drawText("Press m to return to the Main Menu", font , screen, (270), (430))
        drawText('Press p to Play', font, screen, (270) , (450) ) #X pos/Y pos of rest text
        drawText('Press h for Help', font, screen, (270) , (470) )
        pygame.display.update()


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
                if event.type == KEYUP:
                    #Before checking for any key event. Still do this but then check key pressed was spacebar
                    if (event.key == pygame.K_p):
                        done = True
                        return
                    elif (event.key == pygame.K_h):
                        Help()
                    elif (event.key == pygame.K_s):
                        Highscore()
                    elif (event.key == pygame.K_m):
                        main()
                        

    #Method that resets the game and its feature's when you press R to play again
    def Reset():
        if True:
                    my_evader.gameover = False
                    my_evader.ammo = 10
                    my_evader.rect.x = 345
                    my_evader.rect.y = 490
                    my_evader.behaviour = EvaderBehaviour()
                    my_evader.sheild = None
                    current_powerup  = None




    class Enemy(pygame.sprite.Sprite):

        def __init__(self, color, width, height, speed):
            super().__init__()
##            print("I was created")
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

    class EvaderBehaviour():
        """
        Our default evader behaviour
        """
        
        def __init__(self):
            self.speed = 1
        
        def is_expired(self):
            #Default behaviour never expires
            return False

    class SpeedUpBehaviour(EvaderBehaviour):
        """
        Our speed powerup
        """
        
        def __init__(self):
            self.speed = 2
            self.started = time.time()
        
        def is_expired(self):
            active_period = time.time() - self.started
            return active_period > POWERUP_SECONDS

    class ShieldUpBehaviour(EvaderBehaviour):
        """
        Our Shield Up powerup
        """
        def __init__(self):
            self.started = time.time()
            self.speed = my_evader.behaviour.speed
            
        def is_expired(self):
            active_period = time.time() - self.started
            return active_period > POWERUP_SECONDS         


    ##Shield Sprite
    class Shield(pygame.sprite.Sprite):
        def __init__ (self, color, width, height, enemy_group):
            super().__init__()

            self.started = time.time()
            self.image = pygame.Surface([width,height])
            self.image.fill(color)
            self.enemy_grp = enemy_group

            print("Shield",enemy_group, self.enemy_grp)
            #for images
            #asurf = pygame.image.load(os.path.join('data', 'bla.png'))
            #self.image = assurf

            self.rect = self.image.get_rect()
            self.x_speed = 0
            self.y_speed = 0
            self.rect.x = my_evader.rect.x + (x_speed * my_evader.behaviour.speed) -10
            self.rect.y = (my_evader.rect.y +(y_speed * my_evader.behaviour.speed))-15
            self.active = False
            #self.behaviour = EvaderBehaviour()


            
        def get_X(self):
             return self.rect.x

        def update(self):
                
                
            #print("Shield Update",self.rect.x,self.rect.y )
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.y < 0:
                self.rect.y = 0
            elif self.rect.x > 690:
                self.rect.x = 690
            elif self.rect.y > 490:
                self.rect.y = 490
            else:
                self.rect.x = self.rect.x + (x_speed * my_evader.behaviour.speed)
                self.rect.y = self.rect.y +(y_speed * my_evader.behaviour.speed) 

            col=sprite_collide_list = pygame.sprite.spritecollide(self, self.enemy_grp, True)

            for y in col:
            # Draw rects around the collided enemies.
                print("print collide: new enemy created")
                ##CREATE NEW ENEMY
                my_enemy = Enemy(BLACK, 10, 10, 1)
                enemy_group.add(my_enemy)
                all_sprites_group.add (my_enemy)

            
            if col == True:
                print("Shield Protect")
                self.gameover = False
                ##CREATE NEW ENEMY
                my_enemy = Enemy(BLACK, 10, 10, 1)
                enemy_group.add(my_enemy)
                all_sprites_group.add (my_enemy)
                

                
##            sprite_collide_list = pygame.sprite.spritecollide(self, self.enemy_grp, False)
##            for x in sprite_collide_list:              
##                self.gameover = True

            def is_expired(self):
                active_period = time.time() - self.started
                return active_period > POWERUP_SECONDS

        
    class Evader(pygame.sprite.Sprite):

        def __init__ (self, color, width, height, ammo, gameover, enemy_group, Power_up_Bullet):
            super().__init__()
            
            self.image = pygame.Surface([width,height])
            self.image.fill(color)
            #for images
            #asurf = pygame.image.load(os.path.join('data', 'bla.png'))
            #self.image = assurf

            self.rect = self.image.get_rect()
            self.x_speed = 0
            self.y_speed = 0
            self.rect.x = 345
            self.rect.y = 490
            self.ammo = 10
            self.enemy_grp = enemy_group
            self.gameover = gameover
            self.Power_up_Bullet = Power_up_Bullet
            self.behaviour = EvaderBehaviour()

        def get_X(self):
             return self.rect.x

        def update(self):

            if self.behaviour.is_expired():
                #Reset to default behaviour if expired
                print("Back to basics")
                self.behaviour = EvaderBehaviour()
                global my_evader_shield
                if my_evader_shield:
                    my_evader_shield.kill()
                    my_evader_shield = None
                    

            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.y < 0:
                self.rect.y = 0
            elif self.rect.x > 690:
                self.rect.x = 690
            elif self.rect.y > 490:
                self.rect.y = 490
            else:
                self.rect.x = self.rect.x + (x_speed * self.behaviour.speed)
                self.rect.y = self.rect.y + (y_speed * self.behaviour.speed)

            

            sprite_collide_list = pygame.sprite.spritecollide(self, self.enemy_grp, False)
            for x in sprite_collide_list:              
                self.gameover = True


            sprite_collide_list = pygame.sprite.spritecollide(self, power_up_group, True)
            for x in sprite_collide_list:   
                if type(x) is Power_up_Bullet:
                    my_evader.ammo += 10


                x.apply_power(self)
                print(sprite_collide_list)

        def shoot_bullet(self):
            if spacebar == True and my_evader.gameover == False:

                my_bullet = Bullet (PINK, 5, 5, 5, my_evader.rect.x +2.5, my_evader.rect.y, enemy_group)
                all_sprites_group.add(my_bullet)
                
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
            print("Score ")


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
            self.PowerUpType = ""
            self.started_at = time.time()

        def is_expired(self):
            # Just keep track how long something has lived for
            return time.time() - self.started_at > POWERUP_SECONDS
        
    class Power_up_coins(Power_up):

        def __init__(self, color, width, height):
            super().__init__(color, width, height)

        def apply_power(self, evader):
            print("50 Score Applied")
            global score
            score += 50
            print ("score " ,score)
            return score

    class Power_up_Bullet(Power_up):
        
        def __init__(self, color, width, height):
            super().__init__(color, width, height) 

        def apply_power(self, evader):
            pass        
        
    class Power_up_Speed(Power_up):
        def __init__(self, color, width, height):
            super().__init__(color, width, height)

        def apply_power(self, evader):
            print("SPEED APPLIED")
            evader.behaviour = SpeedUpBehaviour()

    class Power_up_Shield(Power_up):
        def __init__(self, color, width, height):
            super().__init__(color, width, height)

        def apply_power(self, evader):
        ##Add Evader Shield
            print("SHIELD APPLIED")
            global my_evader_shield
            global enemy_group
            if not my_evader_shield:
                my_evader_shield = Shield(BLUE, 30, 4,enemy_group)
                all_sprites_group.add (my_evader_shield)
                evader_group.add(my_evader_shield)
                
            evader.behaviour = ShieldUpBehaviour()



    def create_powerup():
        #change to (1, 8) if you want only 50% chance of powerup appearing.
        rand = random.randint(1, 4)
        #rand = 4
        powerup = None
        if rand == 1:
            powerup = Power_up_Bullet(PINK, 7, 7)
        elif rand == 2:
            powerup = Power_up_coins(GOLD, 7, 7)
        elif rand == 3:
            powerup = Power_up_Speed(GREEN, 7 ,7)
        elif rand == 4:
            powerup = Power_up_Shield(BLUE, 7, 7)        
        return powerup


    #Text for main menu of game
    if mainmenu == True:
        drawText('Evasion', font, screen, (345), (250) ) # X pos/Y pos of Evasion text
        drawText('Press p to Play', font, screen, (345) , (270) ) #X pos/Y pos of rest text
        drawText('Press s for High Score', font, screen, (345) , (290) )
        drawText('Press h for Help', font, screen, (345) , (310) )
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

    global score
 
    power_up_group = pygame.sprite.Group()

    evader_group =pygame.sprite.Group()        

    

    #List of all sprites
    all_sprites_group = pygame.sprite.Group()

    
    enemy_number = 15
    for x in range (enemy_number):
        my_enemy = Enemy(BLACK, 10, 10, 1)
        enemy_group.add(my_enemy)
        all_sprites_group.add (my_enemy)

    my_evader = Evader(RED, 10, 10, 10, False, enemy_group, Power_up_Bullet)
    all_sprites_group.add (my_evader)
    evader_group.add(my_evader)
    done = False
                     
    # -------- Main Program Loop -----------
    time_started = time.time()
    last_minute = 0
    handle_spacebar = False
    counter = 5

    current_powerup = None
    while not done:
        elapsed_seconds = time.time() - time_started
        current_minute = elapsed_seconds // 60

        if current_minute > last_minute:
            counter = counter * current_minute
            counter = int(counter)

            print("Counter" , counter)
            for x in range(counter):
                my_enemy = Enemy(BLACK, 10, 10, current_minute)
                enemy_group.add(my_enemy)
                all_sprites_group.add (my_enemy)
                last_minute = current_minute

        if current_powerup:
            #Check if powerup needs to be killed
            if current_powerup.is_expired():
                current_powerup.kill()
                current_powerup = None 
        else:
            current_powerup = create_powerup()
            power_up_group.add(current_powerup)
            all_sprites_group.add(current_powerup)     

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
                    handle_spacebar = True
                   

             
        # --- Game logic should go here
        
        all_sprites_group.update()
        my_evader.x_speed=x_speed
        my_evader.y_speed=y_speed

        ### Shield
        if my_evader_shield:
            all_sprites_group.update()
            my_evader_shield.x_speed=x_speed
            my_evader_shield.y_speed=y_speed


        if my_evader.gameover == False:
            score = score + 1
        else:
            score = score + 0


            
        # --- Screen-clearing code goes here
     
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
     
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(DBLUE)
     
        # --- Drawing code should go here
        
        if my_evader.gameover == True:
            screen.fill(BLACK)
            drawText("GAME OVER", font, screen,(270), (10))
            aScore = "Score: %s" %(score)
            drawText(aScore, font, screen, (270), (230))
            drawText("Press m to return to the main menu", font, screen, (270), (450))
            drawText("Press r to play again", font, screen, (270), (470))
            

            highscore = int(data)
            if score > highscore:
                highscore = score
                data = str(highscore)
                f = open("highscore.txt","wt")
                f.write(data)
                f.close()
            hs = "HighScore %s" %(highscore)
            drawText(hs, font , screen, (270),(250) )

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_m):
                    score = 0
                    main()

                if (event.key == pygame.K_r):
                    score = 0
                    Reset()
            
            
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


main()
