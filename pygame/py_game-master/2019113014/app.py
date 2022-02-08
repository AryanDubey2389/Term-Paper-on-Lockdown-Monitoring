import pygame
import sys
import math
import time
import config
pygame.init()

win = pygame.display.set_mode((1180, 800))

pygame.display.set_caption("FIRST GAME")
yel = [255, 255, 0]
x = 540
y = 760
xi = 540
yi = 0
temp1 = 9
width = 30
height = 15
vel = 10
red = [255, 0, 0]
dis = 0
p = 0
t = 0
i = 0
s = ""
f = 0
v = 0
temp2 = []
temp2.append(0)
champ1 = pygame.image.load("img.png")
champ1 = pygame.transform.scale(champ1, (70, 30))
champ2 = pygame.image.load("img1.png")
champ2 = pygame.transform.scale(champ2, (70, 30))

x1 = [50, 270, 500, 750, 1000]
x2 = [0, 200, 420, 650, 1000]
x3 = [0, 220, 450, 720, 959]
x4 = [30, 220, 500, 890, 1090]
x5 = [100, 300, 480, 800, 1050]
x6 = [200, 300, 600, 850]
yo1 = [610, 430, 290, 120]
x7 = [850, 600, 300, 200]
d = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0
]
y1 = [70, 210, 370, 530, 690]
f1 = 0
f2 = 0
temp = 0
minim = 800
scorey = [650, 600, 480, 430, 330, 280, 160, 110, 30]
scorey1 = [30, 110, 160, 280, 330, 430, 480, 600, 650]
font = pygame.font.SysFont(None, 40)
score = 0
mvng0 = pygame.image.load("img.png")
mvng0 = pygame.transform.scale(mvng0, (94, 50))
mvng1 = pygame.image.load("e.png")  # tellling about the player image
mvng1 = pygame.transform.scale(mvng1, (94, 50))
mvng2 = pygame.image.load("d.png")
mvng2 = pygame.transform.scale(mvng2, (94, 50))
mvng3 = pygame.image.load("e.png")
mvng3 = pygame.transform.scale(mvng3, (94, 50))

mvng4 = pygame.image.load("shark.png")
mvng4 = pygame.transform.scale(mvng4, (94, 50))

mvng5 = pygame.image.load("tree.png")
mvng5 = pygame.transform.scale(mvng5, (94, 50))

arr2 = [mvng0, mvng1, mvng2, mvng3, mvng4]
score1 = 0
s1 = "0"
score = 0
l = 1
var = 0


def barrier(y2, y1, x2, x1):
    dis = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if dis < 40:
        return 1
    else:
        return 0


def found(s, len):
    for i in range(0, len):
        if s == temp2[i]:
            return 1
    return 0


def blit(img, k, l):
    win.blit(img, (k, l))


def start(msg):
    screen_text = font.render(msg, True, red)
    win.blit(screen_text, [540, 760])


def end(msg):
    screen_text = font.render(msg, True, red)
    win.blit(screen_text, [540, 0])


def level(l):
    screen_text = font.render(l, True, red)
    win.blit(screen_text, [40, 750])


def points(s):
    screen_text1 = font.render("Champ1 - " + s + " Now Playing", True, red)
    win.blit(screen_text1, [50, 10])

    screen_text = font.render("Champ2 - " + s1, True, red)
    win.blit(screen_text, [950, 10])


def points1(s1):
    screen_text = font.render("Champ2 - " + s1 + "  Now Playing", True, red)
    win.blit(screen_text, [750, 10])
    screen_text1 = font.render("Champ1 - " + s, True, red)
    win.blit(screen_text1, [50, 10])


def begin(s2):
    screen_text = font.render(s2, True, red)
    win.blit(screen_text, [540, 400])


def collide(fl):
    screen_text = font.render(fl, True, yel)
    win.blit(screen_text, [540, 400])


def finalscore(fl):
    screen_text = font.render(fl, True, yel)
    win.blit(screen_text, [540, 700])


