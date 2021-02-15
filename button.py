import pygame as pg

class Button:
     def __init__(self, _text = "Dummy text" , _font = "fonts/StandingRoomOnlyNF.ttf", _font_size = 32, _pos_x = 0,
                  _pos_y = 0):
        self._text = _text
        self._font = _font
        self._font_size = _font_size
        self._pos_x = _pos_x
        self._pos_y = _pos_y

    def 

    # Define the attributes as property objects.
    state = property(get_state, set_state)
    turn = property(get_turn, set_turn)
    state_matrix = property(get_state_matrix, set_state_matrix)
    player1_win_flag = property(get_player1_win_flag, set_player1_win_flag)
    player2_win_flag = property(get_player2_win_flag, set_player2_win_flag)
    draw_flag = property(get_draw_flag, set_draw_flag)
    state_changed_flag = property(get_state_changed_flag, set_state_changed_flag)
