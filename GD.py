#-*-coding: utf8-*-
import pygame
import pygame as pg
from time import*
from collections import deque
pygame.init()
size = [800, 600]
x = 400
y = 525
vy = 0
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
block = pg.image.load('X Generation/block.bmp')
bR = block.get_rect(
    bottomright=size)
screen.blit(block, bR)
running = True
V = open('X Generation/Level.txt', mode = 'r').read()
V = V.split("\n")
def dts(x1, y1, x2, y2, x3, y3):
    for i in range(100):
        m1x, m1y = (x1 * 2 + x2) / 3, (y1 * 2 + y2) / 3
        m2x, m2y = (x1 + x2 * 2) / 3, (y1 + y2 * 2) / 3
        if (((m1x - x3) ** 2 + (m1y - y3) ** 2) > ((m2x - x3) ** 2 + (m2y - y3) ** 2)):
            x1 = m1x
            y1 = m1y
        else:
            x2 = m2x
            y2 = m2y
    return ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

for i in range(len(V)):

    V[i] = V[i].split()
itb = False
jump = False
mode = 0
mp = {}
for i in V:
    if i == []:
        continue
    #print(i)
    if max(int(i[2]), 376) in mp:
        mp[max(int(i[2]), 376)].append(i)
    else:
        mp[max(int(i[2]), 376)] = [i]