f = 0
win.fill((0, 0, 255))
run = True
j = 1
arr2 = [mvng0, mvng1, mvng2, mvng3, mvng4]
while f == 0:
    x = 540
    y = 760
    run = 1
    score = 0
    score1 = 0
    s1 = str(score1)

    while run:
        for i in range(0, len(temp2)):
            temp2[i] = 0
        pygame.time.delay(100)
        win.fill((0, 100, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > vel - 55:
            x -= vel
        if keys[pygame.K_RIGHT] and x < 1180 - width - vel:
            x += vel  # working of the keys
        if keys[pygame.K_UP] and y > vel - 15:
            y -= vel
        if keys[pygame.K_DOWN] and y < 780 - height - vel:
            y += vel
        pygame.draw.line(win, yel, (0, 0), (1180, 0), 80)
        pygame.draw.line(win, red, (0, 160), (1180, 160), 50)
        pygame.draw.line(win, red, (0, 320), (1180, 320),
                         50)  # my whole screen
        pygame.draw.line(win, red, (0, 480), (1180, 480), 50)
        pygame.draw.line(win, red, (0, 640), (1180, 640), 50)
        pygame.draw.line(win, yel, (0, 800), (1180, 800), 80)
        start("START")
        end("END")
        string = str(l)
        level("LEVEL - " + string)
        win.blit(champ1, (x, y))

        for i in range(0, 7):
            if y < scorey[i] and y > scorey[i+1] and minim > y and i % 2 == 0:
                score += 10
                minim = scorey[i + 1]  # finding the score
            else:
                if y < scorey[i] and y > scorey[
                        i + 1] and minim > y and i % 2 == 1:
                    score += 5
                    minim = scorey[i + 1]
        if y <= scorey[8] and minim < y and y < 880:
            score += 10
            minim = 0

        t = 0
        while t < len(x6):
            blit(mvng5, x6[t], yo1[t])
            blit(mvng5, x7[t], yo1[t])  # storing the obstacles
            t = t + 1
        pygame.display.update()
        t = 0
        while t < 5:
            x1[t] += 10 + v
            if x1[t] > 1180:
                x1[t] = 0  # storing the obstacles
            blit(mvng0, x1[t], y1[0])
            t = t + 1
        t = 0
        while t < 5:
            x2[t] = x2[t] - 10 - v
            if x2[t] < 0:
                x2[t] = 1180  # storing the obstacles
            blit(mvng1, x2[t], y1[1])
            t = t + 1
        t = 0
        while t < 5:
            x3[t] += 10 + v
            if x3[t] > 1180:
                x3[t] = 0
            blit(mvng2, x3[t], y1[2])
            t = t + 1
        t = 0
        while t < 5:
            x4[t] = x2[t] - 10 - v
            if x4[t] < 0:
                x4[t] = 1180
            blit(mvng3, x4[t], y1[3])
            t = t + 1
        t = 0
        while t < 5:
            x5[t] += 10 + v
            if x5[t] > 1080:
                x5[t] = 0
            blit(mvng4, x5[t], y1[4])
            t = t + 1
        pygame.display.update()
        var = -1

        t = 0
        for t in range(0, t + 30):
            d.append(0)
        t = 0
        while t < 4:
            d[t + 4] = barrier(y, y1[0], x, x1[t])  # movement of the obstacles
            t = t + 1
        t = 0
        while t < 4:
            d[t + 8] = barrier(y, y1[1], x, x2[t])
            t = t + 1
        t = 0
        while t < 4:
            d[t + 12] = barrier(y, y1[2], x, x3[t])
            t = t + 1
        t = 0
        while t < 4:
            d[t + 16] = barrier(
                y, y1[3], x,
                x4[t])  # using the distance formula to check collision
            t = t + 1
        t = 0
        while t < 4:
            d[t + 20] = barrier(y, y1[4], x, x5[t])
            t = t + 1
        t = 0
        while t < 4:
            d[t + 24] = barrier(y, yo1[t], x, x6[t])
            t = t + 1
        t = 0
        while t < 4:
            d[t + 28] = barrier(y, yo1[t], x, x7[t])
            t = t + 1
        t = 0
        while t < 32:
            p = p or d[t]
            t = t + 1
            if p == 1:
                f1 = 1
        if p == 1:
            print("LOST")
            collide("CHAMP1 COLLIDED")
            pygame.display.update()  # checking the collision
            time.sleep(2)
            f = 1
            yi = 10

        if y == 0:
            temp1 = y
            f = 1
            yi = 0
        s = str(score)
        points(s)
        pygame.display.update()

        while f == 1:
            minim = 0
            for i in range(0, len(temp2)):
                temp2[i] = 0
            p = 0
            start("END")
            end("START")
            while run:
                pygame.time.delay(100)
                win.fill((0, 100, 255))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                keys = pygame.key.get_pressed()

                if keys[pygame.K_a] and xi > vel - 55:
                    xi -= vel
                if keys[pygame.K_d] and xi < 1180 - width - vel:
                    xi += vel
                if keys[pygame.K_w] and yi > vel - 15:  # working of the keys
                    yi -= vel

                if keys[pygame.K_s] and yi < 780 - height - vel:
                    yi += vel

                pygame.draw.line(win, yel, (0, 0), (1180, 0), 80)
                pygame.draw.line(win, red, (0, 160), (1180, 160), 50)
                pygame.draw.line(win, red, (0, 320), (1180, 320), 50)
                pygame.draw.line(win, red, (0, 480), (1180, 480),
                                 50)  # the whole scene
                pygame.draw.line(win, red, (0, 640), (1180, 640), 50)
                pygame.draw.line(win, yel, (0, 800), (1180, 800), 80)
                win.blit(champ2, (xi, yi))
                start("END")
                end("START")
                string = str(l)
                level("LEVEL - " + string)
                temp = 0
                pygame.display.update()
                t = 0
                for i in range(0, 7):
                    if yi > scorey1[i] and yi < scorey1[
                            i + 1] and minim < yi and i % 2 == 0:
                        score1 += 10
                        minim = scorey1[i + 1]  # storing the score
                    else:
                        if yi > scorey1[i] and yi < scorey1[
                                i + 1] and minim < yi and i % 2 == 1:
                            score1 += 5
                            minim = scorey1[i + 1]
                    if yi <= scorey1[0] and minim > yi and yi < 780:
                        minim = 0
                t = 0
                while t < len(x6):
                    blit(mvng5, x6[t], yo1[t])
                    blit(mvng5, x7[t], yo1[t])
                    t = t + 1
                    pygame.display.update()
                t = 0  # movement of the obstacles
                while t < 5:
                    x1[t] += 10 + v
                    if x1[t] > 1180:
                        x1[t] = 0
                    blit(mvng0, x1[t], y1[0])
                    t = t + 1
                t = 0
                while t < 5:
                    x2[t] = x2[t] - 10 - v
                    if x2[t] < 0:
                        x2[t] = 1180
                    blit(mvng1, x2[t], y1[1])
                    t = t + 1
                t = 0
                while t < 5:
                    x3[t] += 10 + v
                    if x3[t] > 1180:
                        x3[t] = 0
                    blit(mvng2, x3[t], y1[2])
                    t = t + 1
                t = 0
                while t < 5:
                    x4[t] = x4[t] - 10 - v
                    if x4[t] < 0:
                        x4[t] = 1180
                    blit(mvng3, x4[t], y1[3])
                    t = t + 1
                t = 0
                while t < 5:
                    x5[t] += 10 + v
                    if x5[t] > 1080:
                        x5[t] = 0
                    blit(mvng4, x5[t], y1[4])
                    t = t + 1
                pygame.display.update()

                t = 0
                for t in range(0, t + 30):
                    d.append(0)
                t = 0
                while t < 4:
                    d[t + 4] = barrier(yi, y1[0], xi, x1[t])
                    t = t + 1
                t = 0
                while t < 4:
                    d[t + 8] = barrier(yi, y1[1], xi, x2[t])
                    t = t + 1
                t = 0
                while t < 4:
                    d[t + 12] = barrier(yi, y1[2], xi, x3[t])
                    t = t + 1  # using distance formula to calculate distance
                t = 0
                while t < 4:
                    d[t + 16] = barrier(yi, y1[3], xi, x4[t])
                    t = t + 1
                t = 0
                while t < 4:
                    d[t + 20] = barrier(yi, y1[4], xi, x5[t])
                    t = t + 1
                t = 0
                while t < 4:
                    d[t + 24] = barrier(yi, yo1[t], xi, x6[t])
                    t = t + 1
                t = 0
                while t < 4:
                    d[t + 28] = barrier(yi, yo1[t], xi, x7[t])
                    t = t + 1
                t = 0
                while t < 32:
                    p = p or d[t]
                    t = t + 1

                if p == 1:
                    collide("CHAMP2 COLLIDED")
                    pygame.display.update(
                    )  # checking the collision and also who won or lost
                    time.sleep(2)
                    if score > score1:
                        finalscore("CHAMP1 WINS")
                    else:
                        finalscore("CHAMP2 WINS")
                    pygame.display.update()
                    time.sleep(2)
                    run = 0
                    f = 0
                if yi == 760:
                    f = 0
                    y = 760
                    v += 10
                    l = l + 1
                    break

                s1 = str(score1)
                points1(s1)
                pygame.display.update()

            pygame.display.update()
        p = 0

pygame.quit()
