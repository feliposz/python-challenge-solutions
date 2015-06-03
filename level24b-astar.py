import AStar
import pygame
from time import time
import pickle


maze = pygame.image.load("maze3.png")

mapdata = []
width = maze.get_width()
height = maze.get_height()

WALL = -1
PATH = 1

for y in range(height):
    for x in range (width):
        color = maze.get_at((x, y))
        if color == (255,255,255,255):
            mapdata.append(WALL)
        else:
            mapdata.append(PATH)

startpoint = (639, 0)
endpoint = (1, 640)

mapdata[startpoint[0] + startpoint[1] * width] = 5
mapdata[endpoint[0] + endpoint[1] * width] = 6

maphandler = AStar.SQ_MapHandler(mapdata, width, height)
astar = AStar.AStar(maphandler)
start = AStar.SQ_Location(startpoint[0], startpoint[1])
end = AStar.SQ_Location(endpoint[0], endpoint[1])

stime = time()
path = astar.findPath(start, end)
etime = time()

if not path:
    print("not found")
else:
    print("found!")
    print("stime =", stime)
    print("etime =", etime)
    print("total =", etime-stime)
    print("nodes =", len(path.nodes))
    points = []
    for node in path.nodes:
        point = (node.location.x, node.location.y)
        if point[0]%2 and point[1]%2:
            points.append(point)
    pfile = open("level24_points.pickle", "wb")
    pickle.dump(points, pfile)
    pfile.close()
        
