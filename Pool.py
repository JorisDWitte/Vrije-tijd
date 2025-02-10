import pygame
import sys
import math

## defining sizes etc (globals):
WIDTH = 1000
HEIGHT = 700
White = (255, 255, 255, 255)
Black = (0, 0, 0, 0)
Red = (200, 50, 50, 255)
Green = (150, 50, 200, 255)
BalRad = 15
fps = 15
MaxSpeed = 40
xhodl = 0
yhodl = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.init()

## functions
# clas bal and its movement
# subclass for white bal
#def text_objects for text display
class Balletje:
    def __init__(self, color, xpos, ypos, angle=0, speed=0):
        #radius=BalRad
        self.xpos = xpos
        self.ypos = ypos
        self.okay = color
        self.xspeed = speed
        self.yspeed = 0

    def draw(self):
        pygame.draw.circle(screen, self.okay, (self.xpos, self.ypos), BalRad)

    def move(self):
        if (20+BalRad > self.xpos+self.xspeed) or (self.xpos+self.xspeed > (WIDTH-20-BalRad)):
            self.xspeed = -self.xspeed
        if (20 + BalRad > self.ypos + self.yspeed) or (self.ypos + self.yspeed > (HEIGHT - 20 - BalRad)):
            self.yspeed = -self.yspeed
        self.xpos = self.xpos+self.xspeed
        self.ypos = self.ypos+self.yspeed
        if self.xspeed >= 1: self.xspeed = int((self.xspeed/40-1/40)*40)
        elif 1 < self.xspeed < -1: self.xspeed = 0
        elif self.xspeed <= -1: self.xspeed = int((self.xspeed / 40 + 1 / 40) * 40)
        # elif self.xspeed <= -1: self.xspeed += 1
        if self.yspeed >= 1: self.yspeed = int((self.yspeed / 40 - 1 / 40) * 40)
        elif 1 < self.yspeed < -1: self.yspeed = 0
        elif self.yspeed <= -1: self.yspeed = int((self.yspeed / 40 + 1 / 40) * 40)


    def bounce(self):
        pass
        # if xpos/pos is te groot of te klein
        # if (x/y)pos komt overeen met andere bal (x,y)pos


class WitBalletje(Balletje):
    def getstarted(self):
        if self.xspeed & self.yspeed == 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.xspeed += 50
                    if event.key == pygame.K_LEFT:
                        self.xspeed -= 50
"""                    if event.key == pygame.K_UP:
                        Bal_Speed[1] -= Bal_Input
                    if event.key == pygame.K_DOWN:
                        Bal_Speed[1] += Bal_Input
"""


def text_objects(text, font):
    textsurface = font.render(text, True, White)
    return textsurface, textsurface.get_rect()


## objecten:
# witte bal
# andere balletjes
witte = WitBalletje(White, WIDTH/5, HEIGHT/2, 1, 40)
balletjes = []
posballetjesx = [2*WIDTH/3, 2*WIDTH/3+1.6*BalRad, 2*WIDTH/3+1.6*BalRad]
posballetjesy = [HEIGHT/2, HEIGHT/2+BalRad, HEIGHT/2-BalRad]
for bal in range(len(posballetjesx)):
    balletjes.append(Balletje(Red, posballetjesx[bal], posballetjesy[bal], 1))
newtext1 = pygame.font.Font('freesansbold.ttf', 20)


## game states:
# 1. game itself

while True:
    screen.fill(Green)
    pygame.draw.rect(screen, Black, (0, 0, 20, HEIGHT)) #l
    pygame.draw.rect(screen, Black, (0, 0, WIDTH, 20)) #b
    pygame.draw.rect(screen, Black, (WIDTH-20, 0, WIDTH, HEIGHT)) #rechterboord
    pygame.draw.rect(screen, Black, (0, HEIGHT-20, WIDTH, HEIGHT))
    textsurf, textrect = text_objects(f"Hitting white bal for: {xhodl}, {yhodl}", newtext1)
    textrect.center = ((150), (20))
    screen.blit(textsurf, textrect)

    #pygame.draw.circle(screen, White, (WIDTH/5, HEIGHT/2), BalRad)
    witte.draw()
    witte.move()
    for balletje in balletjes:
        balletje.draw()
    clock.tick(fps)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xhodl += 10
            if event.key == pygame.K_LEFT:
                xhodl -= 10
            if event.key == pygame.K_DOWN:
                yhodl += 10
            if event.key == pygame.K_UP:
                yhodl -= 10
            if event.key == pygame.K_KP_ENTER:
                if witte.xspeed & witte.yspeed == 0:
                    if xhodl > 40: xhodl = 40
                    if yhodl > 40: yhodl = 40
                    witte.xspeed = xhodl
                    witte.yspeed = yhodl
                    xhodl = 0
                    yhodl = 0
