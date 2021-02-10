import pygame as pg

import sys, pygame
pygame.init()

size = width, height = 900, 600
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Nicholas Cage')

ball = pygame.image.load("head.png")
ballrect = pygame.Rect(100, 100, 256, 256)
mouse_flag=False

while 1:
    pos = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_flag=True
            pos = pygame.mouse.get_pos()
            ballrect = pygame.Rect(pos[0]-128, pos[1]-128, 256, 256)
    screen.fill(black)
    font = pygame.font.SysFont(None, 24)
    img = font.render('Click somewhere on the screen. DO IT!!11!', True, (100, 100, 100))
    screen.blit(img, (20, 20))
    if mouse_flag:
        screen.blit(ball, ballrect)
    pygame.display.update()

