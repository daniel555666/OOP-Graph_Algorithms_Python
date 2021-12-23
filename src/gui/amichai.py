import sys

import pygame
import random
pygame.init()
black = [0, 0, 0]
white = [255, 255, 255]
size = [1200, 700]
scr = pygame.display.set_mode(size)
pygame.display.set_caption("EX3 Dolev Daniel Yakov")
snow_list = []
for i in range(50):
    x = random.randrange(0, 700)
    y = random.randrange(0, 600)
    snow_list.append([x, y])
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    scr.fill(black)
    for i in range(len(snow_list)):
        pygame.draw.circle(scr, white, snow_list[i], 2)
        snow_list[i][1] += 1
        if snow_list[i][1] > 400:
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            x = random.randrange(0, 400)
            snow_list[i][0] = x
    pygame.display.flip()
    clock.tick(20)
pygame.quit()
sys.exit()

# import pygame, sys
# from pygame.locals import *
# pygame.init()
# FPS = 20
# fpsClock = pygame.time.Clock()
# Displaysrf = pygame.display.set_mode((700, 600), 0, 20)
# pygame.display.set_caption('Animation')
# white = (255, 255, 255)
# dImg = pygame.image.load('img2.png')
# dx = 10
# dy = 10
# direction = 'right'
# while True:
#     Displaysrf.fill(white)
#     if direction == 'right':
#         dx += 5
#         if dx == 280:
#             direction = 'down'
#     elif direction == 'down':
#         dy += 5
#         if dy == 220:
#             direction = 'left'
#     elif direction == 'left':
#         dx -= 5
#         if dx == 10:
#             direction = 'up'
#     elif direction == 'up':
#         dy -= 5
#         if dy == 10:
#             direction = 'right'
#     Displaysrf.blit(dImg, (dx, dy))
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()
#     fpsClock.tick(FPS)

# from pygame import mixer
# mixer.init()
# mixer.music.load("music1.ogg")
# mixer.music.set_volume(0.5)
# mixer.music.play()
# while True:
#     print("Press 'p' to pause, 'r' to resume")
#     print("Press 'e' to end the program")
#     enter = input("  ")
#     if enter == 'p':
#         mixer.music.pause()
#     elif enter == 'r':
#         mixer.music.unpause()
#     elif enter == 'e':
#         mixer.music.stop()
#         break

# import pygame
# import sys
# pygame.init()
# s = (600, 500)
# screen = pygame.display.set_mode(s)
# color_white = (255,255,255)
# color_light = (180,180,180)
# color_dark = (110,110,110)
# width = screen.get_width()
# height = screen.get_height()
# smallfont = pygame.font.SysFont('Arial',30)
# text = smallfont.render('Quit' , True , color_white)
# while True:
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             pygame.quit()
#         if e.type == pygame.MOUSEBUTTONDOWN:
#             if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
#                 pygame.quit()
#                 sys.exit()
#     screen.fill((0,0,0))
#     mouse = pygame.mouse.get_pos()
#     if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
#         pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
#     else:
#         pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
#     screen.blit(text , (width/2+50,height/2))
#     pygame.display.update()

# import sys
#
# import pygame
# pygame.init()
# w=550;
# h=400
# scr = pygame.display.set_mode( (w, h) )
# pygame.display.set_caption('click on image')
# image = pygame.image.load("img.jpg").convert()
# x = 20;
# y = 30;
# scr.blit(image, (x,y))
# pygame.display.flip()
# running = True
# while (running):
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             running = False
#         if e.type == pygame.MOUSEBUTTONDOWN:
#             x, y = e.pos
#             if image.get_rect().collidepoint(x, y):
#                 print('clicked on image:', str(x), ",", str(y))
# pygame.quit()
# sys.exit()

# import sys
#
# import pygame
# pygame.init()
# window = pygame.display.set_mode((600, 600))
# pygame.display.set_caption("Drawing Design")
# x = 300
# y = 300
# width = 20
# height = 20
# vel = 10
# run = True
# while run:
#     pygame.time.delay(10)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and x > 0:
#         x -= vel
#     if keys[pygame.K_RIGHT] and x < 600 - width:
#         x += vel
#     if keys[pygame.K_UP] and y > 0:
#         y -= vel
#     if keys[pygame.K_DOWN] and y < 600 - height:
#         y += vel
#     pygame.draw.rect(window, (255, 255, 255), (x, y, width, height))
#     pygame.display.update()
# pygame.quit()
# sys.exit()

# # from https://pythonguides.com/python-pygame-tutorial/
# import sys
#
# import pygame
#
#
# def test_py_game_1():
#     pygame.init()
#     scr = pygame.display.set_mode((600, 500))
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         scr.fill((255, 255, 255))
#         pygame.draw.circle(scr, (200, 0, 0), (250, 250), 80)
#         color = (0, 0, 255)
#         pygame.draw.rect(scr, color, pygame.Rect(60, 60, 100, 100))
#         color = (0, 255, 0)
#         pygame.draw.line(scr, color, (40, 300), (140, 380), 6)
#         purple = (102, 0, 102)
#         pygame.draw.polygon(scr, purple,
#                             ((346, 0), (491, 106), (436, 277), (256, 277), (200, 106)))
#         pygame.display.flip()
#     pygame.quit()
#     sys.exit()
#
# test_py_game_1()



# first example
# import pygame
#
# WIDTH, HEIGHT = (900, 500)
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#
#
# def game():
#     run = True
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#
#     WIN.fill(216, 242, 230)
#     pygame.display.update()
#     pygame.quit()
#
#
# if __name__ == '__main__':
#     game()
