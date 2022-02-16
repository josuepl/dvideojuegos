import pygame, sys, time
from pygame.locals import *

pygame.init()
fondo = (255, 255, 255)
altoY = 600
anchoX = 800
posIx = 30
posIy = 100

pantalla = pygame.display.set_mode((anchoX, altoY))

sprPr = pygame.transform.scale2x(pygame.image.load(r"Sprite\linkP2.png"))

frame_act = 0
frame_act2 = 0
frames = 12
fr_ancho = 48
fr_alto = 64
cont = 0

spriteL = pygame.sprite.Sprite
spriteL.image = sprPr
spriteL.rect = spriteL.image.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for spl in range(12):
        pantalla.fill([0, 0, 0])  
    #movimiento derecha
        n_rec = pygame.Rect((frame_act * fr_ancho ,fr_alto,fr_ancho,fr_alto))
        print("frame: ",frame_act, "posX: ",frame_act * fr_ancho)
        pantalla.blit(spriteL.image.subsurface(n_rec),(posIx + cont,0))
        if (frame_act >= frames - 1):
            frame_act = 0
        else:
            frame_act += 1
        cont+=1
    #movimiento izquierda
        n_rec = pygame.Rect((frame_act * fr_ancho ,200,fr_ancho,fr_alto))
        print("frame: ",frame_act, "posX: ",frame_act * fr_ancho)
        pantalla.blit(spriteL.image.subsurface(n_rec),(posIx + cont,100))
        if (frame_act >= frames - 1):
            frame_act = 0
        else:
            frame_act += 1
        cont+=1
    #movimiento arriba
        n_rec = pygame.Rect((frame_act * fr_ancho ,4*fr_alto,fr_ancho,fr_alto))
        print("frame: ",frame_act, "posX: ",frame_act * fr_ancho)
        pantalla.blit(spriteL.image.subsurface(n_rec),(posIx + cont,300))
        if (frame_act >= frames - 1):
            frame_act = 0
        else:
            frame_act += 1
        cont+=1
    #movimiento abajo
        n_rec = pygame.Rect((frame_act * fr_ancho ,6*fr_alto,fr_ancho,fr_alto))
        print("frame: ",frame_act, "posX: ",frame_act * fr_ancho)
        pantalla.blit(spriteL.image.subsurface(n_rec),(posIx + cont,200))
        if (frame_act >= frames - 1):
            frame_act = 0
        else:
            frame_act += 1
        cont+=1

        pygame.display.update()
        time.sleep(.1)
