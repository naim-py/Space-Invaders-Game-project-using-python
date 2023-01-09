import math
import pygame
import random
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load("background.png")

# Background sound
mixer.music.load("background.wav")
mixer.music.play(-1)

#caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#player
playerIm = pygame.image.load("player.png")
playerx = 370
playery = 500
playerx_change = 0

# Enemy
enemyIm = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6


for i in range(num_of_enemies):
    enemyIm.append(pygame.image.load("enemy.png"))
    enemyx.append(random.randint(0,800))      #370
    enemyy.append(random.randint(50,150))    #10
    enemyx_change.append(0.3)
    enemyy_change.append(40)

# Bullet
#ready = state means u cannot see the on the screen
# fire basically bullet is currently moving
bulletIm = pygame.image.load("bullet2.png")
bulletx = 0
bullety = 480
bulletx_change = 0
bulety_change = 2   # bullet speed
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)

textx = 10
texty = 10

# Game over text
over_font = pygame.font.Font("freesansbold.ttf",64)


def show_score(x,y):
    score = font.render("Score : " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


def game_over_text():
    over_text = over_font.render("Game Over",True,(255,255,255))
    screen.blit(over_text,(200,250))


def player(x,y):
    screen.blit(playerIm,(x,y))

def enemy(x,y,i):
    screen.blit(enemyIm[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIm,(x+16,y+10))


def iscollision( enemyx,enemyy , bulletx,bullety ):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy-bullety, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:
    screen.fill((0,0,150))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #keyword strock for movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.7
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.6
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    # Get the current x cordinates of the spaceship
                    bulletx = playerx
                    fire_bullet(bulletx,bullety)



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = .2


    # 5 = 5+ -.1 => 5 =5 -.1
    # 5= 5 + .1
    playerx += playerx_change
    #border for playerx
    if playerx <=0 :
        playerx = 0
    elif playerx >= 736 :
        playerx = 736

    #border for enemy Movement
    for i in range(num_of_enemies):

        # Game over
        if enemyy[i] > 440:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break

        enemyx[i]  += enemyx_change[i]
        if enemyx[i] <=0 :
            enemyx_change[i] = .3
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736 :
            enemyx_change[i]  = -.3
            enemyy[i] += enemyy_change[i]

        # Collision
        collision = iscollision(enemyx[i],enemyy[i], bulletx,bullety)
        if collision :
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bullety = 480
            bullet_state = 'ready'
            score_value += 1
            print(score_value)
            enemyx[i] = random.randint(0,736)      #370
            enemyy[i] = random.randint(50,150)

        enemy(enemyx[i],enemyy[i],i)

    # bullet movement
    if bullety <=0:
        bullety = 480
        bullet_state = 'ready'
    if bullet_state is "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bulety_change


    player(playerx,playery)
    show_score(textx,texty)
    pygame.display.update()

