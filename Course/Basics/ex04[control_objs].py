import pygame as pyg
from pygame.locals import *
from sys import exit

pyg.init()

resolution = 720, 480
display = pyg.display.set_mode(resolution)
pyg.display.set_caption("controlando objetos")

x = resolution[0] / 2 - 25
y = resolution[1] / 2 - 35

fps = pyg.time.Clock()

while True:
    fps.tick(60)
    
    for event in pyg.event.get():
        if event.type == QUIT:
            pyg.quit()
            exit()

        '''
        apenas clicar 

        if event.type == KEYDOWN: 
            if event.key == K_a:
                x -= 20
            elif event.key == K_d:
                x += 20
            elif event.key == K_w: 
                y -= 20
            elif event.key == K_s: 
                y += 20
        '''

    # caso mantenha a tecla precionada
    if pyg.key.get_pressed()[K_a]:
        x -= 5
    elif pyg.key.get_pressed()[K_d]:
        x += 5
    elif pyg.key.get_pressed()[K_w]:
        y -= 5
    elif pyg.key.get_pressed()[K_s]:
        y += 5

    display.fill((0, 0, 0))

    pyg.draw.rect(display, (255, 0, 0), (x, y, 50, 70))

    pyg.display.update()
