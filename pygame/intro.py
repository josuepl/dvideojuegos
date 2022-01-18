import pygame
from sys import exit
import time
from pygame.draw import rect

class Cuadrado:
    def __init__(self,posX, posY,tam,color):
        self.posX = posX
        self.posY = posY
        self.tam = tam
        self.color = color
        self.velx = 1
        self.vely = 1
        pass
    pass
    def comprobarL(self,maxX, maxY):
        if (self.posX + self.tam) >= maxX:
            self.velx = -1
            print("Limite X >:",self.posX )
        if (self.posY + self.tam) >= maxY:
            self.vely = -1
            print("Limite Y >:",self.posY )
        if self.posX  <= 0:
            self.velx = 1
            print("Limite X >:",self.posX )
        if self.posY <= 0:
            self.vely = 1
            print("Limite Y >:",self.posY )
        pass



pygame.init() # Inicializa todo el ambiente del videojuego en Pygame, funcion principal
              # Una vez inicializado el ambiente de trabajo, pygame podra invocar cualquiera de sus procedimientos
anchoV = 400    # Se define el ancho de la ventana
altoV = 400     # Se define el alto de la ventana 
pantalla = pygame.display.set_mode((anchoV,altoV))

#color RGB
rojo = (255, 0, 0) 
verde = (0, 255, 0)
azul = (0, 0, 255)
negro =(0, 0, 0)

#Posiciones iniciales
xIni = 0
yIni = 0

#Crear las instancias de la clase Cuadrado
cRojo = Cuadrado(100,100,40,rojo)
cVerde = Cuadrado(100,120,20,verde)
cAzul = Cuadrado(100,140,10,azul)


#Ciclo infinito de interacción con la libreria o videojuego
while True:
    # Espacio para agregar los elementos gráficos y de audio
    # Actualiza todos los elementos de la pantalla
    pygame.Surface.fill(pantalla,negro,None)
    for event in pygame.event.get(): # En cada iteración se considera el evento de salir
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit() # Se llama al procedimiento de salir de Pygame
            exit() # Se llama al procedimiento de salir del SO
    #print("Cuadrado R: ",cRojo.posX, " ", cRojo.velx)
    pygame.draw.rect(pantalla, cRojo.color, (cRojo.posX, cRojo.posY, cRojo.tam,cRojo.tam)) # (Superficie en la cual dibuja, color, (objeto rect{x,y, tamx, tamy} ))
    pygame.draw.rect(pantalla, cVerde.color, (cVerde.posX, cVerde.posY , cVerde.tam,cVerde.tam))
    pygame.draw.rect(pantalla, cAzul.color, (cAzul.posX, cAzul.posY , cAzul.tam,cAzul.tam))
    xIni = 3
    yIni = 3
    #Actualizar posicion de los cuadrados
    cRojo.posX = cRojo.posX + (xIni*cRojo.velx)
    cRojo.posY = (cRojo.posY*cRojo.vely)
    cVerde.posX += (xIni)*cVerde.velx
    cVerde.posY += (yIni)*cVerde.vely
    cAzul.posX = cAzul.posX*cAzul.velx
    cAzul.posY += (yIni)*cAzul.vely

    #Comprabar los limites de las posiciones x,y
    cRojo.comprobarL(400,400)
    cVerde.comprobarL(400,400)
    cAzul.comprobarL(400,400)

    time.sleep(.1)
    pygame.display.flip() # se muestra la pantalla creada
