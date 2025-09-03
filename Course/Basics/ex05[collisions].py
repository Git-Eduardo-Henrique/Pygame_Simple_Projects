import pygame as pyg
from pygame.locals import *
from sys import exit
from random import randint

pyg.init()

resolution = 720, 480
display = pyg.display.set_mode(resolution)
pyg.display.set_caption("colições")

x = resolution[0] / 2 - 25
y = resolution[1] / 2 - 35

# pos azul
x_blue = randint(50, 670)
y_blue = randint(50, 430)

fps = pyg.time.Clock()

while True:
    fps.tick(60)
    
    for event in pyg.event.get():
        if event.type == QUIT:
            pyg.quit()
            exit()

    if pyg.key.get_pressed()[K_a]:
        x -= 10
    elif pyg.key.get_pressed()[K_d]:
        x += 10
    elif pyg.key.get_pressed()[K_w]:
        y -= 10
    elif pyg.key.get_pressed()[K_s]:
        y += 10

    display.fill((0, 0, 0))

    # guardar em variaveis para modificar dps
    red_rect = pyg.draw.rect(display, (255, 0, 0), (x, y, 50, 50))
    blue_rect = pyg.draw.rect(display, (0, 0, 255), (x_blue, y_blue, 50, 50))

    # se colidir o azul vai para um local aleatorio
    if red_rect.colliderect(blue_rect):
        x_blue = randint(50, 670)
        y_blue = randint(50, 430)

    pyg.display.update()
