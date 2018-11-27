#Autor: Michelle Sánchez Guerrero
#Descripción: videojuego de aliens vs astronauts

import pygame

#Dimensiones
ANCHO = 800
ALTO = 600

#Colores
BLANCO = (255, 255, 255)

#Estados
MENU = 1
SELECCION = 2
NIVELES = 3
NIVEL1 = 4
NIVEL2 = 5
INFINITO = 6

def dibujarMenu(ventana, menu, boton):
    ventana.blit(menu, (0,0))
    ventana.blit(boton, (ANCHO//2-146.5, ALTO//2-30))

def dibujarNivel1(ventana):
    ventana.fill(BLANCO)


def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #Imágenes
    #fondo = pygame.image.load("jardin.png")
    menu = pygame.image.load("menu.png")
    niveles = pygame.image.load("niveles.png")
    btnJugar = pygame.image.load("boton jugar.png")
    btnlvl1 = pygame.image.load("boton nivel1.png")
    btnlvl2 = pygame.image.load("boton nivel2.png")

    estado = MENU


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            #elif evento.type == pygame.MOUSEBUTTONUP: #Tipo de evento, en este caso cuando se oprime una tecla
             #   if estado == MENU: #Ver si el usuario oprimió la tecla hacia arriba
                    #spritePlanta.rect.bottom -= 15
                   # movimiento = ARRIBA
                #elif evento.key == pygame.K_DOWN:
                    #spritePlanta.rect.bottom += 15
                 #   movimiento = ABAJO
                #elif evento.key == pygame.K_z: #disparo
                 #   efecto.play()
                  #  spriteBala = pygame.sprite.Sprite()
                   # spriteBala.image = imgBala
                 #   #spriteBala.rect = imgBala.get_rect()
                  #  spriteBala.rect.left = spritePlanta.rect.width
                   # spriteBala.rect.bottom = spritePlanta.rect.bottom - 30
                    #listaBalas.append(spriteBala)
           # elif evento.type == pygame.MOUSEBUTTONDOWN:
            #    xm, ym = pygame.mouse.get_pos()
             #   xb = ANCHO//2 - 125
              #  yb = ALTO//2 - 37.5
               # anchoB = 250
                #altoB = 75
                #if xm>= xb and xm <= xb + anchoB and ym>= yb and ym<=yb+altoB:
                 #   estado = JUGANDO

        #Preguntar en qué estado está el juego
        if estado == MENU:
            dibujarMenu(ventana, menu, btnJugar)



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps


    # Después del ciclo principal
    pygame.quit()  # termina pygame


dibujar()