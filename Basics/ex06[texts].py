import pygame as pyg
from pygame.locals import *
from sys import exit
from random import randint

pyg.init()

resolution = 720, 480
display = pyg.display.set_mode(resolution)
pyg.display.set_caption("texto de pontos")

# fonte, tamanho, negrito, italico
font = pyg.font.SysFont("Arial", 40, True, True)

x = resolution[0] / 2 - 25
y = resolution[1] / 2 - 35

x_blue = randint(50, 670)
y_blue = randint(50, 430)

points = 0

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

    pts = f"Points: {points}"
    # variavel_da_fonte.render(texto, True, cor rgb)
    rend_pts = font.render(pts, True, (255, 255, 255))

    red_rect = pyg.draw.rect(display, (255, 0, 0), (x, y, 50, 50))
    blue_rect = pyg.draw.rect(display, (0, 0, 255), (x_blue, y_blue, 50, 50))

    if red_rect.colliderect(blue_rect):
        x_blue = randint(50, 670)
        y_blue = randint(50, 430)

        points += 1

    # para mostrar o texto na tela
    display.blit(rend_pts, (500, 20)) # variavel com render, tupla com x e y
    pyg.display.update()
