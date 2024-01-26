import pygame
from settings import *
from boss import *
class Player():
    def __init__(self,screen,level,levelCount,startPoint):
        self.startPoint = startPoint
        self.x = startPoint[0]
        self.y = startPoint[1]
        self.radius = 15
        self.speed = 5
        self.screen = screen
        self.level = level
        self.levelCount = levelCount
        self.goal = False
        self.deaths = 0

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.y - self.radius > 0 and self.checkTileCollision((0,-1)):
            self.y -= self.speed
        if key[pygame.K_s] and self.y + self.radius < HEIGHT and self.checkTileCollision((0,1)):
            self.y += self.speed
        if key[pygame.K_a] and self.x - self.radius > 0 and self.checkTileCollision((-1,0)):
            self.x -= self.speed
        if key[pygame.K_d] and self.x + self.radius < WIDTH and self.checkTileCollision((1,0)):
            self.x += self.speed

    def checkTileCollision(self,direction):
        if direction[0] == -1 or direction[1] == -1:
            xpos = self.x + direction[0] * (self.radius + self.speed)
            ypos = self.y + direction[1] * (self.radius + self.speed)
        else:
            xpos = self.x + direction[0] * (self.radius)
            ypos = self.y + direction[1] * (self.radius)
        if xpos < WIDTH and ypos < HEIGHT:
            xTile = xpos // TILESIZE
            yTile = ypos // TILESIZE
            if self.level[self.levelCount][yTile][xTile] == 1:
                return False
            else:
                return True

    def checkGoal(self):
        xTile = self.x // TILESIZE
        yTile = self.y // TILESIZE
        if self.level[self.levelCount][yTile][xTile] == 4 and self.goal == False:
            self.goal = True
            return True
        else:
            return False
    def update(self):
        self.move()
        pygame.draw.circle(self.screen,"#e74c3c",(self.x,self.y),self.radius)

    def collide(self,enemyPos,size):
        if self.x - size <= enemyPos[0] <= self.x + size and self.y - size <= enemyPos[1] <= self.y + size:
            self.x = self.startPoint[0]
            self.y = self.startPoint[1]
            pygame.mixer.Sound.play(hurtSound)
            self.deaths += 1
