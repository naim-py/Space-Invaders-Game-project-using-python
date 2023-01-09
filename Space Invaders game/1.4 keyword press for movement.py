import pygame
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

def player(x,y):
    screen.blit(playerIm,(x,y))


running = True
while running:
    screen.fill((0,0,150))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #keyword strock for movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = .1


    # 5 = 5+ -.1 => 5 =5 -.1
    # 5= 5 + .1
    playerx += playerx_change

    #border
    if playerx <=0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    player(playerx,playery)
    pygame.display.update()