import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
NEGRE = (0,0,0)
BLANC = (255,255,255)
VERMELL = (255,0,0)
TARONJA = (255,127,0)
GROC = (255,255,0)
VERD = (0,255,0)
BLAU = (0,0,255)
LILA = (75,0,130)
MORAT = (148,0,211)


pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Escala Colors')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANC)
    rectangle1 =  pygame.Rect(0, 0, 50, 50)
    rectangle2 = pygame.Rect(0, 50, 100, 50)
    rectangle3 = pygame.Rect(0, 100, 150, 50)
    rectangle4 = pygame.Rect(0, 150, 200, 50)
    rectangle5 = pygame.Rect(0, 200, 250, 50)
    rectangle6 = pygame.Rect(0, 250, 300, 50)
    rectangle7 = pygame.Rect(0, 300, 350, 50)
    pygame.draw.rect(pantalla, VERMELL, rectangle1)
    pygame.draw.rect(pantalla, TARONJA, rectangle2)
    pygame.draw.rect(pantalla, GROC, rectangle3)
    pygame.draw.rect(pantalla, VERD, rectangle4)
    pygame.draw.rect(pantalla, BLAU, rectangle5)
    pygame.draw.rect(pantalla, LILA, rectangle6)
    pygame.draw.rect(pantalla, MORAT, rectangle7)
    pygame.display.update()
