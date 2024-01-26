import pygame
import math
from settings import *
from util import *
from boss import bossBullet
import random
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,size,speed,screen,path):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.path = path
        self.pathCount = 1
        self.screen = screen

    def move(self):
        xDif = self.path[self.pathCount][0] - self.x
        yDif = self.path[self.pathCount][1] - self.y

        if xDif < 0:
            self.x -= min(self.speed,abs(xDif))
        elif xDif > 0:
            self.x += min(self.speed,abs(xDif))
        if yDif < 0:
            self.y -= min(self.speed,abs(yDif))
        elif yDif > 0:
            self.y += min(self.speed,abs(yDif))

        if xDif == 0 and yDif == 0:
            if self.pathCount < len(self.path) - 1:
                self.pathCount += 1
            else:
                self.pathCount = 0

    def draw(self):
        self.move()
        pygame.draw.circle(self.screen,"#f1c40f",(self.x,self.y),self.size)

class Chaser(pygame.sprite.Sprite):
    def __init__(self,x,y,size,speed,screen):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.screen = screen
        self.angle = 0
        self.moveDistance = 15

    def getAngle(self,playerPos):
        self.speed = .2
        xDif = self.x - playerPos[0]
        yDif = self.y - playerPos[1]
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
        if playerPos[1] > HEIGHT - TILESIZE:
            self.speed = .5
            xDif = self.x - (WIDTH - TILESIZE - TILESIZE / 2)
            yDif = self.y - TILESIZE
            if yDif != 0:
                tempAngle = math.atan(xDif / yDif)
                angle = math.degrees(tempAngle)
                if yDif < 0:
                    angle += 180
                self.angle = angle
            else:
                if xDif > 0:
                    self.angle = 90
                else:
                    self.angle = -90
    def move(self):
        angle = math.radians(self.angle)
        xmove = math.sin(angle) * 15
        ymove = math.cos(angle) * 15
        if self.x - xmove * self.speed < WIDTH - TILESIZE and self.y - ymove * self.speed > TILESIZE:
            self.x -= xmove * self.speed
            self.y -= ymove * self.speed

    def draw(self):
        self.move()
        pygame.draw.circle(self.screen,"#f1c40f",(self.x,self.y),self.size)

class Spinner(pygame.sprite.Sprite):
    def __init__(self,x,y,center,size,speed,distance,screen,startAngle):
        super().__init__()
        self.x = x
        self.y = y
        self.center = center
        self.distance = distance
        self.size = size
        self.speed = speed
        self.screen = screen
        self.angle = startAngle
        self.moveDistance = 15

    def getAngle(self):
        xDif = self.x - self.center[0]
        yDif = self.y - self.center[1]
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

    def move(self):

        angle = math.radians(self.angle)
        xmove = math.sin(angle) * self.distance
        ymove = math.cos(angle) * self.distance
        self.x = self.center[0] + xmove
        self.y = self.center[1] + ymove

    def draw(self):
        self.move()
        self.angle += self.speed
        pygame.draw.circle(self.screen,"#f1c40f",(self.x,self.y),self.size)
        pygame.draw.circle(self.screen,"#f1c40f",(self.center),self.size)

class MiniBoss(pygame.sprite.Sprite):
    def __init__(self,x,y,screen,size,bossBulletGroup,player,ability):
        super().__init__()
        self.size = size
        self.screen = screen
        self.angle = 180
        self.surface = pygame.image.load("graphics/bossImage.png").convert_alpha()
        self.rect = self.surface.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.bossBulletGroup = bossBulletGroup
        self.player = player
        self.ability = ability
        self.abilityTimer = 0
    def getAngle(self,playerPos):
        if self.ability == "shoots":
            if self.abilityTimer % 50 == 0:
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
        elif self.ability == "danmaku":
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

    def draw(self):
        if self.alive:
            self.ablilites()

        for bullet in self.bossBulletGroup:
            bullet.draw()
            self.player.collide((bullet.x,bullet.y),bullet.size)
        rotateCenter(self.screen,self.surface,self.rect.topleft,self.angle)


    def ablilites(self):
        if self.ability == "shoots":
                self.abilityTimer += 1
                if self.abilityTimer % 50 > 30:
                    self.bossBulletGroup.add(bossBullet(self.rect.centerx, self.rect.centery, 5, self.angle, 15,self.screen))
                    if self.abilityTimer % 50 == 0:
                        self.getAngle((self.player.x, self.player.y))
                        self.angle += random.randint(-50,50)

        elif self.ability == "danmaku":
                self.abilityTimer += 1
                if self.abilityTimer % 10 == 0:
                    self.bossBulletGroup.add(bossBullet(self.rect.centerx, self.rect.centery, 3, self.angle + random.randint(-50,+50), 15, self.screen))

class Bouncer(pygame.sprite.Sprite):
    def __init__(self,x,y,screen,size,speed,angle):
        super().__init__()
        self.size = size
        self.screen = screen
        self.angle = angle
        self.x = x
        self.y = y
        self.speedx = speed
        self.speedy = speed
        self.moveDistance = 15

    def draw(self):
        self.move()
        self.bounce()
        pygame.draw.circle(self.screen,"#f1c40f",(self.x,self.y),self.size)

    def bounce(self):
        if (self.x - self.size <= TILESIZE or self.x + self.size >= WIDTH - TILESIZE):
            self.speedx *= -1
        elif (self.y - self.size <= TILESIZE or self.y + self.size >= HEIGHT - TILESIZE):
            self.speedy *= -1
    def move(self):
        angle = math.radians(self.angle)
        xmove = math.sin(angle) * self.moveDistance
        ymove = math.cos(angle) * self.moveDistance
        self.x -= xmove * self.speedx / 5
        self.y -= ymove * self.speedy / 5
