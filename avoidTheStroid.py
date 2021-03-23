#! /usr/local/bin/python

# author: Alex Taft
# date  : 11/21/18


import pygame, random, sys

from pygame.locals import *


sx = 500
sy = 500

pygame.init()
screen = pygame.display.set_mode((sx, sy))
pygame.display.set_caption('Avoid the Stroid')

clock = pygame.time.Clock() 

shipImage = pygame.image.load('./images/ship.png').convert()
shipRect = shipImage.get_rect()

# ==================================================
def ship(cx,cy):
    
    screen.blit(shipImage, (cx,cy))

    shipRect.x = cx
    shipRect.y = cy

# ==================================================
class astroid():
    #x =  
    x = 0 
    y = 0
    xAmt = 0

    def __init__(self):
        self.x = random.randint(0,400)
        self.stroidImage = pygame.image.load('./images/stroid.png').convert()
        self.sRect = self.stroidImage.get_rect()

    def draw(self):
        screen.blit(self.stroidImage, (self.x,self.y))
        self.sRect.x = self.x
        self.sRect.y = self.y

    def col(self):
        return self.sRect.colliderect(shipRect)
        
# ==================================================

cx      = 250   
cy      = 350   
C_XSIZE = 150
C_YSIZE = 100
C_DIST  = 1


astList = []

pygame.key.set_repeat(1)

font_coord = pygame.font.Font(None, 16)

cycleCount = 0
health = 100
score = 0

# ==================================================
while True:

    sx,sy = screen.get_size()
    screen.fill((0, 0, 0))
    
    # ------------------------------
    for ast in astList:
        if(cycleCount%4 == 0):
            ast.xAmt = random.randint(-3,3)
        if ((ast.x < sx - C_XSIZE) and (ast.xAmt > 0)) or ((ast.x > 0) and (ast.xAmt < 0)):
            ast.x += ast.xAmt

        ast.y += 1
        if(ast.y > sy):
            astList.remove(ast)
            score += 1 

    if(random.randint(0,90) == 0):
        astList.append(astroid())

    # ------------------------------
    for e in pygame.event.get():
        if e.type == KEYDOWN:
            keys = pygame.key.get_pressed()  #checking pressed keys
            if keys[pygame.K_RETURN]:
                sys.exit(0)
            elif keys[pygame.K_RIGHT]:
                if cx < sx - C_XSIZE:
                    cx += C_DIST
            elif keys[pygame.K_LEFT]:
                if cx > 0:
                    cx -= C_DIST
            elif keys[pygame.K_UP]:
                if cy > 0:
                    cy -= C_DIST
            elif keys[pygame.K_DOWN]:
                if cy < sy - C_YSIZE:
                    cy += C_DIST 

    # ------------------------------
    for ast in astList:
        if ast.col():
            print("ouch\r")
            health -= 1
            screen.fill((150, 0, 0))
        ast.draw() 

    # ------------------------------

    ship(cx,cy)

    sTex = "(" + str(cx) + "," + str(cy) + ")"
    text_coord = font_coord.render(sTex, True, (255,255,255))

    sHealth = "health: " + str(health) 
    text_health = font_coord.render(sHealth, True, (255,255,255))

    sScore = "score: " + str(score) 
    text_score = font_coord.render(sScore, True, (255,255,255))

    screen.blit(text_coord, (0,0))
    screen.blit(text_health, (0,12))
    screen.blit(text_score, (0,24))

    # ------------------------------
    if health > 0:
        cycleCount += 1
        pygame.display.update()
        clock.tick(40)




