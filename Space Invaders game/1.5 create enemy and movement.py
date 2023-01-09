import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
#caption
pygame.display.set_caption("Space Invaders")
#icon
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#player
playerIm = pygame.image.load("player.png")
playerIm = pygame.transform.scale(playerIm,(60,90))
playerx = 370
playery = 500
playerx_change = 0

# Enemy
enemyIm = pygame.image.load("spaceship.png")
enemyIm = pygame.transform.scale(enemyIm,(60,90))
enemyx = random.randint(0,800)      #370
enemyy = random.randint(10,10)     #10
enemyx_change = 0.3
enemyy_change = 40

def player(x,y):
    screen.blit(playerIm,(x,y))

def enemy(x,y):
    screen.blit(enemyIm,(x,y))

running = True
while running:
    screen.fill((0,0,150))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #keyword strock for movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.5

            if event.key == pygame.K_RIGHT:
                playerx_change = 0.5


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = .3


    # 5 = 5+ -.1 => 5 =5 -.1
    # 5= 5 + .1
    playerx += playerx_change
    #border for playerx
    if playerx <=0 :
        playerx = 0
    elif playerx >= 736 :
        playerx = 736

    #border for enemy
    enemyx  += enemyx_change
    if enemyx <=0 :
        enemyx_change = 0.3
        enemyy += enemyy_change
    elif enemyx >= 736 :
        enemyx_change  = -.3
        enemyy += enemyy_change

    player(playerx,playery)
    enemy(enemyx,enemyy)
    pygame.display.update()