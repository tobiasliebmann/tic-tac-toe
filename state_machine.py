import numpy as np

import functools as ft


class State:
    # The current state of the system. There are four states.
    # 0 - Corresponds to the tart screen.
    # 1 - Corresponds to the actual game.
    # 2 - Player 1 has won.
    # 3 - Player 2 has won.
    # 4 - Game is a draw.
    menu_state = 0
    how_to_play_state = 1
    credits_state = 2
    gaming_state = 3
    player1_won_state = 4
    player2_won_state = 5
    draw_state = 6

    allowed_states = (menu_state, how_to_play_state, credits_state, gaming_state, player1_won_state,
                      player2_won_state, draw_state)

    # Markers for the players that are used in the state matrix.
    player1_marker = 1
    player2_marker = -1
    empty_field_marker = 0

    allowed_markers = (player2_marker, empty_field_marker, player1_marker)

    def __init__(self):
        # Initialize the game in the menu state.
        self._state = self.menu_state
        # Flag which is raised when a state is changed for the first time
        self._state_changed_flag = True
        # The current turn in the tic-tac-toe game.
        self._turn = 1
        # The state matrix of the game. It is initialized with only 0s, corresponding to an empty tic tac toe grid.
        # A 1 corresponds to player1 using the crosses. A -1 corresponds to player 2 using the circles.
        self._state_matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        # Flags to indicate the result of a game.
        self._player1_win_flag = False
        self._player2_win_flag = False
        self._draw_flag = False

    # --------------------------------------------------
    # Getter and Setter methods for the class attributes.
    # --------------------------------------------------
    # The setter and getter methods don't have documentation since the they only set and return the according values.
    # Further the getter methods check if the entered value has the according type if it has not a value error is
    # raised. The only exception is the method to set the state matrix since its checking procedure is rather
    # complicated.

    def get_state(self):
        return self._state

    def set_state(self, new_state):
        if new_state in self.allowed_states:
            self._state = new_state
            self._state_changed_flag = True
        else:
            raise ValueError("The new state has to be on of the following values"+str(self.allowed_states)+".")

    def get_state_changed_flag(self):
        return self._state_changed_flag

    def set_state_changed_flag(self, new_state_changed_flag):
        if isinstance(new_state_changed_flag, bool):
            self._state_changed_flag = new_state_changed_flag
        else:
            raise ValueError("state_changed_flag needs to be a boolean.")

    def get_turn(self):
        return self._turn

    def set_turn(self, new_turn):
        if isinstance(new_turn, int) and 0 <= new_turn <= 10:
            self._turn = new_turn
        else:
            raise ValueError("turn needs to be a positive integer smaller or equal than 10. ")

    def get_state_matrix(self):
        return self._state_matrix

    def set_state_matrix(self, new_state_matrix):
        """
        The setter method to set a new state matrix. The method checks if it is a 3x3-matrix and checks if the entries
        are either -1, 0 or 1. If they aren't a Value error is raised.
        :param new_state_matrix:
        :return:
        """
        # Checks if the entries of the state matrix are either -1, 0 or 1 by using the reduce function of functools.
        check_matrix_vals = ft.reduce(lambda x, y: (x in self.allowed_markers) and (y in self.allowed_markers),
                                      new_state_matrix.reshape(9), True)
        # Check the if the matrix is 3x3 and if it has the correct entries.
        if new_state_matrix.shape == (3, 3) and check_matrix_vals:
            self._state_matrix = new_state_matrix
        else:
            raise ValueError("The entry's of the state matrix can only be -1, 0 or 1.")

    def get_player1_win_flag(self):
        return self._player1_win_flag

    def set_player1_win_flag(self, new_player1_win_flag):
        if isinstance(new_player1_win_flag, bool):
            self._player1_win_flag = new_player1_win_flag
        else:
            raise ValueError("player1_win_flag has to be a boolean.")

    def get_player2_win_flag(self):
        return self._player2_win_flag

    def set_player2_win_flag(self, new_player2_win_flag):
        if isinstance(new_player2_win_flag, bool):
            self._player2_win_flag = new_player2_win_flag
        else:
            raise ValueError("player2_win_flag has to be a boolean.")

    def get_draw_flag(self):
        return self._draw_flag

    def set_draw_flag(self, new_draw_flag):
        if isinstance(new_draw_flag, bool):
            self._draw_flag = new_draw_flag
        else:
            raise ValueError("draw_flag has to be a boolean.")

    # Define the attributes as property objects.
    state = property(get_state, set_state)
    turn = property(get_turn, set_turn)
    state_matrix = property(get_state_matrix, set_state_matrix)
    player1_win_flag = property(get_player1_win_flag, set_player1_win_flag)
    player2_win_flag = property(get_player2_win_flag, set_player2_win_flag)
    draw_flag = property(get_draw_flag, set_draw_flag)
    state_changed_flag = property(get_state_changed_flag, set_state_changed_flag)

    # -----------------------------
    # Normal methods for the class.
    # -----------------------------

    def set_state_matrix_component(self, row_index, column_index, value):
        """
        Allows one to manually set the elements of the state matrix. The position of the element is defined by the
        corresponding row and column index.
        Example: The row index 2 and the column index 1 means the last row and the middle column
        :param row_index: Int, the index defining the row. It can take the values 0, 1 and 2.
        :param column_index: Int, the index of the column ranging from 0 to 2.
        :param value: Int, the new values replacing the current values at the defined position.
        :return: -
        """
        if value in self.allowed_markers:
            self.state_matrix[row_index, column_index] = value
        else:
            raise ValueError("An entry of the state matrix can only be -1, 0 or 1.")

    def win_check(self):
        """
        This method checks the current state matrix and looks if a player has won.
        A win is defined by three similar numbers in a row, column or diagonal.
        The checking for a winner is done by adding up the rows, columns or diagonals up.
        The win flags are then changed accordingly.
        :return: -
        """
        transposed_matrix = self.state_matrix.T

        # Check the rows for a winner
        for x in self.state_matrix:
            total = np.sum(x)
            if total == 3 * self.player1_marker:
                self.player1_win_flag = True
            if total == 3 * self.player2_marker:
                self.player2_win_flag = True
        # Check the columns for a winner
        for x in transposed_matrix:
            total = np.sum(x)
            if total == 3 * self.player1_marker:
                self.player1_win_flag = True
            if total == 3 * self.player2_marker:
                self.player2_win_flag = True
        # Checking the diagonals by looking at the trace of the original state_matrix and a transformed matrix where
        # the diagonal elements are taken from the bottom left corner to the top right corner of the state matrix.
        trafo_matrix = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        trace = np.trace(self.state_matrix)
        trafo_trace = np.trace(np.matmul(trafo_matrix, self.state_matrix))
        if trace == 3 * self.player1_marker or trafo_trace == 3 * self.player1_marker:
            self.player1_win_flag = True
        if trace == 3 * self.player2_marker or trafo_trace == 3 * self.player2_marker:
            self.player2_win_flag = True

    def init_gaming_state(self):
        """
        Initializes the state corresponding to the start of a game.
        :return: -
        """
        self.state = self.gaming_state
        self.turn = 1
        self.state_matrix = np.full((3, 3), self.empty_field_marker)
        self.player1_win_flag = False
        self.player2_win_flag = False
        self.draw_flag = False

    def add_new_marker(self, row_index, column_index):
        """
        Defines the actions that are performed, when the screen is clicked and a new graphic is added to the tic-tac-toe
        grid.
        :return:
        """
        if self.state_matrix[row_index][column_index] == self.empty_field_marker:
            if self.turn % 2 != 0:
                self.set_state_matrix_component(row_index, column_index, self.player1_marker)
            else:
                self.set_state_matrix_component(row_index, column_index, self.player2_marker)
            self.turn += 1
            # You need at least 5 turns before you can win
            if self.turn >= 6:
                self.win_check()
                if self.player1_win_flag:
                    self.state = self.player1_won_state
                    self.state_changed_flag = True
                elif self.player2_win_flag:
                    self.state = self.player2_won_state
                    self.state_changed_flag = True
                elif self.turn >= 10:
                    self.state = self.draw_state
                    self.state_changed_flag = True
