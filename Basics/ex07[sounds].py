import pygame
from pygame.locals import *
from sys import exit, path
from random import randint

pygame.init()

resolution = 720, 480
display = pygame.display.set_mode(resolution)
pygame.display.set_caption("Sons no Pygame")

font = pygame.font.SysFont("Arial", 40, True, True)

x = resolution[0] / 2 - 25
y = resolution[1] / 2 - 35

x_blue = randint(50, 670)
y_blue = randint(50, 430)

points = 0

fps = pygame.time.Clock()

# carrega um som para o pygame | apenas WAV
collison_sound = pygame.mixer.Sound("smw_coin.wav")

while True:
    fps.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x -= 10
    elif pygame.key.get_pressed()[K_d]:
        x += 10
    elif pygame.key.get_pressed()[K_w]:
        y -= 10
    elif pygame.key.get_pressed()[K_s]:
        y += 10

    display.fill((0, 0, 0))

    pts = f"Points: {points}"
    rend_pts = font.render(pts, True, (255, 255, 255))

    red_rect = pygame.draw.rect(display, (255, 0, 0), (x, y, 50, 50))
    blue_rect = pygame.draw.rect(display, (0, 0, 255), (x_blue, y_blue, 50, 50))

    if red_rect.colliderect(blue_rect):
        x_blue = randint(50, 670)
        y_blue = randint(50, 430)

        points += 1

        collison_sound.play() # toca o som

    display.blit(rend_pts, (500, 20))
    pygame.display.update()