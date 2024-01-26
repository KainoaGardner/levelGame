import pygame

def scaleImage(image,scale):
    size = round(image.get_width() * scale),round(image.get_height() * scale)
    return pygame.transform.scale(image,size)

def rotateCenter(screen,image,topLeft,angle):
    rotatedImage = pygame.transform.rotate(image,angle)
    newRect = rotatedImage.get_rect(center=image.get_rect(topleft=topLeft).center)
    screen.blit(rotatedImage,newRect.topleft)

