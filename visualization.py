import pygame as pg

import state_machine as sm

import math as m


class Graphics:
    screen_width = 900
    screen_height = screen_width
    screen_size = (screen_height, screen_width)
    screen = pg.display.set_mode(screen_size)

    game_state = sm.State()

    cross_length = screen_width / 3

    outer_circle_radius = screen_width / 7
    inner_circle_radius = screen_width / 8

    white = (255, 255, 255)
    black = (0, 0, 0)
    read = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    def __init__(self):
        pg.init()
        self.game_state.init_game_state()

    def get_screen_size(self):
        """

        :return:
        """
        return self.screen_size

    def set_screen_size(self, new_screen_width, new_screen_height):
        """

        :param new_screen_width:
        :param new_screen_height:
        :return:
        """
        self.screen_size = (new_screen_width, new_screen_height)

    def set_screen_width(self, new_screen_width):
        """

        :param new_screen_width:
        :return:
        """
        self.screen_width = new_screen_width

    def get_screen_width(self):
        """

        :return:
        """
        return self.screen_width

    def set_screen_height(self, new_screen_height):
        """

        :param new_screen_height:
        :return:
        """
        self.screen_height = new_screen_height

    def get_screen_height(self):
        """

        :return:
        """
        return self.screen_height

    def init_background(self):
        """

        :return:
        """
        pg.display.set_caption('Tic-Tac-Toe')
        self.screen.fill(self.black)
        if self.game_state.get_state() == 1:
            # Draw 3x3-grid for tic-tac-toe
            pg.draw.line(self.screen, self.white, (0, self.screen_height / 3), (self.screen_width, self.screen_height / 3))
            pg.draw.line(self.screen, self.white, (0, 2 * self.screen_height / 3),
                         (self.screen_width, 2 * self.screen_height / 3))
            pg.draw.line(self.screen, self.white, (self.screen_width / 3, 0), (self.screen_width / 3, self.screen_height))
            pg.draw.line(self.screen, self.white, (2 * self.screen_width / 3, 0),
                         (2 * self.screen_width / 3, self.screen_height))

    def draw_cross(self, pos_x, pos_y):
        """
        :param pos_x: x coordinate of the middle of the cross.
        :param pos_y: y coordinate of the middle of the cross.
        :return: -
        """
        pg.draw.line(self.screen, self.green, (pos_x - self.cross_length/2, pos_y - self.cross_length/2),
                     (pos_x + self.cross_length/2, pos_y + self.cross_length/2))
        pg.draw.line(self.screen, self.green, (pos_x + self.cross_length/2, pos_y + self.cross_length/2),
                     (pos_x - self.cross_length/2, pos_y - self.cross_length/2))

    def draw_circle(self, pos_x, pos_y):
        """

        :param pos_x: x coordinate of the center of the circle.
        :param pos_y: y coordinate of the center of the circle.
        :return:
        """
        pg.draw.circle(self.screen, self.blue, (pos_x, pos_y), self.outer_circle_radius)
        pg.draw.circle(self.screen, self.black, (pos_x, pos_y), self.inner_circle_radius)

    def convert_indices_to_drawing_position(self, row_index, column_index):
        """
        The function converts the indices of a state matrix into a position on the screen.
        :param row_index: row index of a state matrix. Possible values are 0,1 or 2
        :param column_index: column index of a state matrix. Possible values are 0,1 or 2
        :return: The according position on the screen
        """
        return (self.screen_width * row_index/3 + self.screen_width/6,
                self.screen_height * column_index/3 + self.screen_height/6)

    def on_click(self, pos_x, pos_y):
        """

        :param pos_x:
        :param pos_y:
        :return:
        """
        row_index = m.trunc(3 * pos_x/self.screen_width)
        column_index = m.trunc(3 * pos_y/self.screen_height)
        self.game_state.refresh_state(row_index, column_index)
        self.render_game()


    def render_game(self):
        """
        This method
        :return: -
        """
        state_matrix = self.game_state.get_state_matrix()
        for row_index in range(3):
            for column_index in range(3):
                (x, y) = self.convert_indices_to_drawing_position(row_index, column_index)
                if state_matrix[row_index][column_index] == self.game_state.player1_marker:
                    self.draw_cross(x, y)
                elif state_matrix[row_index][column_index] == self.game_state.player1_marker:
                    self.draw_circle(x, y)
