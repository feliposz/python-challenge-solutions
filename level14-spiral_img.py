import pygame

imgItaly = pygame.image.load("italy.jpg")
imgWire = pygame.image.load("wire.png")

# os pixels em wire.png estão em sequencia e devem ser dispostos numa "espiral"
# para formar a imagem


pygame.display.init()
disp = pygame.display.set_mode((640, 480))
x = 0
y = 0
i = 0
maxNum = 100

while (i < 10000 and maxNum > 0):
    for direcao in range(4):
        cont = 0
        if direcao == 0:
            dx = 1 ; dy = 0
        elif direcao == 1:
            dx = 0 ; dy = 1
            maxNum -= 1
        elif direcao == 2:
            dx = -1 ; dy = 0
        elif direcao == 3:
            dx = 0 ; dy = -1
            maxNum -= 1
        while (i < 10000 and cont < maxNum):
            cont += 1
            disp.set_at((x, y), imgWire.get_at((i, 0)))
            x += dx
            y += dy
            i += 1
        pygame.display.flip()

pygame.time.delay(3000)
pygame.display.quit()

#and its name is uzi. you'll hear from him later. 

