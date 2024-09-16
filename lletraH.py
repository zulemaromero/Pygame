import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
NEGRE = (0,0,0)
VERMELL = (255,0,0,0)
BLANC = (255,255,255)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Lletra H')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANC)
    rectangle1 =  pygame.Rect(100, 100, 50, 200)
    rectangle2 = pygame.Rect(200, 100, 50, 200)
    rectangle3 = pygame.Rect(100, 170, 100, 50)
    pygame.draw.rect(pantalla, VERMELL, rectangle1)
    pygame.draw.rect(pantalla, VERMELL, rectangle2)
    pygame.draw.rect(pantalla, VERMELL, rectangle3)
    pygame.display.update()
