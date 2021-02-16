import pygame as pg

import inspect as ins

class Button:
     def __init__(self, _func, _screen, _text = "Dummy text" , _font = "fonts/StandingRoomOnlyNF.ttf", _font_size = 32,
                  _pos_x = 0, _pos_y = 0, *_args):
        """

        :param _func:
        :param _screen:
        :param _text:
        :param _font:
        :param _font_size:
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
        # x and y position of the button on the screen
        self._pos_x = _pos_x
        self._pos_y = _pos_y
        # Function object and arguments
        self._func = _func
        self._args = _args

     def set_func(self, new_func):
         if ins.isfunction(new_func):
            self._func = new_func
         else:
             raise ValueError("The object has to a function.")

     def get_func(self):
         return self._func

     def set_text(self, new_text):
         if isinstance(new_text, str):
             self._text = new_text
         else:
             raise ValueError("The object need to be a string.")

     def get_text(self):
         return self._text




     # Define the attributes as property objects.
     # To use getter and setter methods more easily.
     func = property(get_func, set_func)
     text = property(get_text, set_text)
     font = property(get_font, set_font)
     font_size = property(get_font_size, set_font_size)
     pos_x = property(get_pos_x, set_pos_x)
     pos_y = property(get_pos_y, set_pos_y)
     args = property(get_args, set_args)


    def draw_button(self):
        """

        :return:
        """
        self.screen.

