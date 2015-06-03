import pygame
import pickle

pfile = open("level24_points.pickle", "rb")
points = pickle.load(pfile)
pfile.close()

maze = pygame.image.load("maze3.png")

pygame.display.init()
disp = pygame.display.set_mode((800, 600))
disp.blit(maze, (0,0))

data = []
for p in points:
    color = maze.get_at(p)
    data.append(color[0])
    disp.set_at(p, (0, 0, 255, 255))

pygame.display.flip()
pygame.time.delay(5000)
pygame.display.quit()

# get only the odd bytes
bdata = bytes(data)

myzip = open("level24_result.zip", "wb")
myzip.write(bdata)
myzip.close()
