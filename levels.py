from settings import *
from enemy import *
from boss import Boss
import random

def createLevel(level):
    with open(level, "r") as worldFile:
        text = worldFile.readlines()

    levelList = []
    for line in text:
        newLine = line.replace("\n", "")
        rowList = []
        for tile in newLine:
            rowList.append(int(tile))
        levelList.append(rowList)
    return levelList


def setupLevel(levelCount,enemyGroup,bossGroup,screen,player,bossBulletGroup,chaserGroup,spinnerGroup,miniBossGroup,bouncerGroup):
    enemyGroup.empty()
    player.levelCount = levelCount
    chaserGroup.empty()
    spinnerGroup.empty()
    miniBossGroup.empty()
    bossBulletGroup.empty()
    bouncerGroup.empty()
    player.goal = False
    if levelCount == 0:
        player.startPoint = (25,HEIGHT//2)
        player.x = player.startPoint[0]
        player.y = player.startPoint[1]
        for i in range(16):
            enemy = Enemy(TILESIZE * 2 + TILESIZE // 2 + TILESIZE * i, TILESIZE * 3 + TILESIZE // 2, 10,
                          3, screen, [(TILESIZE * 2 + TILESIZE // 2 + TILESIZE * i, TILESIZE * 3 + TILESIZE // 2),
                                      (TILESIZE * 2 + TILESIZE // 2 + TILESIZE * i, TILESIZE * 16 + TILESIZE // 2)])
            enemyGroup.add(enemy)

        for i in range(14):
            enemy = Enemy(TILESIZE * 2 + TILESIZE // 2, TILESIZE * 3 + TILESIZE // 2 + TILESIZE * i, 10,
                          3, screen, [(TILESIZE * 2 + TILESIZE // 2, TILESIZE * 3 + TILESIZE // 2 + TILESIZE * i),
                                      (TILESIZE * 16 + TILESIZE // 2 + TILESIZE, TILESIZE * 3 + TILESIZE // 2 + TILESIZE * i)])
            enemyGroup.add(enemy)




        for i in range(15):
            enemy = Enemy(TILESIZE * 3 + TILESIZE * i, TILESIZE * 16 + TILESIZE // 2, 10,
                          3, screen, [(TILESIZE * 3 + TILESIZE * i , TILESIZE * 16 + TILESIZE // 2),(TILESIZE * 3 + TILESIZE * i, TILESIZE * 3 + TILESIZE // 2)])
            enemyGroup.add(enemy)

        for i in range(13):
            enemy = Enemy(TILESIZE * 16 + TILESIZE + TILESIZE // 2, TILESIZE * 4 + TILESIZE * i, 10,
                          3, screen, [(TILESIZE * 16 + TILESIZE + TILESIZE // 2, TILESIZE * 4 + TILESIZE * i),(TILESIZE * 2 + TILESIZE // 2, TILESIZE * 4 + TILESIZE * i)])
            enemyGroup.add(enemy)



    elif levelCount == 1:
        player.startPoint = (25,HEIGHT//2)
        player.x = player.startPoint[0]
        player.y = player.startPoint[1]

        for i in range(31):
            enemy = Enemy(TILESIZE * 2 + (TILESIZE // 2) * i + TILESIZE // 2, TILESIZE * 3 + TILESIZE // 2, 10,
                          4.2, screen, [(TILESIZE * 2 + (TILESIZE // 2) * i + TILESIZE // 2, TILESIZE * 3 + TILESIZE // 2),
                                      (TILESIZE * 2 + (TILESIZE // 2) * i + TILESIZE // 2, TILESIZE * 16 + TILESIZE // 2)])
            enemyGroup.add(enemy)

    elif levelCount == 2:
        player.startPoint = (25,HEIGHT//2)
        player.x = player.startPoint[0]
        player.y = player.startPoint[1]

        for i in range(17):
            enemy = Enemy(TILESIZE * 1 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2 + TILESIZE * i, 10,
                          4, screen, [(TILESIZE * 1 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2),
                                      (TILESIZE * 1 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2),(TILESIZE * 3 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2),(TILESIZE * 3 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2)])
            enemyGroup.add(enemy)

        for i in range(17):
            enemy = Enemy(TILESIZE * 5 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2 + TILESIZE * i, 10,
                          9, screen, [(TILESIZE * 5 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2),
                                      (TILESIZE * 5 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2),(TILESIZE * 7 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2),(TILESIZE * 7 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2)])
            enemyGroup.add(enemy)

        for i in range(17):
            enemy = Enemy(TILESIZE * 9 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2 + TILESIZE * i, 10,
                          5, screen, [(TILESIZE * 9 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2),
                                      (TILESIZE * 9 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2),
                                      (TILESIZE * 11 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2),
                                      (TILESIZE * 11 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2)])
            enemyGroup.add(enemy)

        for i in range(17):
            enemy = Enemy(TILESIZE * 11 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2 - TILESIZE * i, 10,
                          5, screen, [(TILESIZE * 11 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2),
                                      (TILESIZE * 11 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2),
                                      (TILESIZE * 9 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2),
                                      (TILESIZE * 9 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2),
                                      ])
            enemyGroup.add(enemy)


        for i in range(18):
            enemy = Enemy(TILESIZE * 13 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2 + TILESIZE * i, 10,
                          5, screen, [(TILESIZE * 13 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2),
                                      (TILESIZE * 13 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2),
                                      (TILESIZE * 15 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2),
                                      (TILESIZE * 15 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2)])
            enemyGroup.add(enemy)

        for i in range(18):
            enemy = Enemy(TILESIZE * 15 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2 - TILESIZE * i, 10,
                          5, screen, [(TILESIZE * 15 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2),
                                      (TILESIZE * 15 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2),
                                      (TILESIZE * 13 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2),
                                      (TILESIZE * 13 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2),
                                      ])
            enemyGroup.add(enemy)

        for i in range(10):
            enemy = Enemy(TILESIZE * 17 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2 + TILESIZE * i, 10,
                          15, screen, [(TILESIZE * 17 + TILESIZE // 2, TILESIZE * 1 + TILESIZE // 2),
                                      (TILESIZE * 17 + TILESIZE // 2, TILESIZE * 18 + TILESIZE // 2)])

            enemyGroup.add(enemy)

    elif levelCount == 3:
        player.startPoint = (25, HEIGHT // 2)
        player.x = player.startPoint[0]
        player.y = player.startPoint[1]
        for i in range(18):
            enemy = Enemy(TILESIZE * 1 + TILESIZE // 2 + TILESIZE * i , TILESIZE * 9 + i * 10, 10,
                          5, screen, [(TILESIZE * 1 + TILESIZE // 2 + TILESIZE * i, TILESIZE * 9 + 10),
                                      (TILESIZE * 1 + TILESIZE // 2 + TILESIZE * i, TILESIZE * 11 - 10)])
            enemyGroup.add(enemy)

    elif levelCount == 4:
        player.startPoint = (25, TILESIZE * 2)
        player.x = player.startPoint[0]
        player.y = player.startPoint[1]
        for i in range(22):
            spinnerGroup.add(Spinner(WIDTH // 2,TILESIZE,(WIDTH//2,HEIGHT//2),10,-1.6,550 - i * 25,screen,0))
        for i in range(22):
            spinnerGroup.add(Spinner(WIDTH // 2,TILESIZE,(WIDTH//2,HEIGHT//2),10,-1.6,550 - i * 25,screen,180))

    elif levelCount == 5:
        player.startPoint = (TILESIZE // 2, TILESIZE * 2)
        player.x = player.startPoint[0]
        player.y = player.startPoint[1]

        enemy = Enemy(100 + TILESIZE, TILESIZE + 100, 100,
                      10, screen, [(100 + TILESIZE, TILESIZE + 100),(WIDTH - 100 - TILESIZE, TILESIZE + 100),(WIDTH - 100 - TILESIZE, HEIGHT - 100 - TILESIZE),(100 + TILESIZE, HEIGHT - 100 - TILESIZE),(100 * 2 + TILESIZE, TILESIZE + 100 * 2),(WIDTH - 100 * 2 - TILESIZE, TILESIZE + 100 * 2),(WIDTH - 100 * 2 - TILESIZE, HEIGHT - 100 * 2 - TILESIZE),(100 * 2 + TILESIZE, HEIGHT - 100 * 2 - TILESIZE),(100 * 3 + TILESIZE, TILESIZE + 100 * 3),(WIDTH - 100 * 3 - TILESIZE, TILESIZE + 100 * 3),(WIDTH - 100 * 3 - TILESIZE, HEIGHT - 100 * 3 - TILESIZE),(100 * 3 + TILESIZE, HEIGHT - 100 * 3 - TILESIZE),(WIDTH //2,HEIGHT //2)])
        enemyGroup.add(enemy)

    elif levelCount == 6:
        player.startPoint = (TILESIZE * 6, TILESIZE // 2)
        player.x = player.startPoint[0]
        player.y = player.startPoint[1]
        for _ in range(100):
            bouncer = Bouncer(random.randint(TILESIZE + 10,WIDTH - (TILESIZE + 10)),random.randint(TILESIZE + 10,HEIGHT - (TILESIZE + 10)),screen,10,1,random.randint(0,360))
            bouncerGroup.add(bouncer)




    elif levelCount == 7:
        player.startPoint = (TILESIZE + TILESIZE //2, HEIGHT - 25)
        player.x = player.startPoint[0]
        player.y = player.startPoint[1]
        chaserGroup.add(Chaser((WIDTH - TILESIZE - TILESIZE / 2),TILESIZE,25,.2,screen))

    elif levelCount == 8:
        for chaser in chaserGroup:
            chaser.kill()
        player.startPoint = (TILESIZE // 2,HEIGHT//2)
        player.x = player.startPoint[0]
        player.y = player.startPoint[1]
        miniBossGroup.add(MiniBoss(WIDTH - TILESIZE - TILESIZE // 2, TILESIZE * 3,screen,50,bossBulletGroup,player,"shoots"))
        miniBossGroup.add(MiniBoss(WIDTH - TILESIZE - TILESIZE // 2 , HEIGHT - TILESIZE * 3, screen, 50, bossBulletGroup, player, "danmaku"))

    elif levelCount == 9:
        player.startPoint = (WIDTH // 2, HEIGHT - 25)
        player.x = player.startPoint[0]
        player.y = player.startPoint[1]
        bossGroup.add(Boss(screen,75,bossBulletGroup,player))

    elif levelCount == 10:
        player.startPoint = (WIDTH // 2, HEIGHT // 2)
        player.x = player.startPoint[0]
        player.y = player.startPoint[1]

def addScoreBoard(scoreBoard,time):
    scoreBoard.append(time//1000)
    for _ in range(len(scoreBoard)):
        for i in range(len(scoreBoard) - 1):
            if scoreBoard[i] > scoreBoard[i + 1]:
                temp = scoreBoard[i]
                scoreBoard[i] = scoreBoard[i + 1]
                scoreBoard[i + 1] = temp
    if len(scoreBoard) > 5:
        del scoreBoard[4:-1]
    return scoreBoard





text = bigFont.render("YOU WIN!",True,"Black")
textRect = text.get_rect()
textRect.center = (WIDTH //2, HEIGHT // 2)

restart = font.render("Press R to Restart",True,"Black")
restartRect = text.get_rect()
restartRect.center = (WIDTH //2 - 30, HEIGHT // 2 + 50)


def displayWin(screen):
    screen.blit(text,textRect)
    screen.blit(restart, restartRect)


def displayLevelCount(screen,levelCount):
    levelText = font.render(f"Level: {levelCount + 1}",True,"White")
    levelTextRect = text.get_rect()
    levelTextRect = (TILESIZE/4,TILESIZE/4)
    screen.blit(levelText,levelTextRect)

def displayDeathCount(screen,deaths):
    deathText = font.render(f"Deaths: {deaths}",True,"White")
    deathTextRect = deathText.get_rect()
    deathTextRect.center = (WIDTH//2,TILESIZE / 2)
    screen.blit(deathText,deathTextRect)

def displayTimeScore(screen,time):
    timeText = font.render(f"Time: {time//1000}",True,"White")
    timeTextRect = timeText.get_rect()
    timeTextRect.center = (WIDTH - TILESIZE - TILESIZE / 2,TILESIZE/2)
    screen.blit(timeText,timeTextRect)

def displayScoreBoard(screen,scoreBoard):
    scoreBoardText = bigFont.render(f"ScoreBoard:",True,"Black")
    scoreBoardTextRect = scoreBoardText.get_rect()
    scoreBoardTextRect.center = (WIDTH //2, TILESIZE * 2)
    screen.blit(scoreBoardText,scoreBoardTextRect)
    for i in range(len(scoreBoard)):
        score = font.render(f"{i + 1}: {scoreBoard[i]}s", True, "Black")
        scoreRect = score.get_rect()
        scoreRect.center = (WIDTH //2, TILESIZE * 3 + TILESIZE * i)
        screen.blit(score, scoreRect)