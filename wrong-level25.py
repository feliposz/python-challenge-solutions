import pygame

lake1 = pygame.image.load("lake1.jpg")

pygame.display.init()
disp = pygame.display.set_mode((640, 480))

disp.blit(lake1, (0,0))

startx = [127, 255, 384, 512]
for x in startx:
    disp.set_at((x, 0), (255, 0, 255, 255))



starty = [96, 192, 288, 384]
for y in starty:
    disp.set_at((0, y), (255, 0, 255, 255))


for x in startx:


pygame.display.flip()
pygame.time.delay(4000)
pygame.display.quit()

for x in startx:
    print(x)

print()

for y in starty:
    print(y)


    color = lake1.get_at((x, 0))
    if color[0] < 50 and color[1] < 50 and color[2] < 50:

#you have seen that e**l (evil?) gimmick before
