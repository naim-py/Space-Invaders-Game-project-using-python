import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
#caption
pygame.display.set_caption("Space Invaders")
#icon
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,150))
    pygame.display.update()