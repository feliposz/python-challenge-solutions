import pygame

img = pygame.image.load("oxygen.png")

linha = 46
coluna = 3

while (coluna < 610):
    cor = img.get_at((coluna, linha))
    print (chr(cor[0]), end="")
    coluna += 7

lista = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print()
for c in lista:
    print (chr(c), end="")
