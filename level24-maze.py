import pygame
import sys

sys.setrecursionlimit(10000)

maxdepth = 0

def walkmaze(x, y, depth=0):
    global maxdepth
    #if x == 645 or y == 645:
    if y == 4:
        print ("Found the way!!!")
        return True
    if depth > maxdepth:
        maxdepth = depth
    color = disp.get_at((x, y))
    if color == (0,0,255,255) or color[2] == 0:
        return False
    disp.set_at((x, y), (0,0,255,255))
    if (depth % 50 == 0):
        pygame.display.flip()
    if walkmaze(x+1, y, depth+1) or walkmaze(x, y+1, depth+1) or walkmaze(x, y-1, depth+1) or walkmaze(x-1, y, depth+1):
        return True
    else:
        disp.set_at((x, y), (128,128,255,255))
        pygame.display.flip()
        return False


maze = pygame.image.load("maze.png")

pygame.display.init()
disp = pygame.display.set_mode((650,650))

disp.blit(maze, (5, 5))

#disp.set_at((640, 5), (255,0,255,255))
#disp.set_at((645, 645), (255,0,255,255))
#walkmaze(643, 5)
walkmaze(645, 645)

print("maxdepth =", maxdepth)

pygame.display.flip()
pygame.time.delay(10000)
pygame.display.quit()