L = deque()
xv = 5
while running:
    x += xv
    #print(x)
    if mode == 2:
        if jump:
            vy = -0.5
        if 1:
            vy += 0.05
            if vy >= 1:
                vy = 2
            #print(vy, itb)
            if 1:
                
                y = (y + min(vy, 1))
                #print(int(min(vy, 1)) // 1, itb, vy)
                if vy < 0:
                    y -= 1
            if y >= 525:
                y = 525
                itb = True
    if mode == 1:
        #print(jump)
        if jump:
            y -= xv
        else:
            y += xv
    if mode == 0 or mode==3:
        if vy == "a":
            pass
        else:
            #x += 1
            vy += 0.025 * xv
            if vy >= 1:
                vy = 1
            #print(vy, itb)
            if 1:
                
                y = (y + min(vy, 1))
                #print(int(min(vy, 1)) // 1, itb, vy)
                #if vy < 0:
                #    y -= 1
            if y >= 525:
                y = 525
                itb = True
        #print(y, vy)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            jump = True
            #print("J")
        if event.type ==  pygame.MOUSEBUTTONUP:
            jump = False
            #print("U")
    # обновляем значения
    screen.fill((255, 0, 255))
    Obj = []
    if jump and (itb or mode == 2):
        vy -= 5
        y -= 3
        itb = 0
    if x + 900 in mp:
        for i in mp[x + 900]:
            L.append(i)
    while not len(L) == 0 and int(L[0][2]) == x - 450:
        L.popleft()
    for i in L:
        if i[0] == "block":
            Obj.append(pg.image.load('X Generation/block.bmp'))
            #if 1:
                #print(int(i[2]), int(i[1]), x, y)
                #if (dts(int(i[2]) - 400, int(i[1]), int(i[2]) - 450, int(i[1]), x, y + 50) <= 150):
                    #print(dts(int(i[2]) - 400, int(i[1]), int(i[2]) - 450, int(i[1]), x, y + 50), int(i[2]) - 400, int(i[1]), int(i[2]) - 350, int(i[1]), x, y - 100)
            Obj.append(Obj[-1].get_rect(
                topleft=(int(i[2]) - x, int(i[1]))))
            screen.blit(Obj[-2], Obj[-1])
            #running = True
            if dts(int(i[2]) - 400, int(i[1]), int(i[2]) - 400, int(i[1]) - 50, x, y) <= 25:
                running = False
            #pygame.draw.line(screen, "red", (int(i[2]) - x, int(i[1])), (int(i[2]) - x + 50, int(i[1])), width = 10) 
            if dts(int(i[2]) - 400, int(i[1]), int(i[2]) - 350, int(i[1]), x, y + 50) <= 27:
                itb = True
                vy = "a"
                #print(10)
            else:
                if vy == "a":
                    vy = 0
            
        if i[0] == "spike":
            Obj.append(pg.image.load('X Generation/spike.bmp'))
            Obj[-1].set_colorkey((255, 255, 255))
            #print(int(i[2]) - x, int(i[1]))
            Obj.append(Obj[-1].get_rect(
                topleft=(int(i[2]) - x, int(i[1]))))
            screen.blit(Obj[-2], Obj[-1])
            #running = True
            if dts(int(i[2]) - 400, int(i[1]), int(i[2]) - 375, int(i[1]) - 50, x, y) <= 27 or dts(int(i[2]) - 350, int(i[1]), int(i[2]) - 375, int(i[1]) - 50, x, y) <= 27 or dts(int(i[2]) - 350, int(i[1]), int(i[2]) - 400, int(i[1]), x, y) <= 27:
                running = False

 
        
        if i[0] == "sgras":
            Obj.append(pg.image.load('X Generation/sgras.bmp'))
            Obj[-1].set_colorkey((255, 255, 255))
            #print(int(i[2]) - x, int(i[1]))
            Obj.append(Obj[-1].get_rect(
                topleft=(int(i[2]) - x, int(i[1]))))
            screen.blit(Obj[-2], Obj[-1])
            if dts(int(i[2]) - 400, int(i[1]), int(i[2]) - 350, int(i[1]), x, y) <= 27:
                running = False
        if i[0] == "pofly":
            Obj.append(pg.image.load('X Generation/pofly.bmp'))
            Obj[-1].set_colorkey((255, 255, 255))
            #print(int(i[2]) - x, int(i[1]))
            Obj.append(Obj[-1].get_rect(
                topleft=(int(i[2]) - x, int(i[1]))))
            screen.blit(Obj[-2], Obj[-1])
            if dts(int(i[2]) - 375, int(i[1]), int(i[2]) - 375, int(i[1]) + 150, x, y) <= 27:
                mode = 1
        if i[0] == "posqr":
            Obj.append(pg.image.load('X Generation/posqr.bmp'))
            Obj[-1].set_colorkey((255, 255, 255))
            #print(int(i[2]) - x, int(i[1]))
            Obj.append(Obj[-1].get_rect(
                topleft=(int(i[2]) - x, int(i[1]))))
            screen.blit(Obj[-2], Obj[-1])
            if dts(int(i[2]) - 375, int(i[1]), int(i[2]) - 375, int(i[1]) + 150, x, y) <= 27:
                mode = 0
        if i[0] == "popln":
            Obj.append(pg.image.load('X Generation/popln.bmp'))
            Obj[-1].set_colorkey((255, 255, 255))
            #print(int(i[2]) - x, int(i[1]))
            Obj.append(Obj[-1].get_rect(
                topleft=(int(i[2]) - x, int(i[1]))))
            screen.blit(Obj[-2], Obj[-1])
            if dts(int(i[2]) - 375, int(i[1]), int(i[2]) - 375, int(i[1]) + 150, x, y) <= 27:
                mode = 2
        if i[0] == "pgras":
            Obj.append(pg.image.load('X Generation/pgras.bmp'))
            Obj[-1].set_colorkey((255, 255, 255))
            #print(int(i[2]) - x, int(i[1]))
            Obj.append(Obj[-1].get_rect(
                topleft=(int(i[2]) - x, int(i[1]))))
            screen.blit(Obj[-2], Obj[-1])
            if dts(int(i[2]) - 400, int(i[1]) - 50, int(i[2]) - 350, int(i[1]) - 50, x, y) <= 27:
                running = False
        if i[0] == "Aline":
            Obj.append(pg.image.load('X Generation/Aline.bmp'))
            Obj[-1].set_colorkey((255, 255, 255))
            #print(int(i[2]) - x, int(i[1]))
            Obj.append(Obj[-1].get_rect(
                topleft=(int(i[2]) - x, int(i[1]))))
            screen.blit(Obj[-2], Obj[-1])
            if dts(int(i[2]) - 400, int(i[1]) - 50, int(i[2]) - 350, int(i[1]), x, y) <= 27:
                running = False
        if i[0] == "Bline":
            Obj.append(pg.image.load('X Generation/Bline.bmp'))
            Obj[-1].set_colorkey((255, 255, 255))
            #print(int(i[2]) - x, int(i[1]))
            Obj.append(Obj[-1].get_rect(
                topleft=(int(i[2]) - x, int(i[1]))))
            screen.blit(Obj[-2], Obj[-1])
            if dts(int(i[2]) - 400, int(i[1]), int(i[2]) - 350, int(i[1]) - 50, x, y) <= 27:
                running = False
        if i[0] == "x2spd":
            Obj.append(pg.image.load('X Generation/x2spd.bmp'))
            Obj[-1].set_colorkey((255, 255, 255))
            #print(int(i[2]) - x, int(i[1]))
            Obj.append(Obj[-1].get_rect(
                topleft=(int(i[2]) - x, int(i[1]))))
            screen.blit(Obj[-2], Obj[-1])
            if dts(int(i[2]) - 375, int(i[1]), int(i[2]) - 375, int(i[1]) + 150, x, y) <= 27:
                xv = 6
    Obj.append(pg.image.load('player.bmp'))
    Obj[-1].set_colorkey((255, 255, 255))
    #print(int(i[2]) - x, int(i[1]))
    Obj.append(Obj[-1].get_rect(
        topleft=(375, int(y // 1) + 25)))
    screen.blit(Obj[-2], Obj[-1])
    #running = True
    # рисуем
    pygame.display.flip()
    #clock.tick(300)
    #sleep(1)
pygame.quit()
