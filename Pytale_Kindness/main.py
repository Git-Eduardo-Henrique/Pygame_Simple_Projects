import pygame as pyg
from pygame.locals import *
from save_name import Windows

human_name = Windows.choose_name_window()
print(f"Nome do humano caido: {human_name}")

running = True

window = pyg.display.set_mode((640, 480))
icon_image = pyg.image.load("Pytale_Kindness/sprites/green_soul_icon.png").convert_alpha()
pyg.display.set_icon(icon_image)

true_lab_image = pyg.image.load("Pytale_Kindness/sprites/true_lab.png").convert()
gaster_standing_image = pyg.image.load("Pytale_Kindness/sprites/gaster_standing.png").convert_alpha()

fps = pyg.time.Clock()

while running:
    fps.tick(30)

    pyg.display.set_caption(f"Pytale - Undertale Pygame 0.1 | FPS:{fps.get_fps():.0f}") 

    for event in pyg.event.get():
         if event.type == QUIT:
            running = False

    window.blit(true_lab_image, (0, 0))
    window.blit(gaster_standing_image, (282, 150))
    pyg.display.update()

pyg.quit()