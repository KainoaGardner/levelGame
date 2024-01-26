import pygame
TILESIZE = 50
TILEAMOUNT = 20
WIDTH = TILEAMOUNT * TILESIZE
HEIGHT = TILEAMOUNT * TILESIZE

FPS = 60
pygame.init()
font = pygame.font.SysFont("Bahnschrift",35)
bigFont = pygame.font.SysFont("Bahnschrift",50)
mainMenuImage = pygame.image.load("graphics/mainmenu.png")

hurtSound = pygame.mixer.Sound("audio/hurt.wav")
hurtSound.set_volume(.5)
shootSound = pygame.mixer.Sound("audio/shoot.wav")
shootSound.set_volume(.05)
explosionSound = pygame.mixer.Sound("audio/explosion.wav")
explosionSound.set_volume(.3)