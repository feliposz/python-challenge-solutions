import pygame
img = pygame.image.load("balloons.jpg")
pygame.display.init()
disp = pygame.display.set_mode((img.get_width(), img.get_height()*2))
halfWidth = int(img.get_width() / 2)
height = img.get_height()
for y in range(img.get_height()):
    for x in range(halfWidth):
        c1 = img.get_at((x, y))
        c2 = img.get_at((x+halfWidth, y))
        disp.set_at((x, y), c1-c2)
        disp.set_at((x+halfWidth, y), c2-c1)
        disp.set_at((x, y+height), c1)
        disp.set_at((x+halfWidth, y+height), c2)        
pygame.display.flip()
pygame.time.delay(15000)
pygame.display.quit()
