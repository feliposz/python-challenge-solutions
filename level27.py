import pygame

zigzag = pygame.image.load("zigzag.gif")

def other():
    global zigzag
    for i in [2408, 49443, 75111]:
        break
        print("=========")
        for j in range(275):
            x = int((i+j)%320)
            y = int((i+j)/320)
            color = zigzag.get_at((x, y))
            print(chr(color[0]), end="")
        print()


    for y in range(zigzag.get_height()):
        for x in range(zigzag.get_width()):
            color = zigzag.get_at((x, y))
            char = chr(color[0])
            if (char >= "A" and char <= "Z") or (char >= "a" and char <= "z"):
                print(char, end="")


def nothing():
    global zigzag
    pygame.display.init()
    disp = pygame.display.set_mode((640, 480))

    for y in range(zigzag.get_height()):
        for x in range(0, zigzag.get_width()-3, 3):
            color = (zigzag.get_at((x, y))[0], zigzag.get_at((x+1, y))[0], zigzag.get_at((x+2, y))[0], 255)
            disp.set_at((int(x/3), y), color)


    pygame.display.flip()
    pygame.time.delay(5000)
    pygame.display.quit()

def nothing2():
    global zigzag
    pygame.display.init()
    disp = pygame.display.set_mode((640, 480))

    for y in range(0, zigzag.get_height()-3, 3):
        for x in range(0, zigzag.get_width()):
            color = (zigzag.get_at((x, y))[0], zigzag.get_at((x, y+1))[0], zigzag.get_at((x, y+2))[0], 255)
            disp.set_at((x, int(y/3)), color)


    pygame.display.flip()
    pygame.time.delay(5000)
    pygame.display.quit()

def nothing3():
    global zigzag
    pygame.display.init()
    disp = pygame.display.set_mode((640, 480))

    px = 0
    py = 0
    data = []
    for y in range(zigzag.get_height()):
        for x in range(0, zigzag.get_width()):
            color = zigzag.get_at((x, y))
            data.append(color[0])
            disp.set_at((px, py), color)
            px += 1
            if px >= 298:
                px = 0
                py += 1

    pygame.display.flip()
    #pygame.time.delay(5000)
    pygame.display.quit()

    bdata = bytes(data)
    print(bdata)
    #open("level27.bin", "wb").write(bdata)

nothing3()
