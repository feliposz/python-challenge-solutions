import pygame

frames = []
for i in range(133):
    frames.append(pygame.image.load("white\\frame"+str(i)+".png"))

pygame.display.init()
disp = pygame.display.set_mode((640,480))

x = 50
y = 50

for i in range(133):
    dx = 0
    dy = 0
    for px in [98, 100, 102]:
        for py in [98, 100, 102]:
            if frames[i].get_at((px, py))[0] > 0:
                dx = px - 100
                dy = py - 100
    if dx == 0 and dy == 0:
        x += 50
        y = 50
    x += dx
    y += dy
    disp.set_at((x, y), (255, 255, 255, 255))
    pygame.display.flip()
    pygame.time.delay(50)

pygame.display.flip()
pygame.time.delay(5000)
pygame.display.quit()
