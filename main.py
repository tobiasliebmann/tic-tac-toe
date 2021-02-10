import sys

import pygame

import numpy as np

import random


def position_test(input_pos, test_dimension):
    """

    :param input_pos:
    :param test_dimension:
    :return:
    """
    if 0 <= input_pos <= test_dimension / 3:
        return 0
    elif test_dimension / 3 < input_pos <= 2 * test_dimension / 3:
        return test_dimension / 3
    else:
        return 2 * test_dimension / 3


pygame.init()

player1_flag = True

im_width = 300
im_height = 300

size = width, height = 900, 900
speed = [1, 1]
black = 0, 0, 0

outer_circle_radius = 140
inner_circle_radius = 120

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic-Tac-Toe')

screen.fill(black)

while 1:
    pygame.draw.line(screen, (255, 0, 0), (0, height / 3), (width, height / 3))
    pygame.draw.line(screen, (255, 0, 0), (0, 2 * height / 3), (width, 2 * height / 3))
    pygame.draw.line(screen, (255, 0, 0), (width / 3, 0), (width / 3, height))
    pygame.draw.line(screen, (255, 0, 0), (2 * width / 3, 0), (2 * width / 3, height))
    #    font = pygame.font.SysFont(None, 24)
    #    img = font.render('Click somewhere on the screen. DO IT!!11!', True, (100, 100, 100))
    #    screen.blit(img, (20, 20))
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #nic_cage_rect = pygame.Rect(position_test(pos[0], width), position_test(pos[1], height), 256, 256)
            line_start_x = position_test(pos[0], width)
            line_start_y = position_test(pos[1], height)
            if player1_flag:
                pygame.draw.line(screen, (0, 255, 0), (line_start_x, line_start_y), (line_start_x + height/3, line_start_y + height/3))
                pygame.draw.line(screen, (0, 255, 0), (line_start_x, line_start_y + height/3), (line_start_x + width/3, line_start_y))
                player1_flag = False
            else:
                center = (line_start_x + width/6, line_start_y + height/6)
                pygame.draw.circle(screen, (0, 0, 255), center, outer_circle_radius)
                pygame.draw.circle(screen, black, center, inner_circle_radius)
                player1_flag = True
    pygame.display.update()
    pygame.time.Clock().tick(5)
