import pygame as pg

import state_machine as sm

import math as m


class Graphics:
    screen_width = 900
    screen_height = screen_width
    screen_size = (screen_height, screen_width)
    screen = pg.display.set_mode(screen_size)

    game_font = None

    replay_button = None

    game_state = sm.State()

    cross_length = screen_width / 3

    outer_circle_radius = screen_width / 7
    inner_circle_radius = screen_width / 8

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    def __init__(self):
        pg.init()
        self.game_font = pg.font.SysFont("Comic Sans MS", 30)
        self.game_state.init_gaming_state()

    def init_visuals(self):
        """

        :return:
        """
        self.draw_background()
        self.draw_grid()

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

    def draw_background(self):
        """

        :return:
        """
        pg.display.set_caption('Tic-Tac-Toe')
        self.screen.fill(self.black)

    def draw_grid(self):
        """

        :return:
        """
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
        pg.draw.line(self.screen, self.green, (pos_x + self.cross_length/2, pos_y - self.cross_length/2),
                     (pos_x - self.cross_length/2, pos_y + self.cross_length/2))

    def draw_circle(self, pos_x, pos_y):
        """

        :param pos_x: x coordinate of the center of the circle.
        :param pos_y: y coordinate of the center of the circle.
        :return:
        """
        pg.draw.circle(self.screen, self.blue, (pos_x, pos_y), self.outer_circle_radius)
        pg.draw.circle(self.screen, self.black, (pos_x, pos_y), self.inner_circle_radius)

    def draw_replay_button(self, pos_x, pos_y):
        """

        :param pos_x:
        :param pos_y:
        :return: -
        """
        self.replay_button = self.screen.blit(self.game_font.render("Click here for new game.", True, self.red),
                                              (pos_x, pos_y))

    def convert_indices_to_drawing_position(self, row_index, column_index):
        """
        The function converts the indices of a state matrix into a position on the screen.
        :param row_index: row index of a state matrix. Possible values are 0,1 or 2
        :param column_index: column index of a state matrix. Possible values are 0,1 or 2
        :return: The according position on the screen
        """
        return (self.screen_width * column_index/3 + self.screen_width/6,
                self.screen_height * row_index/3 + self.screen_height/6)

    def on_click(self, pos_x, pos_y):
        """

        :param pos_x:
        :param pos_y:
        :return:
        """
        row_index = m.trunc(3 * pos_y/self.screen_width)
        column_index = m.trunc(3 * pos_x/self.screen_height)
        if self.game_state.get_state() == self.game_state.gaming_state:
            # Refresh the state and check wether a player has won or the game is s draw
            self.game_state.add_new_marker(row_index, column_index)
            self.visualize_matrix()
        elif self.game_state.get_state() != self.game_state.gaming_state:
            if self.replay_button.collidepoint((pos_x, pos_y)):
                self.game_state.set_state(self.game_state.gaming_state)
                self.game_state.init_gaming_state()
                self.game_state.toggle_state_changed_flag()

    def visualize_matrix(self):
        """
        This method
        :return: -
        """
        state_matrix = self.game_state.get_state_matrix()
        # if self.game_state.get_state() == self.game_state.gaming_state:
        print(state_matrix)
        for row_index in range(3):
            for column_index in range(3):
                (x, y) = self.convert_indices_to_drawing_position(row_index, column_index)
                if state_matrix[row_index, column_index] == self.game_state.player1_marker:
                    self.draw_cross(x, y)
                    # print("Drew a cross.")
                elif state_matrix[row_index, column_index] == self.game_state.player2_marker:
                    self.draw_circle(x, y)

    def check_visuals(self):
        """
        This method changes the background according to the game state
        :return: -
        """
        if self.game_state.get_state_changed_flag():
            if self.game_state.get_state() == self.game_state.gaming_state:
                self.draw_background()
                self.draw_grid()
            elif self.game_state.get_state() == self.game_state.player1_won_state:
                self.draw_background()
                self.draw_replay_button(25, 25)
                # print("Player 1 won.")
            elif self.game_state.get_state() == self.game_state.player2_won_state:
                self.draw_background()
                self.draw_replay_button(25, 25)
                # print("Player 2 won.")
            elif self.game_state.get_state() == self.game_state.draw_state:
                self.draw_background()
                self.draw_replay_button(25, 25)
                # print("Draw.")
            self.game_state.toggle_state_changed_flag()
