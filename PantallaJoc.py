import time
from pygame.locals import *
import pygame

AMPLADA = 320
ALTURA = 200
BACKGROUND_IMAGE = 'assets/FondoJuego.png'
MUSICA_FONS = 'assets/MusicaArcade.mp3'
YELLOW = (255, 255, 0)
LOGO_IMAGE = "assets/animal.png"
GAME_OVER1 = "assets/PLAYERONE.png"
GAME_OVER2 = "assets/PLAYERTWO.png"
vides1 = 3
vides2 = 3
explosio1 = False
explosio2 = False
temps_explosio = 0
temps_durada_explosio = 500


# Explosión1:
explossion_image = pygame.image.load('assets/explosio.png')

# Jugador 1:
player_image = pygame.image.load('assets/NAUPRINCIPAL.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 2

# Jugador 2:
player_image2 = pygame.image.load('assets/NAUENEMIC.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 150))
velocitat_nau2 = 2

# Bala rectangular blanca:
bala_imatge = pygame.Surface((2, 6))  # definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(YELLOW)  # pintem la superficie de color blanc
bales_jugador1 = []  # llista on guardem les bales del jugador 1
bales_jugador2 = []  # llista on guardem les bales del jugador 2
velocitat_bales = 4
temps_entre_bales = 800  # 1 segon
temps_ultima_bala_jugador1 = 0  # per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0  # per contar el temps que ha passat des de que ha disparat el jugador 2

pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Galactic Battle")
logo = pygame.image.load(LOGO_IMAGE)
pygame.display.set_icon(logo)

# Control de FPS
clock = pygame.time.Clock()
fps = 60

#So Bala:
so_bala = pygame.mixer.Sound('assets/shoot.mp3')
so_bala.set_volume(0.7)

#So Explosio:
so_explosio = pygame.mixer.Sound('assets/so_explosio.mp3')
so_explosio.set_volume(0.2)

#So guanyador:
so_guanyador = pygame.mixer.Sound('assets/so_guanyador.mp3')
so_guanyador.set_volume(0.5)


def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

#So del joc:
ambient_music = pygame.mixer.Sound('assets/MusicaArcade.mp3')
music_chanel = pygame.mixer.Channel(0)
ambient_music.play()
ambient_music.set_volume(0.3)

while True:
    # contador
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # controlar trets de les naus
        if event.type == KEYDOWN:
            # jugador 1
            if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                temps_ultima_bala_jugador1 = current_time
                so_bala.play()

            # jugador 2
            if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom - 10, 4, 10))
                temps_ultima_bala_jugador2 = current_time
                so_bala.play()


    # Moviment del jugador 1
    keys = pygame.key.get_pressed()
    if explosio2 == False and explosio1 == False:
        if keys[K_a]:
            player_rect.x -= velocitat_nau
        if keys[K_d]:
            player_rect.x += velocitat_nau
        # Moviment del jugador 2
        if keys[K_LEFT]:
            player_rect2.x -= velocitat_nau2
        if keys[K_RIGHT]:
            player_rect2.x += velocitat_nau2

    # Mantenir al jugador dins de la pantalla:
    player_rect.clamp_ip(pantalla.get_rect())
    player_rect2.clamp_ip(pantalla.get_rect())

    # dibuixar el fons:
    imprimir_pantalla_fons(BACKGROUND_IMAGE)

    # Actualitzar i dibuixar les bales del jugador 1:
    for bala in bales_jugador1:  # bucle que recorre totes les bales
        bala.y -= velocitat_bales  # mou la bala
        if bala.bottom < 0 or bala.top > ALTURA:  # comprova que no ha sortit de la pantalla
            bales_jugador1.remove(bala)  # si ha sortit elimina la bala
        else:
            pantalla.blit(bala_imatge, bala)  # si no ha sortit la dibuixa
        # Detectar col·lisions jugador 2:
        if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
            print("BOOM 1!")
            vides2 -= 1
            bales_jugador1.remove(bala)  # eliminem la bala
            explosio2 = True
            temps_explosio = current_time
            # eliminem el jugador 2 (un temps)
            # anotem punts al jugador 2

    # Actualitzar i dibuixar les bales del jugador 2:
    for bala in bales_jugador2:
        bala.y += velocitat_bales
        if bala.bottom < 0 or bala.top > ALTURA:
            bales_jugador2.remove(bala)
        else:
            pantalla.blit(bala_imatge, bala)
        # Detectar col·lisions jugador 1:
        if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
            print("BOOM 2!")
            vides1 -= 1
            bales_jugador2.remove(bala)  # eliminem la bala
            explosio1 = True
            temps_explosio = current_time
            # eliminem el jugador 1 (un temps)
            # anotem punts al jugador 1

    # dibuixar els jugadors o explosio:
    # JUGADOR 1
    if explosio1 == False:
        pantalla.blit(player_image, player_rect)
    else:
        pantalla.blit(explossion_image, player_rect)
        so_explosio.play()
        so_explosio.set_volume(0.2)
        if current_time - temps_durada_explosio >= temps_explosio:
            explosio1 = False

    # JUGADOR2
    if explosio2 == False:
        pantalla.blit(player_image2, player_rect2)
    else:
        pantalla.blit(explossion_image, player_rect2)
        so_explosio.play()
        so_explosio.set_volume(0.2)
        if current_time - temps_durada_explosio >= temps_explosio:
            explosio2 = False


    # dibuixar vides
    # Vides Jugador 1:
    def dibuixar_vida1_jugador1():
        vides1j1 = pygame.image.load(('assets/vides.png')).convert()
        pantalla.blit(vides1j1, (310, 190))


    def dibuixar_vida2_jugador1():
        vides2j1 = pygame.image.load(('assets/vides.png')).convert()
        pantalla.blit(vides2j1, (300, 190))


    def dibuixar_vida3_jugador1():
        vides3j1 = pygame.image.load(('assets/vides.png')).convert()
        pantalla.blit(vides3j1, (290, 190))


    if vides2 > 0:
        if vides1 == 3:
            dibuixar_vida3_jugador1()
        if vides1 >= 2:
            dibuixar_vida2_jugador1()
        if vides1 >= 1:
            dibuixar_vida1_jugador1()
        if vides1 == 0:
            ambient_music.stop()
            mort = pygame.image.load(GAME_OVER2).convert()
            pantalla.blit(mort, (0, 0))
            so_guanyador.play()


    # Vides Jugador 2:
    def dibuixar_vida1_jugador2():
        vides1j2 = pygame.image.load(('assets/vides.png')).convert()
        pantalla.blit(vides1j2, (310, 10))


    def dibuixar_vida2_jugador2():
        vides2j2 = pygame.image.load(('assets/vides.png')).convert()
        pantalla.blit(vides2j2, (300, 10))


    def dibuixar_vida3_jugador2():
        vides3j2 = pygame.image.load(('assets/vides.png')).convert()
        pantalla.blit(vides3j2, (290, 10))


    if vides1 > 0:
        if vides2 == 3:
            dibuixar_vida3_jugador2()
        if vides2 >= 2:
            dibuixar_vida2_jugador2()
        if vides2 >= 1:
            dibuixar_vida1_jugador2()
        if vides2 == 0:
            ambient_music.stop()
            mort = pygame.image.load(GAME_OVER1).convert()
            pantalla.blit(mort, (0, 0))
            so_guanyador.play()




    pygame.display.update()
    clock.tick(fps)
