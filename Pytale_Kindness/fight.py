import pygame as pyg
from pygame.locals import *
from sys import exit

pyg.init()

window = pyg.display.set_mode((640, 480))

icon_image = pyg.image.load("Pytale_Kindness/sprites/green_soul_icon.png")
pyg.display.set_icon(icon_image)

fps = pyg.time.Clock()

hud_font = pyg.font.Font("Pytale_Kindness/determination_mono.ttf", 28)
big_hud_font = pyg.font.Font("Pytale_Kindness/determination_mono.ttf", 42)

love = 19
base_life = life = 20 + (love - 1) * 4 if love > 0 else 20

human_name = "CHARA"

while True:
    window.fill((0, 0, 0))

    fps.tick(30)
    pyg.display.set_caption(f"Pytale - Undertale Pygame 0.1 | FPS:{fps.get_fps():.0f}") 

    rend_name_txt = hud_font.render(f"{human_name}", True, (255, 255, 255))
    rend_love_text = hud_font.render(f"LV{love}", True, (255, 255, 255))
    rend_life_text = hud_font.render(f"{life}/{base_life}", True, (255, 255, 255))
    
    rend_fight_text = big_hud_font.render(f"FIGHT", True, (255, 128, 0))
    rend_act_text = big_hud_font.render(f"ACT", True, (255, 128, 0))
    rend_item_text = big_hud_font.render(f"ITEM", True, (255, 128, 0))
    rend_mercy_text = big_hud_font.render(f"MERCY", True, (255, 128, 0))

    for event in pyg.event.get():
         if event.type == QUIT:
            pyg.quit()
            exit()

    window.blit(rend_name_txt, (55, 360))
    window.blit(rend_love_text, (170, 360))
    window.blit(rend_life_text, (450, 360))

    window.blit(rend_fight_text, (50, 410))
    window.blit(rend_act_text, (210, 410))
    window.blit(rend_item_text, (340, 410))
    window.blit(rend_mercy_text, (480, 410))
    pyg.display.update()