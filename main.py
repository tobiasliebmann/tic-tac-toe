import sys

import pygame

import math


def position_test(input_pos, test_dimension):
    """

    :param input_pos:
    :param test_dimension:
    :return:
    """
    if 0 <= input_pos <= test_dimension/3:
        return 0
    elif test_dimension/3 < input_pos <= 2*test_dimension/3:
        return test_dimension/3
    else:
        return 2*test_dimension/3


def click_test(click_pos, matrix):
    """

    :param click_pos:
    :param matrix:
    :return:
    """
    return 0 == matrix[math.trunc(3*click_pos[0]/width)][math.trunc(3*click_pos[1]/height)]


pygame.init()

# This matrix keeps track of the state of system i.e. which player has occupied which field
# A value of 1 stands for the player 1, -1 equates to player 2 and 0 means the field is not occupied.
# The matrix is initialized with only zeros.
state_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

player1_flag = True

size = width, height = 800, 800
black = 0, 0, 0

outer_circle_radius = width/7
inner_circle_radius = width/8

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic-Tac-Toe')

screen.fill(black)

while 1:
    pygame.draw.line(screen, (255, 255, 255), (0, height / 3), (width, height / 3))
    pygame.draw.line(screen, (255, 255, 255), (0, 2 * height / 3), (width, 2 * height / 3))
    pygame.draw.line(screen, (255, 255, 255), (width / 3, 0), (width / 3, height))
    pygame.draw.line(screen, (255, 255, 255), (2 * width / 3, 0), (2 * width / 3, height))

    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            line_start_x = position_test(pos[0], width)
            line_start_y = position_test(pos[1], height)
            row_index = math.trunc(3*pos[0]/width)
            column_index = math.trunc(3*pos[1]/height)

            if player1_flag and click_test(pos, state_matrix):
                pygame.draw.line(screen, (0, 255, 0), (line_start_x, line_start_y),
                                 (line_start_x + height/3, line_start_y + height/3))
                pygame.draw.line(screen, (0, 255, 0), (line_start_x, line_start_y + height/3),
                                 (line_start_x + width/3, line_start_y))
                player1_flag = False
                state_matrix[row_index][column_index] = 1
                print(state_matrix)
            elif not player1_flag and click_test(pos, state_matrix):
                center = (line_start_x + width/6, line_start_y + height/6)
                pygame.draw.circle(screen, (0, 0, 255), center, outer_circle_radius)
                pygame.draw.circle(screen, black, center, inner_circle_radius)
                player1_flag = True
                state_matrix[row_index][column_index] = -1
                print(state_matrix)
            else:
                print("This move is not possible")
                print(state_matrix)
    pygame.display.update()
    pygame.time.Clock().tick(5)
