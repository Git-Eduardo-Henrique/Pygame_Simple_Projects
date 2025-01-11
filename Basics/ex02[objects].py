import pygame as pyg
from pygame.locals import *
from sys import exit

pyg.init()

screen = pyg.display.set_mode((720, 480))
pyg.display.set_caption("Objects Test")

while True:
    for event in pyg.event.get():
        if event.type == QUIT:
            pyg.quit()
            exit()

    # desenha um formas na tela 
    # (obj_tela, (cor rgb), (pos-x, pos-y, comprimento, altura))
    pyg.draw.rect(screen, (255, 0, 0), (200, 300, 50, 50))
    # (obj_tela, (cor rgb), (pos-x, pos-y), raio do circulo)
    pyg.draw.circle(screen, (0, 0, 200), (300, 260), 40)
    # (obj_tela, (cor rgb), (pos-x, pos-y "comeco da linha"), (pos-x, pos-y "final linha"), grosura)
    pyg.draw.line(screen, (200, 200, 0), (390, 0), (390, 600), 5)

    pyg.display.update() 