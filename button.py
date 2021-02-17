import pygame as pg

import inspect as ins

import functools as ft


class Button:
    # Defining RGB colors as tuples.
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    orange = (255, 128, 0)
    purple = (128, 0, 255)
    yellow = (255, 255, 0)
    pink = (255, 0, 128)
    teal = (0, 255, 255)

    def __init__(self, _func, _screen, _text="Dummy text", _font="fonts/StandingRoomOnlyNF.ttf", _font_size=32,
                 _text_color=white, _pos_x=0, _pos_y=0, *_args):
        """

        :param _func:
        :param _screen:
        :param _text:
        :param _font:
        :param _font_size:
        :param _text_color:
        :param _pos_x:
        :param _pos_y:
        :param _args:
        """
        # Pygame screen object
        self._screen = _screen
        # Text on the button
        self._text = _text
        # Text font
        self._font = _font
        # Size of the font
        self._font_size = _font_size
        # Text color
        self._text_color = _text_color
        # x and y position of the button on the screen
        self._pos_x = _pos_x
        self._pos_y = _pos_y
        # Function object and arguments
        self._func = _func
        self._args = _args
        # Graphic for the button
        self._button_graphic = None

    def set_func(self, new_func):
        """

        :param new_func:
        :return:
        """
        if ins.isfunction(new_func):
            self._func = new_func
        else:
            raise TypeError("The object has to a function.")

    def get_func(self):
        return self._func

    def set_text(self, new_text):
        """

        :param new_text:
        :return:
        """
        if isinstance(new_text, str):
            self._text = new_text
        else:
            raise TypeError("The object need to be a string.")

    def get_text(self):
        return self._text

    def set_font_size(self, new_font_size):
        """

        :param new_font_size:
        :return:
        """
        if isinstance(new_font_size, str):
            self._font_size = new_font_size
        else:
            raise TypeError("The new font size needs to be a string.")

    def get_font_size(self):
        return self._font_size

    def set_font(self, new_font):
        """

        :param new_font:
        :return:
        """
        if isinstance(new_font, str):
            if new_font[-4:] == ".tff":
                self._font = new_font
            else:
                raise ValueError("The new font needs end with .tff.")
        else:
            raise TypeError("The new font needs to be of type string.")

    def get_font(self):
        return self._font

    def set_pos_x(self, new_pos_x):
        if isinstance(new_pos_x, int):
            self._pos_x = new_pos_x
        else:
            raise TypeError("New x position must be of type int.")

    def get_pos_x(self):
        return self._pos_x

    def set_pos_y(self, new_pos_y):
        """

        :param new_pos_y:
        :return:
        """
        if isinstance(new_pos_y, int):
            self._pos_x = new_pos_y
        else:
            raise TypeError("New y position must be of type int.")

    def get_pos_y(self):
        return self._pos_y

    def set_args(self, *new_args):
        self._args = new_args

    def get_args(self):
        return self._args

    def set_text_color(self, new_text_color):
        """

        :param new_text_color:
        :return:
        """
        if isinstance(new_text_color, tuple):
            if len(new_text_color) == 3:
                if ft.reduce(lambda x, y: x and isinstance(y, int), new_text_color, True):
                    if ft.reduce(lambda x, y: x and 0 <= y <= 255, new_text_color, True):
                        self._text_color = new_text_color
                    else:
                        raise ValueError("The entries must be between 0 or 255.")
                else:
                    raise TypeError("The entries must be of type int.")
            else:
                raise ValueError("The tuple must be of length 3.")
        else:
            raise TypeError("The text color must be a tuple.")

    def get_text_color(self):
        return self._text_color

    def set_screen(self, new_screen):
        """
        todo: Add test if a pygame screen is passed as argument. At the moment I don't know how to do this.
        :param new_screen:
        :return:
        """
        self._screen = new_screen

    def get_screen(self):
        return self._screen

    # Define the attributes as property objects.
    # To use getter and setter methods more easily.
    func = property(get_func, set_func)
    text = property(get_text, set_text)
    font = property(get_font, set_font)
    font_size = property(get_font_size, set_font_size)
    pos_x = property(get_pos_x, set_pos_x)
    pos_y = property(get_pos_y, set_pos_y)
    args = property(get_args, set_args)
    text_color = property(get_text_color, set_text_color)
    screen = property(get_screen, set_screen)

    def draw_button(self):
        """
        Draws a button on the screen handed to the initializer.
        :return: -
        """
        self._button_graphic = self.screen.blit(pg.font.Font(self.font, self.font_size).render(self.text, True,
                                                                                               self.text_color),
                                                (self.pos_x, self.pos_y))

    def listener(self):
        """
        This method has to be executed in a loop to check if the button was clicked or the cursor moves over it.
        :return: The function defined by the initializer.
        """
        if self._button_graphic.collidepoint(pg.mouse.get_pos()):
            pg.mouse.set_cursor(pg.cursors.diamond)
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    return self.func(*self.args)
        else:
            pg.mouse.set_cursor(pg.cursors.arrow)
