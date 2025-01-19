import pygame as pyg
from pygame.locals import *
from sys import exit

pyg.init()

resolution = 720, 480

screen = pyg.display.set_mode(resolution)
pyg.display.set_caption("Movendo objetos")

# pos (meio do x = metade da tela - metade do objeto)
x = resolution[0] / 2 - 25
y = 0

# para definir o fps
fps = pyg.time.Clock()

while True:
    # recebe tupla e preenche a tela com a cor rgb
    screen.fill((0, 0, 0))

    fps.tick(60) # define o fps

    for event in pyg.event.get():
        if event.type == QUIT:
            pyg.quit()
            exit()

    # recebe coordenadas x e y
    pyg.draw.rect(screen, (255, 0, 0), (x, y, 50, 70))
    
    # realiza o movimento até a borda da tela, depois retorna para cima
    y += 1

    if y >= resolution[1]:
        y = 0

    pyg.display.update()
