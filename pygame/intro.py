import pygame
from sys import exit

from pygame.draw import rect

pygame.init() # Inicializa todo el ambiente del videojuego en Pygame, funcion principal
              # Una vez inicializado el ambiente de trabajo, pygame podra invocar cualquiera de sus procedimientos
anchoV = 400    # Se define el ancho de la ventana
altoV = 400     # Se define el alto de la ventana 
pantalla = pygame.display.set_mode((anchoV,altoV))

#color RGB
rojo = (255, 0, 0) 
verde = (0, 255, 0)
azul = (0, 0, 255)

#Ciclo infinito de interacción con la libreria o videojuego
while True:
    # Espacio para agregar los elementos gráficos y de audio
    # Actualiza todos los elementos de la pantalla

    for event in pygame.event.get(): # En cada iteración se considera el evento de salir
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit() # Se llama al procedimiento de salir de Pygame
            exit() # Se llama al procedimiento de salir del SO
    pygame.draw.rect(pantalla, rojo, (100, 100, 100,10))
    pygame.draw.rect(pantalla, verde, (100, 120, 10,20))
    pygame.draw.rect(pantalla, azul, (100, 140, 40,40))
    pygame.display.update() # se muestra la pantalla creada 
