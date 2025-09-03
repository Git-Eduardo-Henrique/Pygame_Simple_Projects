import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# Display vars
resolution = 720, 480
display = pygame.display.set_mode(resolution)
pygame.display.set_caption("Sons no Pygame")

# Positions vars
snake_x = resolution[0] / 2 - 25
snake_y = resolution[1] / 2 - 35

apple_x = randint(50, 670)
apple_y = randint(50, 430)

snake_list = []

# Text vars
font = pygame.font.SysFont("Arial", 40, True, True)
points = 0

# Sound vars
collison_sound = pygame.mixer.Sound("smw_coin.wav")

# Others
fps = pygame.time.Clock()

def draw_snake(snake_list): # draw snake in screen
    for pos in snake_list:
        pygame.draw.rect(display, (0, 255, 0), (pos[0], pos[1], 25, 25))

while True:
    fps.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        snake_x -= 10
    elif pygame.key.get_pressed()[K_d]:
        snake_x += 10
    elif pygame.key.get_pressed()[K_w]:
        snake_y -= 10
    elif pygame.key.get_pressed()[K_s]:
        snake_y += 10

    # In Screen
    display.fill((255, 255, 255))

    snake = pygame.draw.rect(display, (0, 255, 0), (snake_x, snake_y, 25, 25))
    apple = pygame.draw.rect(display, (255, 0, 0), (apple_x, apple_y, 25, 25))

    if snake.colliderect(apple):
        apple_x = randint(50, 670)
        apple_y = randint(50, 430)

        points += 1

        collison_sound.play()

    # Positions
    head_list = []
    head_list.append(snake_x)
    head_list.append(snake_y)

    snake_list.append(head_list)   

    draw_snake(snake_list)

    # Texts
    pts = f"Points: {points}"
    rend_pts = font.render(pts, True, (0, 0, 0))
    display.blit(rend_pts, (500, 20))

    pygame.display.update()
