import pygame as pg


class Graphics:
    screen_width = 900
    screen_height = screen_width
    screen_size = (screen_height, screen_width)
    screen = pg.display.set_mode(screen_size)

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

    def init_grid(self):
        """

        :return:
        """
        pg.display.set_caption('Tic-Tac-Toe')
        self.screen.fill(self.black)
        # Draw 3x3-grid for tic-tac-toe
        pg.draw.line(self.screen, self.white, (0, self.screen_height / 3), (self.screen_width, self.screen_height / 3))
        pg.draw.line(self.screen, self.white, (0, 2 * self.screen_height / 3),
                     (self.screen_width, 2 * self.screen_height / 3))
        pg.draw.line(self.screen, self.white, (self.screen_width / 3, 0), (self.screen_width / 3, self.screen_height))
        pg.draw.line(self.screen, self.white, (2 * self.screen_width / 3, 0),
                     (2 * self.screen_width / 3, self.screen_height))

    def draw_cross(self, pos_x, pos_y):
        """
        :param pos_x: x coordinate of the top left corner of a cross
        :param pos_y: y coordinate of the top left corner of a cross
        :return:
        """
        pg.draw.line(self.screen, self.green, (pos_x, pos_y), (pos_x + self.cross_length, pos_y + self.cross_length))
        pg.draw.line(self.screen, self.green, (pos_x, pos_y + self.cross_length), (pos_x + self.cross_length, pos_y))

    def draw_circle(self, pos_x, pos_y):
        """

        :param pos_x:
        :param pos_y:
        :return:
        """
        pg.draw.circle(self.screen, self.blue, (pos_x, pos_y), self.outer_circle_radius)
        pg.draw.circle(self.screen, self.black, (pos_x, pos_y), self.inner_circle_radius)

    def render_state_matrix(self, state_matrix):
        """

        :param state_matrix
        :return:
        """


