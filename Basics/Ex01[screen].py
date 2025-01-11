import pygame
from pygame.locals import *
from sys import exit

pygame.init() # inicia o modulo do pygame

screen = pygame.display.set_mode((720, 480)) # difine a tela (largura, altura)
pygame.display.set_caption("Game Test") # muda o nome da janela

# loop principal
while True:
    for event in pygame.event.get(): #d etecta cada evento
        # fechar a tela apertando no X
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update() # fica atualizando a tela do jogo