import pygame

img = pygame.image.load("cave.jpg")

pygame.display.init()
disp = pygame.display.set_mode((640, 480))

for x in range(img.get_width()):
    for y in range(img.get_height()):
        if x % 2 == 1 and y % 2 == 1:
            disp.fill(img.get_at((x, y)), (x, y, 2, 2))

pygame.display.update()

pygame.time.delay(5000)

pygame.display.quit()
