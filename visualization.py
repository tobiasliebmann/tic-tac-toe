import pygame as pg


class Graphics:
    screen_width = 900
    screen_height = screen_width
    screen_size = (screen_height, screen_width)
    outer_circle_radius = screen_width / 7
    inner_circle_radius = screen_width / 8
    white = (255, 255, 255)
    black = (0, 0, 0)
    read = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    screen = pg.display.set_mode(screen_size)

    def init_grid(self):
        """

        :return:
        """
        self.screen.fill(self.black)
        # Draw 3x3-grid for tic-tac-toe
        pg.draw.line(self.screen, self.white, (0, self.screen_height / 3), (self.screen_width, self.screen_height / 3))
        pg.draw.line(self.screen, self.white, (0, 2 * self.screen_height / 3),
                     (self.screen_width, 2 * self.screen_height / 3))
        pg.draw.line(self.screen, self.white, (self.screen_width / 3, 0), (self.screen_width / 3, self.screen_height))
        pg.draw.line(self.screen, self.white, (2 * self.screen_width / 3, 0),
                     (2 * self.screen_width / 3, self.screen_height))
