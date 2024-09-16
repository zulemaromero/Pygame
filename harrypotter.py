import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
NEGRE = (0,0,0)
VERMELL = (255,0,0,0)
BLANC = (255,255,255)
ROSA = (255,182,193)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Cercle')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(ROSA)
    cercle1 = pygame.draw.circle(pantalla, BLANC, (100,200),75)
    cercle2 = pygame.draw.circle(pantalla, BLANC, (400, 200), 75)
    cercle3 = pygame.draw.circle(pantalla, NEGRE, (100, 200), 40)
    cercle4 = pygame.draw.circle(pantalla, NEGRE, (400, 200), 40)
    cercle5 = pygame.draw.circle(pantalla,NEGRE, (100, 200), 75,5)
    cercle6 = pygame.draw.circle(pantalla, NEGRE, (400, 200), 75,5)
    gafitas = pygame.draw.circle(pantalla, NEGRE, (100, 200), 95,10)
    gafitas2 = pygame.draw.circle(pantalla, NEGRE, (400, 200), 95,10)
    linea = pygame.draw.line(pantalla,NEGRE,(190,200),(305,200),5)
    boca = pygame.draw.ellipse(pantalla, BLANC, (150, 350, 200, 100))
    boca2 = pygame.draw.ellipse(pantalla,NEGRE,(150,350,200,100),5)
    nas = pygame.draw.polygon(pantalla,NEGRE,((250,275),(275,325),(225,325)),5)
    raig = pygame.draw.polygon(pantalla,NEGRE,((250,50),(220,75),(250,75),(220,100)),0)
    pygame.display.update()
