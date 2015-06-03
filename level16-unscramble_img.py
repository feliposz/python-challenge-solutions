import pygame

imgMozart = pygame.image.load("mozart.gif")

pygame.display.init()
disp = pygame.display.set_mode((700, 700))

def getPix(i):
    return imgMozart.get_at((int(i%640), int(i/640)))

x = 0
y = 0
i = 0
totalPixels = imgMozart.get_height() * imgMozart.get_width() - 1
while i < totalPixels:
    p0 = getPix(i)
    p1 = getPix(i+1)
    if p0[0] > 240 and p0[1] > 240 and p0[2] > 240 and p1 == (255, 0, 255, 255):
        x = 0
        y = y+1
        i += 5
        pygame.display.flip()
    disp.set_at((x, y), p1)
    x += 1
    i += 1

pygame.display.flip()

pygame.time.delay(5000)
pygame.display.quit()

