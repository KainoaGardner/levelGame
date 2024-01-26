import pygame
from settings import *
from levels import *
from player import Player
from enemy import Enemy
from boss import *


screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
#

def displayMainMenu(screen):
    screen.blit(mainMenuImage,(0,0))
    pygame.display.update()

def displayLevel(level):
    for row in range(len(level)):
        for col in range(len(level[row])):
            if level[row][col] == 0:
                pygame.draw.rect(screen,"#ecf0f1",pygame.Rect(col*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
            elif level[row][col] == 1:
                pygame.draw.rect(screen,"#7f8c8d",pygame.Rect(col*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
            elif level[row][col] == 3:
                pygame.draw.rect(screen,"#3498db",pygame.Rect(col*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
            elif level[row][col] == 4:
                pygame.draw.rect(screen,"#2ecc71",pygame.Rect(col*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))

level = []
for lev in ["level1", "level2", "level3","level4","level5","level6", "level7", "level8","level9","level10","level11"]:
    level.append(createLevel(lev))

levelCount = 0
player = Player(screen, level,levelCount,(25,HEIGHT//2))
enemyGroup = pygame.sprite.Group()
bossGroup = pygame.sprite.Group()
bossBulletGroup = pygame.sprite.Group()
chaserGroup = pygame.sprite.Group()
spinnerGroup = pygame.sprite.Group()
miniBossGroup = pygame.sprite.Group()
bouncerGroup = pygame.sprite.Group()

def display():
    for enemy in enemyGroup:
        enemy.draw()
        player.collide((enemy.x,enemy.y),enemy.size)
    for boss in bossGroup:
        boss.draw()
        boss.openGate(level)
    for chaser in chaserGroup:
        chaser.getAngle((player.x,player.y))
        chaser.draw()
        player.collide((chaser.x,chaser.y),chaser.size)
    for spinner in spinnerGroup:
        spinner.draw()
        player.collide((spinner.x, spinner.y), spinner.size)
    for miniBoss in miniBossGroup:
        miniBoss.getAngle((player.x,player.y))
        miniBoss.draw()
    for bouncer in bouncerGroup:
        bouncer.draw()
        player.collide((bouncer.x, bouncer.y), bouncer.size)

    player.update()


def main(level):
    mainMenu = True
    while mainMenu:
        displayMainMenu(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainMenu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mainMenu = False
    else:
        run = True
        levelCount = 0
        time = 0
        resetTime = 0
        menu = False
        scoreBoard = []
        setupLevel(levelCount,enemyGroup,bossGroup,screen,player,bossBulletGroup,chaserGroup,spinnerGroup,miniBossGroup,bouncerGroup)
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and levelCount == 10:
                        levelCount = 0
                        menu = False
                        level[9][0][9] = 1
                        level[9][0][10] = 1
                        setupLevel(levelCount,enemyGroup,bossGroup,screen,player,bossBulletGroup,chaserGroup,spinnerGroup,miniBossGroup,bouncerGroup)
                        resetTime = pygame.time.get_ticks()


            if player.checkGoal():
                levelCount += 1
                setupLevel(levelCount,enemyGroup,bossGroup,screen,player,bossBulletGroup,chaserGroup,spinnerGroup,miniBossGroup,bouncerGroup)

            displayLevel(level[levelCount])
            displayLevelCount(screen, levelCount)

            if levelCount != 10 and not (levelCount == 0 and player.x < TILESIZE * 2):
                time = pygame.time.get_ticks() - resetTime
            if (levelCount == 0 and player.x < TILESIZE * 2):
                resetTime = pygame.time.get_ticks()
                time = 0


            displayDeathCount(screen,player.deaths)
            displayTimeScore(screen, time)
            display()

            if levelCount == 10:
                displayWin(screen)
                displayScoreBoard(screen,scoreBoard)

            if levelCount == 10 and menu == False:
                scoreBoard = addScoreBoard(scoreBoard,time)
                menu = True




            pygame.display.update()
            clock.tick(FPS)

    pygame.quit()

main(level)
