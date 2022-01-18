import pygame
from sys import exit
from Cuadrado import Cuadrado

pygame.init()
anchoV = 400    # Se define el ancho de la ventana
altoV = 400
tamPant = (anchoV,altoV)
pantalla = pygame.display.set_mode(tamPant)

reloj = pygame.time.Clock() # Se define la variable reloj manejador de refresco de pantalla

cRojo = Cuadrado(100,100,40,(255,50,50))
while True:
    pygame.Surface.fill(pantalla,(0,0,0),None)
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(pantalla, cRojo.color, (cRojo.posX, cRojo.posY, cRojo.tam,cRojo.tam)) # (Superficie en la cual dibuja, color, (objeto rect{x,y, tamx, tamy} ))
    xIni = 3
    yIni = 3
    #Actualizar posicion de los cuadrados
    cRojo.posX = cRojo.posX + (xIni*cRojo.velx)
    cRojo.posY = (cRojo.posY*cRojo.vely)
    cRojo.comprobarL(400,400)
    pygame.display.update()
    reloj.tick(120) # Define la tasa de 60 FPS
    pass