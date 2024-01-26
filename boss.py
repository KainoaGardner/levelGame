import pygame
import math
import random
from settings import *
from util import rotateCenter

pygame.init()


class Boss(pygame.sprite.Sprite):
    def __init__(self,screen,size,bossBulletGroup,player):
        super().__init__()
        self.size = size
        self.screen = screen
        self.angle = 180
        self.surface = pygame.image.load("graphics/bossImage1.png").convert_alpha()
        self.rect = self.surface.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2
        self.bossTimer = pygame.time.get_ticks()
        self.timer = pygame.time.get_ticks()
        self.time = 60
        self.bossBulletGroup = bossBulletGroup
        self.player = player
        self.alive = True
        self.explosionCounter = 0


        self.ability = False
        self.abilityTimer = 0
        self.spin = False
        self.direction = 0
        self.beam = False
        self.xbeam1 = self.rect.centery
        self.xbeam2 = self.rect.centery
        self.danmaku = False
        self.right = False
        self.shoots = False
        self.chase = False
        self.chase2 = False


    def getAngle(self,playerPos):
        xDif = self.rect.centerx - playerPos[0]
        yDif = self.rect.centery - playerPos[1]
        if yDif != 0:
            tempAngle = math.atan(xDif/yDif)
            angle = math.degrees(tempAngle)
            if yDif < 0:
                angle += 180
            self.angle = angle
        else:
            if xDif > 0:
                self.angle = 90
            else:
                self.angle = -90

    def openGate(self,level):
        if (60 - ((self.timer - self.bossTimer)) // 1000) <= 0:
            self.alive = False
            self.ability = True
            self.bossBulletGroup.empty()
            if self.angle >= 5000:
                self.kill()
                pygame.mixer.Sound.play(explosionSound)
                level[9][0][9] = 4
                level[9][0][10] = 4
            return level

    def draw(self):
        if self.alive == False:
            self.death()
        self.ablilites()
        key = pygame.key.get_pressed()

        for bullet in self.bossBulletGroup:
            bullet.draw()
            self.player.collide((bullet.x,bullet.y),bullet.size)

        rotateCenter(self.screen,self.surface,self.rect.topleft,self.angle)
        self.drawTimer()


    def drawTimer(self):
        if (60 - ((self.timer - self.bossTimer)) // 1000) > 0:
            if self.player.y > HEIGHT - TILESIZE:
                self.bossTimer = pygame.time.get_ticks()
                self.timer = pygame.time.get_ticks()
            self.timer = pygame.time.get_ticks()
            time = bigFont.render(str(60 - ((self.timer - self.bossTimer)) // 1000),True,"White")
            timeRect = time.get_rect(center = self.rect.center)
            self.screen.blit(time,timeRect)

    def ablilites(self):
        if self.alive:
            if self.ability == False:
                self.abilityTimer += 1
                if self.abilityTimer > 50:
                    self.ability = True
                    self.abilityTimer = 0
                    choice = random.randint(0,5)
                    self.bossBulletGroup.empty()
                    match choice:
                        case 0:
                            self.spin = True
                            self.direction = random.choice([-1,1])
                        case 1:
                            self.beam = True
                            self.xbeam = self.rect.centerx
                        case 2:self.danmaku = True
                        case 3:self.shoots = True
                        case 4:
                            self.chase = True
                            self.getAngle((self.player.x, self.player.y))
                        case 5:
                            self.chase2 = True
                            self.getAngle((self.player.x, self.player.y))


            if self.spin:
                if self.rect.centery < HEIGHT // 2:
                    self.rect.centery += min(5,HEIGHT//2 - self.rect.centery)
                if self.rect.centery > HEIGHT // 2:
                    self.rect.centery -= min(5,self.rect.centery - HEIGHT//2)
                if self.rect.centerx < WIDTH // 2:
                    self.rect.centerx += min(5, WIDTH // 2 - self.rect.centerx)
                if self.rect.centerx > WIDTH // 2:
                    self.rect.centerx -= min(5, self.rect.centerx - WIDTH // 2)

                if WIDTH // 2 - 25 <= self.rect.centerx <= WIDTH // 2 + 25 and HEIGHT // 2 - 25 <= self.rect.centery <= HEIGHT // 2 + 25:
                    self.rect.centerx = WIDTH // 2
                    self.rect.centery = HEIGHT // 2

                if self.rect.centerx == WIDTH // 2 and self.rect.centery == HEIGHT // 2:

                    self.abilityTimer += 1
                    if self.ability < 50:
                        self.angle += 1 * self.direction
                    if 50 <= self.abilityTimer  and self.abilityTimer < 450:
                        self.angle += 1 * self.direction
                        self.bossBulletGroup.add(bossBullet(self.rect.centerx, self.rect.centery, 5, self.angle, 25, self.screen))
                    if 450 <= self.abilityTimer:
                        self.spin = False
                        self.ability = False
                        self.abilityTimer = 0
                    else:
                        self.angle += 1 * self.direction

            if self.beam:
                if self.abilityTimer > 700:
                    self.beam = False
                    self.ability = False
                    self.abilityTimer = 0

                if self.rect.centery > 50 + TILESIZE // 2:
                    self.angle = 180
                    self.rect.centery -= min(5,self.rect.centery - 50 + TILESIZE // 2)
                if self.rect.centerx < WIDTH // 2:
                    self.rect.centerx += min(5, WIDTH // 2 - self.rect.centerx)
                if self.rect.centerx > WIDTH // 2:
                    self.rect.centerx -= min(5, self.rect.centerx - WIDTH // 2)
                if WIDTH // 2 - 10 <= self.rect.centerx <= WIDTH // 2 + 10:
                    self.rect.centerx = WIDTH // 2

                if self.rect.centery <= 50 + TILESIZE // 2:
                    self.abilityTimer += 1

                    if self.abilityTimer % 100 < 50:
                        self.bossBulletGroup.add(bossBullet(self.xbeam1, self.rect.centery - 15, 10, 180, 25, self.screen))
                        self.bossBulletGroup.add(bossBullet(self.xbeam2, self.rect.centery - 15, 10, 180, 25, self.screen))
                    elif self.abilityTimer % 100 > 50:
                        self.bossBulletGroup.add(bossBullet(self.rect.centerx, self.rect.centery, 10, self.angle, 25, self.screen))

                    elif self.abilityTimer % 100 <= 50:
                        self.xbeam1 = random.randint(TILESIZE + 25, HEIGHT - TILESIZE - 25)
                        self.getAngle((self.player.x, self.player.y))
                        self.xbeam2 = random.randint(TILESIZE + 25, HEIGHT - TILESIZE - 25)

            if self.danmaku:
                if self.abilityTimer > 500:
                    self.danmaku = False
                    self.ability = False
                    self.abilityTimer = 0

                if self.rect.centery > 50 + TILESIZE // 2:
                    self.angle = 180
                    self.rect.centery -= min(5,self.rect.centery - 50 + TILESIZE // 2)
                else:
                    self.abilityTimer += 1
                    self.getAngle((self.player.x, self.player.y))
                    if self.right:
                        if self.rect.centerx < HEIGHT - TILESIZE:
                            self.rect.centerx += 2
                        else:
                            self.right = False
                    elif self.right == False:
                        if self.rect.centerx > TILESIZE:
                            self.rect.centerx -= 2
                        else:
                            self.right = True

                    if self.abilityTimer % 3 == 0:
                        self.bossBulletGroup.add(bossBullet(self.rect.centerx, self.rect.centery, 3, self.angle + random.randint(-25,+25), 15, self.screen))

            if self.shoots:
                if self.abilityTimer > 500:
                    self.shoots = False
                    self.ability = False
                    self.abilityTimer = 0

                if self.rect.centery < HEIGHT // 2:
                    self.rect.centery += min(5,HEIGHT//2 - self.rect.centery)
                if self.rect.centery > HEIGHT // 2:
                    self.rect.centery -= min(5,self.rect.centery - HEIGHT//2)
                if self.rect.centerx < WIDTH // 2:
                    self.rect.centerx += min(5, WIDTH // 2 - self.rect.centerx)
                if self.rect.centerx > WIDTH // 2:
                    self.rect.centerx -= min(5, self.rect.centerx - WIDTH // 2)
                if WIDTH // 2 - 10 <= self.rect.centerx <= WIDTH // 2 + 10 and HEIGHT // 2 - 10 <= self.rect.centery <= HEIGHT // 2 + 10:
                    self.rect.centerx = WIDTH // 2
                    self.rect.centery = HEIGHT // 2
                if self.rect.centerx == WIDTH // 2 and self.rect.centery == HEIGHT // 2:
                    self.abilityTimer += 1
                    if self.abilityTimer % 10 < 5:
                        self.bossBulletGroup.add(bossBullet(self.rect.centerx, self.rect.centery, 5, self.angle, 15,self.screen))
                    if self.abilityTimer % 10 == 9:
                        self.getAngle((self.player.x, self.player.y))
                        self.angle += random.randint(-50,50)

            if self.chase:
                if self.abilityTimer > 500:
                    self.chase = False
                    self.ability = False
                    self.abilityTimer = 0

                self.abilityTimer += 1

                if self.abilityTimer % 100 == 0:
                    self.getAngle((self.player.x, self.player.y))
                if self.abilityTimer % 100 < 80:
                    angle = math.radians(self.angle)
                    xmove = math.sin(angle) * 15
                    ymove = math.cos(angle) * 15
                    self.rect.centerx -= xmove * .8
                    self.rect.centery -= ymove * .8
                    if self.rect.centerx < TILESIZE:
                        self.rect.centerx = TILESIZE
                    elif self.rect.centerx > WIDTH - TILESIZE:
                        self.rect.centerx = WIDTH - TILESIZE
                    if self.rect.centery < TILESIZE:
                        self.rect.centery = TILESIZE
                    elif self.rect.centery > HEIGHT - TILESIZE:
                        self.rect.centery = HEIGHT - TILESIZE

                    self.bossBulletGroup.add(bossBullet(self.rect.centerx, self.rect.centery, 5, self.angle + 180, 15, self.screen))
                    self.bossBulletGroup.add(
                        bossBullet(self.rect.centerx, self.rect.centery, 10, self.angle + 150, 15, self.screen))
                    self.bossBulletGroup.add(
                        bossBullet(self.rect.centerx, self.rect.centery, 10, self.angle - 150, 15, self.screen))
                else:
                    self.getAngle((self.player.x, self.player.y))

            if self.chase2:
                if self.abilityTimer > 500:
                    self.chase2 = False
                    self.ability = False
                    self.abilityTimer = 0

                self.abilityTimer += 1
                self.getAngle((self.player.x, self.player.y))

                angle = math.radians(self.angle)
                xmove = math.sin(angle) * 15
                ymove = math.cos(angle) * 15
                self.rect.centerx -= xmove * .35
                self.rect.centery -= ymove * .35

                if self.rect.centerx < TILESIZE:
                    self.rect.centerx = TILESIZE
                elif self.rect.centerx > WIDTH - TILESIZE:
                    self.rect.centerx = WIDTH - TILESIZE
                if self.rect.centery < TILESIZE:
                    self.rect.centery = TILESIZE
                elif self.rect.centery > HEIGHT - TILESIZE:
                    self.rect.centery = HEIGHT - TILESIZE

                if self.abilityTimer % 5 == 0:
                    self.bossBulletGroup.add(bossBullet(self.rect.centerx, self.rect.centery, 1, self.angle + 180 + random.randint(-20,20), 15, self.screen))

    def death(self):
        if self.rect.centerx - self.size <= WIDTH // 2 <= self.rect.centerx + self.size and self.rect.centery - self.size <= HEIGHT // 2 <= self.rect.centery + self.size:
            if 0 <= self.angle < 3000:
                self.explosionCounter += .2
                self.angle += self.explosionCounter
            elif 3000 <= self.angle < 5000:
                self.angle += self.explosionCounter
                pygame.draw.circle(self.screen,"#f39c12",self.rect.center,self.angle % 3000 // 10)
            pygame.mixer.Sound.play(shootSound)
        else:
            if self.rect.centery < HEIGHT // 2:
                self.rect.centery += min(5, HEIGHT // 2 - self.rect.centery)
            if self.rect.centery > HEIGHT // 2:
                self.rect.centery -= min(5, self.rect.centery - HEIGHT // 2)
            if self.rect.centerx < WIDTH // 2:
                self.rect.centerx += min(5, WIDTH // 2 - self.rect.centerx)
            if self.rect.centerx > WIDTH // 2:
                self.rect.centerx -= min(5, self.rect.centerx - WIDTH // 2)
            if WIDTH // 2 - 10 <= self.rect.centerx <= WIDTH // 2 + 10 and HEIGHT // 2 - 10 <= self.rect.centery <= HEIGHT // 2 + 10:
                self.rect.centerx = WIDTH // 2
                self.rect.centery = HEIGHT // 2



class bossBullet(pygame.sprite.Sprite):
    def __init__(self,x,y,speed,angle,size,screen):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.moveDist = 10
        self.size = size
        self.screen = screen
        pygame.mixer.Sound.play(shootSound)

    def move(self):
        angle = math.radians(self.angle)
        xmove = math.sin(angle) * self.moveDist
        ymove = math.cos(angle) * self.moveDist
        self.x -= xmove * self.speed / 5
        self.y -= ymove * self.speed / 5


    def draw(self):
        self.move()
        pygame.draw.circle(self.screen,"#f1c40f",(self.x,self.y),self.size)

        if self.x < TILESIZE + self.size or self.x > WIDTH - TILESIZE - self.size or self.y < TILESIZE + self.size or self.y > HEIGHT - TILESIZE - self.size:
            self.kill()

