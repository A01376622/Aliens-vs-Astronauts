#Autor: Michelle Sánchez Guerrero
#Descripción: videojuego de aliens vs astronauts

import pygame

#Dimensiones
ANCHO = 800
ALTO = 600

#Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

#Estados
MENU = 1
INSTRUCTIVO = 2
NIVELES = 3
NIVEL1 = 4
NIVEL2 = 5
INFINITO = 6
PERDER = 7
GANAR = 8

#Coordenadas slots
slotsX = [65, 175.5, 286, 396.5, 507]
slotsY = [216, 344, 472]

def dibujarMenu(ventana, menu, boton):
    ventana.blit(menu, (0,0))
    ventana.blit(boton, (ANCHO//2-146.5, ALTO//2-30))

def dibujarInstructivo(ventana, instructivo, boton):
    ventana.blit(instructivo, (0,0))
    ventana.blit(boton, (30, 50))

def dibujarNiveles(ventana, niveles, boton1, boton2):
    ventana.blit(niveles, (0,0))
    ventana.blit(boton1, (220, 280))
    ventana.blit(boton2, (450, 280))

def dibujarPartidaPerdida(ventana, perdida, boton):
    ventana.blit(perdida, (0,0))
    ventana.blit(boton, (475, 460))

def dibujarPartidaGanada(ventana, ganar, boton):
    ventana.blit(ganar, (0, 0))
    ventana.blit(boton, (485, 465))

def dibujarNivel1(ventana, jugando, slot, btnAl1, btnTr):
    ventana.blit(jugando, (0,0))
    #Slots (1 al 5, Primera columna)
    ventana.blit(slot, (slotsX[0], slotsY[0])) #Slot 1. Primera columna
    ventana.blit(slot, (slotsX[1], slotsY[0]))
    ventana.blit(slot, (slotsX[2], slotsY[0]))
    ventana.blit(slot, (slotsX[3], slotsY[0]))
    ventana.blit(slot, (slotsX[4], slotsY[0]))
    #Slots (6 al 10, Segunda columna)
    ventana.blit(slot, (slotsX[0], slotsY[1])) #Slot 6. Segunda columna
    ventana.blit(slot, (slotsX[1], slotsY[1]))
    ventana.blit(slot, (slotsX[2], slotsY[1]))
    ventana.blit(slot, (slotsX[3], slotsY[1]))
    ventana.blit(slot, (slotsX[4], slotsY[1]))
    #Slots (11 al 15, Tercera columna)
    ventana.blit(slot, (slotsX[0], slotsY[2])) #Slot 11. Tercera columna
    ventana.blit(slot, (slotsX[1], slotsY[2]))
    ventana.blit(slot, (slotsX[2], slotsY[2]))
    ventana.blit(slot, (slotsX[3], slotsY[2]))
    ventana.blit(slot, (slotsX[4], slotsY[2]))
    #Botones
    ventana.blit(btnAl1, (151, 42)) #Árbol
    #ventana.blit(btnAl1, (235, 42)) #Alien 1

def dibujarNivel2(ventana, jugando, slot, btnAl1, btnAl2):
    ventana.blit(jugando, (0, 0))
    # Slots (1 al 5, Primera columna)
    ventana.blit(slot, (slotsX[0], slotsY[0]))  # Slot 1. Primera columna
    ventana.blit(slot, (slotsX[1], slotsY[0]))
    ventana.blit(slot, (slotsX[2], slotsY[0]))
    ventana.blit(slot, (slotsX[3], slotsY[0]))
    ventana.blit(slot, (slotsX[4], slotsY[0]))
    # Slots (6 al 10, Segunda columna)
    ventana.blit(slot, (slotsX[0], slotsY[1]))  # Slot 6. Segunda columna
    ventana.blit(slot, (slotsX[1], slotsY[1]))
    ventana.blit(slot, (slotsX[2], slotsY[1]))
    ventana.blit(slot, (slotsX[3], slotsY[1]))
    ventana.blit(slot, (slotsX[4], slotsY[1]))
    # Slots (11 al 15, Tercera columna)
    ventana.blit(slot, (slotsX[0], slotsY[2]))  # Slot 11. Tercera columna
    ventana.blit(slot, (slotsX[1], slotsY[2]))
    ventana.blit(slot, (slotsX[2], slotsY[2]))
    ventana.blit(slot, (slotsX[3], slotsY[2]))
    ventana.blit(slot, (slotsX[4], slotsY[2]))
    # Botones
    ventana.blit(btnAl1, (151, 42))  # Árbol
    ventana.blit(btnAl2, (235, 42)) #Alien 1

def dibujarArbol(ventana, imgArbol, x, y):
    spriteArbol = pygame.sprite.Sprite()
    spriteArbol.image =imgArbol
    spriteArbol.rect = imgArbol.get_rect()
    spriteArbol.rect.left = x
    spriteArbol.rect.bottom = y
    ventana.blit(spriteArbol.image, spriteArbol.rect)

def dibujarAlien(ventana, imgAlien, x, y):
    spriteAlien = pygame.sprite.Sprite()
    spriteAlien.image =imgAlien
    spriteAlien.rect = imgAlien.get_rect()
    spriteAlien.rect.left = x
    spriteAlien.rect.bottom = y
    ventana.blit(spriteAlien.image, spriteAlien.rect)

def dibujarAlien2(ventana, imgAlien, x, y):
    spriteAlien2 = pygame.sprite.Sprite()
    spriteAlien2.image =imgAlien
    spriteAlien2.rect = imgAlien.get_rect()
    spriteAlien2.rect.left = x - 5
    spriteAlien2.rect.bottom = y
    ventana.blit(spriteAlien2.image, spriteAlien2.rect)

def crearAstronauta(imgNaut, x, y):
    spriteNaut = pygame.sprite.Sprite()
    spriteNaut.image = imgNaut
    spriteNaut.rect = imgNaut.get_rect()
    spriteNaut.rect.left = x
    spriteNaut.rect.bottom = y

    return spriteNaut

def dibujarAstronauta(ventana, listaAstronautas):
    for naut in listaAstronautas:
        ventana.blit(naut.image, naut.rect)

def actualizarAstronautas(listaAstronautas):
    for naut in listaAstronautas:
        naut.rect.left -= 0.01

def crearBala(imgBala, x, y):
    spriteBala = pygame.sprite.Sprite()
    spriteBala.image = imgBala
    spriteBala.rect = imgBala.get_rect()
    spriteBala.rect.left = x
    spriteBala.rect.bottom = y

    return spriteBala

def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)

def actualizarBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.left += 10

def verificarColisiones(listaBalas, listaAstronautas, listaVida, contador):
    #recorre las listas al revés
    for k in range(len(listaBalas)-1, -1, -1):
        bala = listaBalas[k]
        borrarBala = False

        for a in range(len(listaAstronautas)-1, -1, -1):
            naut = listaAstronautas[a]

            #Bala vs Naut
            xBala = bala.rect.left
            yBala = bala.rect.bottom
            xA, yA, anchoA, altoA = naut.rect

            if xBala >= xA and xBala <= xA + anchoA and yBala <= yA+100 and yBala >= yA:
                #listaAstronautas.remove(naut)  #borramos al enemigo (de la lista)
                listaVida.pop()

                borrarBala = True
                break

            if len(listaVida) == 0:
                listaAstronautas.remove(naut)
                contador -= 1

        if borrarBala:
            listaBalas.remove(bala)

def verificarSiGana(contador, listaVida):
    if len(listaVida) == 0:
        contador -= 1

    return contador

def verificarSiPierde(listaAstronautas):
    for a in range(0, len(listaAstronautas), 1):
        naut = listaAstronautas[a]

        xA, yA, anchoA, altoA = naut.rect

        if xA == 45:
            return True

        return False

def crearVidaAstronauta():

    return list(range(0,9))

def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #Imágenes
    menu = pygame.image.load("menu.png")
    instructivo = pygame.image.load("instructivo.png")
    niveles = pygame.image.load("niveles.png")
    jugando = pygame.image.load("jugando.png")
    perdida = pygame.image.load("perder.png")
    ganar = pygame.image.load("ganar.png")

    btnJugar = pygame.image.load("boton jugar.png")
    btnlvl1 = pygame.image.load("boton nivel1.png")
    btnlvl2 = pygame.image.load("boton nivel2.png")
    btnAlien100 = pygame.image.load("botonal100.png")
    btnAlien200 = pygame.image.load("botonal200.png")
    btnTree = pygame.image.load("botontr50.png")
    btnAventura = pygame.image.load("modav.png")
    slot = pygame.image.load("slot.png")
    btnMenu = pygame.image.load("botonmenu.png")
    btnSigNivel = pygame.image.load("botonsignivel.png")

    imgTree = pygame.image.load("tree.png")
    imgAlien100 = pygame.image.load("alien100.png")
    imgAlien200 = pygame.image.load("alien2.png")
    imgNaut1 = pygame.image.load("naut1.png")
    imgNautFW = pygame.image.load("nautfw.png")
    bala100 = pygame.image.load("balaAmarilla.png")
    bala200 = pygame.image.load("balaazul.png")

    #Lista balas para cada slot
    listaBalas1 = []
    listaBalas2 = []
    listaBalas3 = []
    listaBalas4 = []
    listaBalas5 = []
    listaBalas6 = []
    listaBalas7 = []
    listaBalas8 = []
    listaBalas9 = []
    listaBalas10 = []
    listaBalas11 = []
    listaBalas12 = []
    listaBalas13 = []
    listaBalas14 = []
    listaBalas15 = []

    #Astronautas
    listaAstronautas = []

    #Aliens - Slots
    alienSlot1 = 0
    alienSlot2 = 0
    alienSlot3 = 0
    alienSlot4 = 0
    alienSlot5 = 0
    alienSlot6 = 0
    alienSlot7 = 0
    alienSlot8 = 0
    alienSlot9 = 0
    alienSlot10 = 0
    alienSlot11 = 0
    alienSlot12 = 0
    alienSlot13 = 0
    alienSlot14 = 0
    alienSlot15 = 0


    #Medidas y
    treeY = 93
    difTreeY = 3
    alienY = 102
    difAlienX = 12
    nautY = 101

    #Elixir
    elixir = 2000

    #Tiempo
    timerBala1 = 0
    timerBala2 = 0
    timerBala3 = 0
    timerBala4 = 0
    timerBala5 = 0
    timerBala6 = 0
    timerBala7 = 0
    timerBala8 = 0
    timerBala9 = 0
    timerBala10 = 0
    timerBala11 = 0
    timerBala12 = 0
    timerBala13 = 0
    timerBala14 = 0
    timerBala15 = 0


    timerAstronauta1 = 0
    timerAstronauta2 = 0
    timerAstronauta3 = 0
    timerAstronauta4 = 0
    timerAstronauta5 = 0
    timerAstronauta6 = 0
    timerAstronauta7 = 0
    timerAstronauta8 = 0
    timerAstronauta9 = 0
    timerAstronauta10 = 0
    timerAstronauta11 = 0
    timerAstronauta12 = 0

    timerGeneral = 0


    #Texto
    fuente = pygame.font.SysFont("monospace", 30)

    contadorPrueba = 0

    restantesLvl1 = 12

    estado = MENU

    botonAlienON = 0



    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONUP: #Tipo de evento, en este caso cuando se oprime una tecla
                if estado == MENU:
                    xm, ym = pygame.mouse.get_pos()
                    xBtnJugar = ANCHO//2-146.5
                    yBtnJugar = ALTO//2-30
                    anchoBtnJugar = 293
                    altoBtnJugar = 103

                    if xm >= xBtnJugar and xm <= xBtnJugar + anchoBtnJugar and ym >= yBtnJugar and ym <= yBtnJugar + altoBtnJugar:
                        estado = INSTRUCTIVO

                elif estado == INSTRUCTIVO:
                    xm, ym = pygame.mouse.get_pos()
                    xBtnAv = 30
                    yBtnAv = 50
                    anchoBtnAv = 233
                    altoBtnAv = 201

                    if xm >= xBtnAv and xm <= xBtnAv + anchoBtnAv and ym >= yBtnAv and ym <= yBtnAv + altoBtnAv:
                        estado = NIVELES

                elif estado == NIVELES:
                    xm, ym = pygame.mouse.get_pos()
                    xBtnLvl1 = 220
                    yBtnLvl1 = 280
                    anchoBtnLvl1 = 141
                    altoBtnLvl1 = 134
                    xBtnLvl2 = 450
                    yBtnLvl2 = 280
                    anchoBtnLvl2 = 137
                    altoBtnLvl2 = 134

                    if xm >= xBtnLvl1 and xm <= xBtnLvl1 + anchoBtnLvl1 and ym >= yBtnLvl1 and ym <= yBtnLvl1 + altoBtnLvl1:
                        estado = NIVEL1

                    if xm >= xBtnLvl2 and xm <= xBtnLvl2 + anchoBtnLvl2 and ym >= yBtnLvl2 and ym <= yBtnLvl2 + altoBtnLvl2:
                        estado = NIVEL2

                elif estado == NIVEL1:
                    xm, ym = pygame.mouse.get_pos()
                    xBtnAlien = 150
                    yBtnAlien = 41
                    anchoBtnAlien = 83
                    altoBtnAlien = 92

                    anchoSlot = 103
                    altoSlot = 103

                    if xm >= xBtnAlien and xm <= xBtnAlien + anchoBtnAlien and ym >= yBtnAlien and ym <= yBtnAlien + altoBtnAlien and elixir > 100:
                        contadorPrueba += 1
                        botonAlienON = 1

                    if verificarSiPierde(listaAstronautas) == True:
                        estado = PERDER

                elif estado == NIVEL2:
                    xm, ym = pygame.mouse.get_pos()
                    xBtnAlien = 150
                    yBtnAlien = 41
                    anchoBtnAlien = 83
                    altoBtnAlien = 92

                    xBtnAlien2 = 235
                    yBtnAlien2 = 42
                    anchoBtnAlien2 = 83
                    altoBtnAlien2 = 93

                    anchoSlot = 103
                    altoSlot = 103

                    if xm >= xBtnAlien and xm <= xBtnAlien + anchoBtnAlien and ym >= yBtnAlien and ym <= yBtnAlien + altoBtnAlien and elixir > 100:
                        contadorPrueba += 1
                        botonAlienON = 1

                    if xm >= xBtnAlien2 and xm <= xBtnAlien2 + anchoBtnAlien2 and ym >= yBtnAlien2 and ym <= yBtnAlien2 + altoBtnAlien2 and elixir > 100:
                        contadorPrueba += 1
                        botonAlienON = 2

                    if verificarSiPierde(listaAstronautas) == True:
                        estado = PERDER

                elif estado == PERDER:
                    xm, ym = pygame.mouse.get_pos()
                    xBtnMn = 475
                    yBtnMn = 460
                    anchoBtnMn = 276
                    altoBtnMn = 107

                    if xm >= xBtnMn and xm <= xBtnMn + anchoBtnMn and ym >= yBtnMn and ym <= yBtnMn + altoBtnMn:
                        estado = MENU

                elif estado == GANAR:
                    xm, ym = pygame.mouse.get_pos()
                    xBtnSN = 485
                    yBtnSN = 465
                    anchoBtnSN = 278
                    altoBtnSN = 108

                    if xm >= xBtnSN and xm <= xBtnSN + anchoBtnSN and ym >= yBtnSN and ym <= yBtnSN + altoBtnSN:
                        estado = NIVELES


                if botonAlienON == 1:
                    xm, ym = pygame.mouse.get_pos()

                    if xm >= slotsX[0] and xm <= slotsX[0] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot: #1 slot
                        contadorPrueba += 1
                        elixir -= 100
                        #dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[0] + alienY)
                        alienSlot1 = 1
                        botonAlienON = 0

                    if xm >= slotsX[1] and xm <= slotsX[1] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot: #2 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[0] + alienY)
                        alienSlot2 = 1
                        botonAlienON = 0

                    if xm >= slotsX[2] and xm <= slotsX[2] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot: #3 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[0] + alienY)
                        alienSlot3 = 1
                        botonAlienON = 0

                    if xm >= slotsX[3] and xm <= slotsX[3] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot: #4 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[0] + alienY)
                        alienSlot4 = 1
                        botonAlienON = 0

                    if xm >= slotsX[4] and xm <= slotsX[4] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot:  #5 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[0] + alienY)
                        alienSlot5 = 1
                        botonAlienON = 0

                    if xm >= slotsX[0] and xm <= slotsX[0] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot:  #6 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[1] + alienY)
                        alienSlot6 = 1
                        botonAlienON = 0

                    if xm >= slotsX[1] and xm <= slotsX[1] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot:  #7 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[1] + alienY)
                        alienSlot7 = 1
                        botonAlienON = 0

                    if xm >= slotsX[2] and xm <= slotsX[2] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot: #8 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[1] + alienY)
                        alienSlot8 = 1
                        botonAlienON = 0

                    if xm >= slotsX[3] and xm <= slotsX[3] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot:  #9 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[1] + alienY)
                        alienSlot9 = 1
                        botonAlienON = 0

                    if xm >= slotsX[4] and xm <= slotsX[4] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot:  #10 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[1] + alienY)
                        alienSlot10 = 1
                        botonAlienON = 0

                    if xm >= slotsX[0] and xm <= slotsX[0] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot:  #11 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[2] + alienY)
                        alienSlot11 = 1
                        botonAlienON = 0

                    if xm >= slotsX[1] and xm <= slotsX[1] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot: #12 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[2] + alienY)
                        alienSlot12 = 1
                        botonAlienON = 0

                    if xm >= slotsX[2] and xm <= slotsX[2] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot:  #13 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[2] + alienY)
                        alienSlot13 = 1
                        botonAlienON = 0

                    if xm >= slotsX[3] and xm <= slotsX[3] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot:  #14 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[2] + alienY)
                        alienSlot14 = 1
                        botonAlienON = 0

                    if xm >= slotsX[4] and xm <= slotsX[4] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot:  #15 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[2] + alienY)
                        alienSlot15 = 1
                        botonAlienON = 0


                if botonAlienON == 2:
                    xm, ym = pygame.mouse.get_pos()

                    if xm >= slotsX[0] and xm <= slotsX[0] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot: #1 slot
                        contadorPrueba += 1
                        elixir -= 100
                        #dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[0] + alienY)
                        alienSlot1 = 2
                        botonAlienON = 0

                    if xm >= slotsX[1] and xm <= slotsX[1] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot: #2 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[0] + alienY)
                        alienSlot2 = 2
                        botonAlienON = 0

                    if xm >= slotsX[2] and xm <= slotsX[2] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot: #3 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[0] + alienY)
                        alienSlot3 = 2
                        botonAlienON = 0

                    if xm >= slotsX[3] and xm <= slotsX[3] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot: #4 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[0] + alienY)
                        alienSlot4 = 2
                        botonAlienON = 0

                    if xm >= slotsX[4] and xm <= slotsX[4] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot:  #5 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[0] + alienY)
                        alienSlot5 = 2
                        botonAlienON = 0

                    if xm >= slotsX[0] and xm <= slotsX[0] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot:  #6 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[1] + alienY)
                        alienSlot6 = 2
                        botonAlienON = 0

                    if xm >= slotsX[1] and xm <= slotsX[1] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot:  #7 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[1] + alienY)
                        alienSlot7 = 2
                        botonAlienON = 0

                    if xm >= slotsX[2] and xm <= slotsX[2] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot: #8 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[1] + alienY)
                        alienSlot8 = 2
                        botonAlienON = 0

                    if xm >= slotsX[3] and xm <= slotsX[3] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot:  #9 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[1] + alienY)
                        alienSlot9 = 2
                        botonAlienON = 0

                    if xm >= slotsX[4] and xm <= slotsX[4] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot:  #10 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[1] + alienY)
                        alienSlot10 = 2
                        botonAlienON = 0

                    if xm >= slotsX[0] and xm <= slotsX[0] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot:  #11 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[2] + alienY)
                        alienSlot11 = 2
                        botonAlienON = 0

                    if xm >= slotsX[1] and xm <= slotsX[1] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot: #12 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[2] + alienY)
                        alienSlot12 = 2
                        botonAlienON = 0

                    if xm >= slotsX[2] and xm <= slotsX[2] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot:  #13 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[2] + alienY)
                        alienSlot13 = 2
                        botonAlienON = 0

                    if xm >= slotsX[3] and xm <= slotsX[3] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot:  #14 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[2] + alienY)
                        alienSlot14 = 2
                        botonAlienON = 0

                    if xm >= slotsX[4] and xm <= slotsX[4] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot:  #15 slot
                        contadorPrueba += 1
                        elixir -= 100
                        dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[2] + alienY)
                        alienSlot15 = 2
                        botonAlienON = 0



        #Preguntar en qué estado está el juego
        if estado == MENU:
            dibujarMenu(ventana, menu, btnJugar)

        if estado == INSTRUCTIVO:
            dibujarInstructivo(ventana, instructivo, btnAventura)

        if estado == NIVELES:
            dibujarNiveles(ventana, niveles, btnlvl1, btnlvl2)

        if estado == NIVEL1:
            dibujarNivel1(ventana, jugando, slot, btnAlien100, btnTree)
            textoPrueba = fuente.render("Prueba: %d" % restantesLvl1, 1, BLANCO)
            textoElixir = fuente.render(("%d") % elixir, 1, BLANCO)
            ventana.blit(textoPrueba, (100, 300))
            ventana.blit(textoElixir, (55, 103))


            if timerAstronauta1 >= 10:
                timerAstronauta1 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[0]+100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta2 >= 30:
                timerAstronauta2 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[1]+100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta3 >= 50:
                timerAstronauta3 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[0]+100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta4 >= 70:
                timerAstronauta4 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[1]+100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta5 >= 80:
                timerAstronauta5 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[2]+100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta6 >= 100:
                timerAstronauta6 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[0]+100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta7 >= 110:
                timerAstronauta7 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[2]+100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta8 >= 120:
                timerAstronauta8 = -10000
                spriteAstronauta = crearAstronauta(imgNautFW, ANCHO, slotsY[1]+100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta9 >= 130:
                timerAstronauta9 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[2]+100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta10 >= 140:
                timerAstronauta10 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[1]+100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta11 >= 150:
                timerAstronauta11 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[0]+100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta12 >= 160:
                timerAstronauta12 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[2]+100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()



            if alienSlot1 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[0] + alienY)

                if timerBala1 >= 5:
                    timerBala1 = 0
                    spriteBala = crearBala(bala100, slotsX[0] + 43, slotsY[0] + 77)
                    listaBalas1.append(spriteBala)

                actualizarBalas(listaBalas1)
                dibujarBalas(ventana, listaBalas1)
                verificarColisiones(listaBalas1, listaAstronautas, vida, restantesLvl1)
                restantesLvl1 = verificarSiGana(restantesLvl1, vida)

            if alienSlot2 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[0] + alienY)

                if timerBala2 >= 5:
                    timerBala2 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[0] + 77)
                    listaBalas2.append(spriteBala)

                actualizarBalas(listaBalas2)
                dibujarBalas(ventana, listaBalas2)
                verificarColisiones(listaBalas2, listaAstronautas, vida, restantesLvl1)

            if alienSlot3 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[0] + alienY)

                if timerBala3 >= 5:
                    timerBala3 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[0] + 77)
                    listaBalas3.append(spriteBala)

                actualizarBalas(listaBalas3)
                dibujarBalas(ventana, listaBalas3)
                verificarColisiones(listaBalas3, listaAstronautas, vida, restantesLvl1)

            if alienSlot4 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[0] + alienY)

                if timerBala4 >= 5:
                    timerBala4 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[0] + 77)
                    listaBalas4.append(spriteBala)

                actualizarBalas(listaBalas4)
                dibujarBalas(ventana, listaBalas4)
                verificarColisiones(listaBalas4, listaAstronautas, vida, restantesLvl1)

            if alienSlot5 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[0] + alienY)

                if timerBala5 >= 5:
                    timerBala5 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[0] + 77)
                    listaBalas5.append(spriteBala)

                actualizarBalas(listaBalas5)
                dibujarBalas(ventana, listaBalas5)
                verificarColisiones(listaBalas5, listaAstronautas, vida, restantesLvl1)

            if alienSlot6 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[1] + alienY)

                if timerBala6 >= 5:
                    timerBala6 = 0
                    spriteBala = crearBala(bala100, slotsX[0] + 43, slotsY[1] + 77)
                    listaBalas6.append(spriteBala)

                actualizarBalas(listaBalas6)
                dibujarBalas(ventana, listaBalas6)
                verificarColisiones(listaBalas6, listaAstronautas, vida, restantesLvl1)

            if alienSlot7 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[1] + alienY)

                if timerBala7 >= 5:
                    timerBala7 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[1] + 77)
                    listaBalas7.append(spriteBala)

                actualizarBalas(listaBalas7)
                dibujarBalas(ventana, listaBalas7)
                verificarColisiones(listaBalas7, listaAstronautas, vida, restantesLvl1)

            if alienSlot8 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[1] + alienY)

                if timerBala8 >= 5:
                    timerBala8 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[1] + 77)
                    listaBalas8.append(spriteBala)

                actualizarBalas(listaBalas8)
                dibujarBalas(ventana, listaBalas8)
                verificarColisiones(listaBalas8, listaAstronautas, vida, restantesLvl1)

            if alienSlot9 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[1] + alienY)

                if timerBala9 >= 5:
                    timerBala9 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[1] + 77)
                    listaBalas9.append(spriteBala)

                actualizarBalas(listaBalas9)
                dibujarBalas(ventana, listaBalas9)
                verificarColisiones(listaBalas9, listaAstronautas, vida, restantesLvl1)

            if alienSlot10 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[1] + alienY)

                if timerBala10 >= 5:
                    timerBala10 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[1] + 77)
                    listaBalas10.append(spriteBala)

                actualizarBalas(listaBalas10)
                dibujarBalas(ventana, listaBalas10)
                verificarColisiones(listaBalas10, listaAstronautas, vida, restantesLvl1)

            if alienSlot11 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[2] + alienY)

                if timerBala11 >= 5:
                    timerBala11 = 0
                    spriteBala = crearBala(bala100, slotsX[0] + 43, slotsY[2] + 77)
                    listaBalas11.append(spriteBala)

                actualizarBalas(listaBalas11)
                dibujarBalas(ventana, listaBalas11)
                verificarColisiones(listaBalas11, listaAstronautas, vida, restantesLvl1)

            if alienSlot12 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[2] + alienY)

                if timerBala12 >= 5:
                    timerBala12 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[2] + 77)
                    listaBalas12.append(spriteBala)

                actualizarBalas(listaBalas12)
                dibujarBalas(ventana, listaBalas12)
                verificarColisiones(listaBalas12, listaAstronautas, vida, restantesLvl1)

            if alienSlot13 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[2] + alienY)

                if timerBala13 >= 5:
                    timerBala13 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[2] + 77)
                    listaBalas13.append(spriteBala)

                actualizarBalas(listaBalas13)
                dibujarBalas(ventana, listaBalas13)
                verificarColisiones(listaBalas13, listaAstronautas, vida, restantesLvl1)

            if alienSlot14 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[2] + alienY)

                if timerBala14 >= 5:
                    timerBala14 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[2] + 77)
                    listaBalas14.append(spriteBala)

                actualizarBalas(listaBalas14)
                dibujarBalas(ventana, listaBalas14)
                verificarColisiones(listaBalas14, listaAstronautas, vida, restantesLvl1)

            if alienSlot15 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[2] + alienY)

                if timerBala15 >= 5:
                    timerBala15 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[2] + 77)
                    listaBalas15.append(spriteBala)

                actualizarBalas(listaBalas15)
                dibujarBalas(ventana, listaBalas15)
                verificarColisiones(listaBalas15, listaAstronautas, vida, restantesLvl1)


            actualizarAstronautas(listaAstronautas)
            dibujarAstronauta(ventana, listaAstronautas)

            if verificarSiPierde(listaAstronautas):
                estado = PERDER

            if restantesLvl1 < -75:
                estado = GANAR

        if estado == NIVEL2:
            dibujarNivel2(ventana, jugando, slot, btnAlien100, btnAlien200)
            textoPrueba = fuente.render("Prueba: %d" % contadorPrueba, 1, BLANCO)
            textoElixir = fuente.render(("%d") % elixir, 1, BLANCO)
            ventana.blit(textoPrueba, (100, 300))
            ventana.blit(textoElixir, (55, 103))

            if timerAstronauta1 >= 10:
                timerAstronauta1 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[0] + 100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta2 >= 30:
                timerAstronauta2 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[1] + 100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta3 >= 50:
                timerAstronauta3 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[0] + 100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta4 >= 70:
                timerAstronauta4 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[1] + 100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta5 >= 80:
                timerAstronauta5 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[2] + 100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta6 >= 100:
                timerAstronauta6 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[0] + 100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta7 >= 110:
                timerAstronauta7 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[2] + 100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta8 >= 120:
                timerAstronauta8 = -10000
                spriteAstronauta = crearAstronauta(imgNautFW, ANCHO, slotsY[1] + 100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta9 >= 130:
                timerAstronauta9 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[2] + 100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta10 >= 140:
                timerAstronauta10 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[1] + 100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta11 >= 150:
                timerAstronauta11 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[0] + 100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if timerAstronauta12 >= 160:
                timerAstronauta12 = -10000
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, slotsY[2] + 100)
                listaAstronautas.append(spriteAstronauta)
                vida = crearVidaAstronauta()

            if alienSlot1 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[0] + alienY)

                if timerBala1 >= 5:
                    timerBala1 = 0
                    spriteBala = crearBala(bala100, slotsX[0] + 43, slotsY[0] + 77)
                    listaBalas1.append(spriteBala)

                actualizarBalas(listaBalas1)
                dibujarBalas(ventana, listaBalas1)
                verificarColisiones(listaBalas1, listaAstronautas, vida, restantesLvl1)
                restantesLvl1 = verificarSiGana(restantesLvl1, vida)

            if alienSlot2 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[0] + alienY)

                if timerBala2 >= 5:
                    timerBala2 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[0] + 77)
                    listaBalas2.append(spriteBala)

                actualizarBalas(listaBalas2)
                dibujarBalas(ventana, listaBalas2)
                verificarColisiones(listaBalas2, listaAstronautas, vida, restantesLvl1)

            if alienSlot3 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[0] + alienY)

                if timerBala3 >= 5:
                    timerBala3 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[0] + 77)
                    listaBalas3.append(spriteBala)

                actualizarBalas(listaBalas3)
                dibujarBalas(ventana, listaBalas3)
                verificarColisiones(listaBalas3, listaAstronautas, vida, restantesLvl1)

            if alienSlot4 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[0] + alienY)

                if timerBala4 >= 5:
                    timerBala4 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[0] + 77)
                    listaBalas4.append(spriteBala)

                actualizarBalas(listaBalas4)
                dibujarBalas(ventana, listaBalas4)
                verificarColisiones(listaBalas4, listaAstronautas, vida, restantesLvl1)

            if alienSlot5 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[0] + alienY)

                if timerBala5 >= 5:
                    timerBala5 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[0] + 77)
                    listaBalas5.append(spriteBala)

                actualizarBalas(listaBalas5)
                dibujarBalas(ventana, listaBalas5)
                verificarColisiones(listaBalas5, listaAstronautas, vida, restantesLvl1)

            if alienSlot6 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[1] + alienY)

                if timerBala6 >= 5:
                    timerBala6 = 0
                    spriteBala = crearBala(bala100, slotsX[0] + 43, slotsY[1] + 77)
                    listaBalas6.append(spriteBala)

                actualizarBalas(listaBalas6)
                dibujarBalas(ventana, listaBalas6)
                verificarColisiones(listaBalas6, listaAstronautas, vida, restantesLvl1)

            if alienSlot7 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[1] + alienY)

                if timerBala7 >= 5:
                    timerBala7 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[1] + 77)
                    listaBalas7.append(spriteBala)

                actualizarBalas(listaBalas7)
                dibujarBalas(ventana, listaBalas7)
                verificarColisiones(listaBalas7, listaAstronautas, vida, restantesLvl1)

            if alienSlot8 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[1] + alienY)

                if timerBala8 >= 5:
                    timerBala8 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[1] + 77)
                    listaBalas8.append(spriteBala)

                actualizarBalas(listaBalas8)
                dibujarBalas(ventana, listaBalas8)
                verificarColisiones(listaBalas8, listaAstronautas, vida, restantesLvl1)

            if alienSlot9 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[1] + alienY)

                if timerBala9 >= 5:
                    timerBala9 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[1] + 77)
                    listaBalas9.append(spriteBala)

                actualizarBalas(listaBalas9)
                dibujarBalas(ventana, listaBalas9)
                verificarColisiones(listaBalas9, listaAstronautas, vida, restantesLvl1)

            if alienSlot10 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[1] + alienY)

                if timerBala10 >= 5:
                    timerBala10 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[1] + 77)
                    listaBalas10.append(spriteBala)

                actualizarBalas(listaBalas10)
                dibujarBalas(ventana, listaBalas10)
                verificarColisiones(listaBalas10, listaAstronautas, vida, restantesLvl1)

            if alienSlot11 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[2] + alienY)

                if timerBala11 >= 5:
                    timerBala11 = 0
                    spriteBala = crearBala(bala100, slotsX[0] + 43, slotsY[2] + 77)
                    listaBalas11.append(spriteBala)

                actualizarBalas(listaBalas11)
                dibujarBalas(ventana, listaBalas11)
                verificarColisiones(listaBalas11, listaAstronautas, vida, restantesLvl1)

            if alienSlot12 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[2] + alienY)

                if timerBala12 >= 5:
                    timerBala12 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[2] + 77)
                    listaBalas12.append(spriteBala)

                actualizarBalas(listaBalas12)
                dibujarBalas(ventana, listaBalas12)
                verificarColisiones(listaBalas12, listaAstronautas, vida, restantesLvl1)

            if alienSlot13 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[2] + alienY)

                if timerBala13 >= 5:
                    timerBala13 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[2] + 77)
                    listaBalas13.append(spriteBala)

                actualizarBalas(listaBalas13)
                dibujarBalas(ventana, listaBalas13)
                verificarColisiones(listaBalas13, listaAstronautas, vida, restantesLvl1)

            if alienSlot14 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[2] + alienY)

                if timerBala14 >= 5:
                    timerBala14 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[2] + 77)
                    listaBalas14.append(spriteBala)

                actualizarBalas(listaBalas14)
                dibujarBalas(ventana, listaBalas14)
                verificarColisiones(listaBalas14, listaAstronautas, vida, restantesLvl1)

            if alienSlot15 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[2] + alienY)

                if timerBala15 >= 5:
                    timerBala15 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[2] + 77)
                    listaBalas15.append(spriteBala)

                actualizarBalas(listaBalas15)
                dibujarBalas(ventana, listaBalas15)
                verificarColisiones(listaBalas15, listaAstronautas, vida, restantesLvl1)


            #--------------ALIEN 2----------------
            #if alienSlot1 == 2:
             #   dibujarAlien2(ventana, imgAlien200, slotsX[0] + difAlienX-5, slotsY[0] + alienY)

            if alienSlot1 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[0] + difAlienX, slotsY[0] + alienY)

                if timerBala1 >= 5:
                    timerBala1 = 0
                    spriteBala = crearBala(bala200, slotsX[0] + 43, slotsY[0] + 77)
                    listaBalas1.append(spriteBala)

                actualizarBalas(listaBalas1)
                dibujarBalas(ventana, listaBalas1)
                verificarColisiones(listaBalas1, listaAstronautas, vida, restantesLvl1)
                restantesLvl1 = verificarSiGana(restantesLvl1, vida)

            if alienSlot2 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[1] + difAlienX, slotsY[0] + alienY)

                if timerBala2 >= 5:
                    timerBala2 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[0] + 77)
                    listaBalas2.append(spriteBala)

                actualizarBalas(listaBalas2)
                dibujarBalas(ventana, listaBalas2)
                verificarColisiones(listaBalas2, listaAstronautas, vida, restantesLvl1)

            if alienSlot3 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[2] + difAlienX, slotsY[0] + alienY)

                if timerBala3 >= 5:
                    timerBala3 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[0] + 77)
                    listaBalas3.append(spriteBala)

                actualizarBalas(listaBalas3)
                dibujarBalas(ventana, listaBalas3)
                verificarColisiones(listaBalas3, listaAstronautas, vida, restantesLvl1)

            if alienSlot4 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[3] + difAlienX, slotsY[0] + alienY)

                if timerBala4 >= 5:
                    timerBala4 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[0] + 77)
                    listaBalas4.append(spriteBala)

                actualizarBalas(listaBalas4)
                dibujarBalas(ventana, listaBalas4)
                verificarColisiones(listaBalas4, listaAstronautas, vida, restantesLvl1)

            if alienSlot5 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[4] + difAlienX, slotsY[0] + alienY)

                if timerBala5 >= 5:
                    timerBala5 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[0] + 77)
                    listaBalas5.append(spriteBala)

                actualizarBalas(listaBalas5)
                dibujarBalas(ventana, listaBalas5)
                verificarColisiones(listaBalas5, listaAstronautas, vida, restantesLvl1)

            if alienSlot6 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[0] + difAlienX, slotsY[1] + alienY)

                if timerBala6 >= 5:
                    timerBala6 = 0
                    spriteBala = crearBala(bala100, slotsX[0] + 43, slotsY[1] + 77)
                    listaBalas6.append(spriteBala)

                actualizarBalas(listaBalas6)
                dibujarBalas(ventana, listaBalas6)
                verificarColisiones(listaBalas6, listaAstronautas, vida, restantesLvl1)

            if alienSlot7 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[1] + difAlienX, slotsY[1] + alienY)

                if timerBala7 >= 5:
                    timerBala7 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[1] + 77)
                    listaBalas7.append(spriteBala)

                actualizarBalas(listaBalas7)
                dibujarBalas(ventana, listaBalas7)
                verificarColisiones(listaBalas7, listaAstronautas, vida, restantesLvl1)

            if alienSlot8 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[2] + difAlienX, slotsY[1] + alienY)

                if timerBala8 >= 5:
                    timerBala8 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[1] + 77)
                    listaBalas8.append(spriteBala)

                actualizarBalas(listaBalas8)
                dibujarBalas(ventana, listaBalas8)
                verificarColisiones(listaBalas8, listaAstronautas, vida, restantesLvl1)

            if alienSlot9 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[3] + difAlienX, slotsY[1] + alienY)

                if timerBala9 >= 5:
                    timerBala9 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[1] + 77)
                    listaBalas9.append(spriteBala)

                actualizarBalas(listaBalas9)
                dibujarBalas(ventana, listaBalas9)
                verificarColisiones(listaBalas9, listaAstronautas, vida, restantesLvl1)

            if alienSlot10 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[4] + difAlienX, slotsY[1] + alienY)

                if timerBala10 >= 5:
                    timerBala10 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[1] + 77)
                    listaBalas10.append(spriteBala)

                actualizarBalas(listaBalas10)
                dibujarBalas(ventana, listaBalas10)
                verificarColisiones(listaBalas10, listaAstronautas, vida, restantesLvl1)

            if alienSlot11 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[0] + difAlienX, slotsY[2] + alienY)

                if timerBala11 >= 5:
                    timerBala11 = 0
                    spriteBala = crearBala(bala100, slotsX[0] + 43, slotsY[2] + 77)
                    listaBalas11.append(spriteBala)

                actualizarBalas(listaBalas11)
                dibujarBalas(ventana, listaBalas11)
                verificarColisiones(listaBalas11, listaAstronautas, vida, restantesLvl1)

            if alienSlot12 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[1] + difAlienX, slotsY[2] + alienY)

                if timerBala12 >= 5:
                    timerBala12 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[2] + 77)
                    listaBalas12.append(spriteBala)

                actualizarBalas(listaBalas12)
                dibujarBalas(ventana, listaBalas12)
                verificarColisiones(listaBalas12, listaAstronautas, vida, restantesLvl1)

            if alienSlot13 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[2] + difAlienX, slotsY[2] + alienY)

                if timerBala13 >= 5:
                    timerBala13 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[2] + 77)
                    listaBalas13.append(spriteBala)

                actualizarBalas(listaBalas13)
                dibujarBalas(ventana, listaBalas13)
                verificarColisiones(listaBalas13, listaAstronautas, vida, restantesLvl1)

            if alienSlot14 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[3] + difAlienX, slotsY[2] + alienY)

                if timerBala14 >= 5:
                    timerBala14 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[2] + 77)
                    listaBalas14.append(spriteBala)

                actualizarBalas(listaBalas14)
                dibujarBalas(ventana, listaBalas14)
                verificarColisiones(listaBalas14, listaAstronautas, vida, restantesLvl1)

            if alienSlot15 == 2:
                dibujarAlien2(ventana, imgAlien200, slotsX[4] + difAlienX, slotsY[2] + alienY)

                if timerBala15 >= 5:
                    timerBala15 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[2] + 77)
                    listaBalas15.append(spriteBala)

                actualizarBalas(listaBalas15)
                dibujarBalas(ventana, listaBalas15)
                verificarColisiones(listaBalas15, listaAstronautas, vida, restantesLvl1)

            actualizarAstronautas(listaAstronautas)
            dibujarAstronauta(ventana, listaAstronautas)

            if verificarSiPierde(listaAstronautas):
                estado = PERDER

            if restantesLvl1 < -75:
                estado = GANAR

        if estado == GANAR:
            dibujarPartidaGanada(ventana, ganar, btnSigNivel)

        if estado == PERDER:
            dibujarPartidaPerdida(ventana, perdida, btnMenu)



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

        timerBala1 += 1/10
        timerBala2 += 1 / 10
        timerBala3 += 1 / 10
        timerBala4 += 1 / 10
        timerBala5 += 1 / 10
        timerBala6 += 1 / 10
        timerBala7 += 1 / 10
        timerBala8 += 1 / 10
        timerBala9 += 1 / 10
        timerBala10 += 1 / 10
        timerBala11 += 1 / 10
        timerBala12 += 1 / 10
        timerBala13 += 1 / 10
        timerBala14 += 1 / 10
        timerBala15 += 1 / 10

        timerAstronauta1 += 1/10
        timerAstronauta2 += 1 / 10
        timerAstronauta3 += 1 / 10
        timerAstronauta4 += 1 / 10
        timerAstronauta5 += 1 / 10
        timerAstronauta6 += 1 / 10
        timerAstronauta7 += 1 / 10
        timerAstronauta8 += 1 / 10
        timerAstronauta9 += 1 / 10
        timerAstronauta10 += 1 / 10
        timerAstronauta11 += 1 / 10
        timerAstronauta12 += 1 / 10

        timerGeneral += 1/10


    # Después del ciclo principal
    pygame.quit()  # termina pygame


dibujar()