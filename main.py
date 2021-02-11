import sys

import pygame

import math

import numpy as np


def init_game_state():
    """

    :return:
    """
    screen.fill(black)
    # Draw 3x3-grid for tic-tac-toe
    pygame.draw.line(screen, (255, 255, 255), (0, height / 3), (width, height / 3))
    pygame.draw.line(screen, (255, 255, 255), (0, 2 * height / 3), (width, 2 * height / 3))
    pygame.draw.line(screen, (255, 255, 255), (width / 3, 0), (width / 3, height))
    pygame.draw.line(screen, (255, 255, 255), (2 * width / 3, 0), (2 * width / 3, height))

def game_over_screen(message):
    """

    :return:
    """
    screen.fill(black)
    # apply it to text on a label
    label = my_font.render(message, True, (255, 0, 0))
    # put the label object on the screen at point x=100, y=100
    screen.blit(label, (width/2, height/2))


def quit_game():
    """

    :return:
    """
    pygame.quit()
    sys.exit()


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
    return 0 == matrix[math.trunc(3*click_pos[1]/height)][math.trunc(3*click_pos[0]/width)]


def win_check(matrix):
    """

    :param matrix:
    :return:
    """
    trafo_matrix = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    transposed_matrix = matrix.T
    for x in matrix:
        total = np.sum(x)
        if total == 3:
            return 1
        if total == -3:
            return -1
    for x in transposed_matrix:
        total = np.sum(x)
        if total == 3:
            return 1
        if total == -3:
            return -1
    if np.trace(matrix) == 3 or np.trace(np.matmul(trafo_matrix, matrix)) == 3:
        return 1
    if np.trace(matrix) == -3 or np.trace(np.matmul(trafo_matrix, matrix)) == -3:
        return -1


pygame.init()

# This matrix keeps track of the state of system i.e. which player has occupied which field
# A value of 1 stands for the player 1, -1 equates to player 2 and 0 means the field is not occupied.
# The matrix is initialized with only zeros.
state_matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

game_state = 1

player_turn = 1

player1_win_flag = False
player2_win_flag = False
draw_flag = False

size = width, height = 1000, 1000
black = 0, 0, 0

outer_circle_radius = width/7
inner_circle_radius = width/8

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic-Tac-Toe')

# pick a font you have and set its size
my_font = pygame.font.SysFont("Comic Sans MS", 30)
retry_button = my_font.render("Click here for new game.", True, (0, 255, 255))
retry_button_rect = retry_button.get_rect()

init_game_state()

while 1:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        if game_state == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                line_start_x = position_test(pos[0], width)
                line_start_y = position_test(pos[1], height)
                column_index = math.trunc(3*pos[0]/width)
                row_index = math.trunc(3*pos[1]/height)
                if player_turn % 2 != 0 and click_test(pos, state_matrix):
                    print("Im here.")
                    pygame.draw.line(screen, (0, 255, 0), (line_start_x, line_start_y), (line_start_x + height/3, line_start_y + height/3))
                    pygame.draw.line(screen, (0, 255, 0), (line_start_x, line_start_y + height/3), (line_start_x + width/3, line_start_y))
                    print("now Im here.")
                    state_matrix[row_index][column_index] = 1
                    if win_check(state_matrix) == 1:
                        game_state = 2
                        player1_win_flag = True
                        pygame.time.delay(1000)
                    player_turn = player_turn + 1
                    print(state_matrix)
                    print(player_turn)
                elif player_turn % 2 == 0 and click_test(pos, state_matrix):
                    center = (line_start_x + width/6, line_start_y + height/6)
                    pygame.draw.circle(screen, (0, 0, 255), center, outer_circle_radius)
                    pygame.draw.circle(screen, black, center, inner_circle_radius)
                    state_matrix[row_index][column_index] = -1
                    if win_check(state_matrix) == -1:
                        game_state = 2
                        player2_win_flag = True
                        pygame.time.delay(1000)
                    player_turn = player_turn + 1
                    print(state_matrix)
                    print(player_turn)
                elif player_turn >= 10:
                    game_state = 2
                    draw_flag = True
                    pygame.time.delay(1000)
                else:
                    print(state_matrix)
                    print("You cant place your marker here.")
        if game_state == 2:
            if player1_win_flag:
                game_over_screen("Cross wins.")
            elif player2_win_flag:
                game_over_screen("Circle wins.")
            elif draw_flag:
                game_over_screen("Draw.")
            retry_button_graphic = screen.blit(retry_button, (100, 100))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if retry_button_graphic.collidepoint(pos):
                    print("Retry button was clicked.")
                    game_state = 1
                    player1_win_flag = False
                    player2_win_flag = False
                    draw_flag = False
                    player_turn = 1
                    state_matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
                    init_game_state()
    pygame.display.flip()
    pygame.time.delay(5)
