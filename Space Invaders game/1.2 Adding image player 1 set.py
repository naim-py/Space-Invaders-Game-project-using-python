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

def player():
    screen.blit(playerIm,(playerx,playery))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,150))

    player()
    pygame.display.update()