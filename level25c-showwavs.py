import pygame

def drawWavFile(file, coord, disp):
    result = open(file, "rb").read()
    y=0
    for width in [60]:
        i=44
        x=0
        while i < len(result)-3:
            color = (result[i], result[i+1], result[i+2])
            disp.set_at((coord[0]+x, coord[1]+y), color)
            i+=3
            x += 1
            if x == width:
                x = 0
                y += 1

pygame.display.init()
disp = pygame.display.set_mode((640, 480))

for i in range(25):
    x = int(i%5) * 60
    y = int(i/5) * 60
    drawWavFile("download\\lake" + str(i+1) + ".wav", (x, y), disp)
    pygame.display.flip()

pygame.time.delay(5000)
pygame.display.quit()
