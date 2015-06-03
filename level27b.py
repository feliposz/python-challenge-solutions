import pygame
import pickle

zigzag = pygame.image.load("zigzag.gif")

pal = zigzag.get_palette()

data = []
for y in range(zigzag.get_height()):
    for x in range(zigzag.get_width()):
        color = zigzag.get_at((x, y))
        data.append(pal.index(color))

bdata = bytes(data)

#obj = pickle.loads(bdata)
