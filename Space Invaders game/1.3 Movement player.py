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

def player(x,y):
    screen.blit(playerIm,(x,y))


running = True
while running:
    screen.fill((0,0,150))
    #movement
    playerx -= .5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    player(playerx,playery)
    pygame.display.update()