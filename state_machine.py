import numpy as np


class State:
    # The current state of the system. There are only two states 1 and 2.
    # todo: 0 - Corresponds to the tart screen.
    # 1 - Corresponds to the actual game.
    # 2 - Player 1 has won.
    # 3 - Player 2 has won.
    # 4 - Game is a draw.
    state = 1

    # Markers for the palyers that used in the state matrix.
    player1_marker = 1
    player2_marker = -1

    # The current turn in the tic-tac-toe game.
    turn = 1

    # The state matrix of the game. It is initialized with only 0s, corresponding to an empty tic tac toe grid.
    # A 1 corresponds to player1 using the crosses. A -1 corresponds to player 2 using the circles.
    state_matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    # Flags to indicate the result of a game.
    player1_win_flag = False
    player2_win_flag = False
    draw_flag = False

    # Getter and Setter method for the class variables.

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state

    def get_turn(self):
        return self.turn

    def set_turn(self, new_turn):
        self.turn = new_turn

    def get_state_matrix(self):
        return self.state_matrix

    def set_state_matrix(self, new_state_matrix):
        self.state_matrix = new_state_matrix

    def get_player1_win_flag(self):
        return self.player1_win_flag

    def set_player1_win_flag(self, new_player1_win_flag):
        self.player1_win_flag = new_player1_win_flag

    def get_player2_win_flag(self):
        return self.player2_win_flag

    def set_player2_win_flag(self, new_player2_win_flag):
        self.player2_win_flag = new_player2_win_flag

    def get_draw_flag(self):
        return self.draw_flag

    def set_draw_flag(self, new_draw_flag):
        self.draw_flag = new_draw_flag

    def set_state_matrix_component(self, row_index, column_index, value):
        """
        Allows one to manually set the elements of the state matrix. The position of the element is defined by the
        corresponding row and column index.
        Example: The row index 2 and the column index 1 means the last row and the middle column
        :param row_index: The index defining the row. It can take the values 0, 1 and 2.
        :param column_index: The index of the column ranging from 0 to 2.
        :param value: The new values replacing the current values at the defined position.
        :return: -
        """
        self.state_matrix[row_index, column_index] = value

    def win_check(self):
        """
        This method checks the current state matrix and looks if a player has won.
        A win is defined by three similar numbers in a row, column or diagonal.
        The checking for a winner is done by adding up the rows, columns or diagonals up.
        If the resulting value is 3 => player 1 has won.
        If the resulting values is -3 => player 2 has won.
        The win flags are then changed accordingly.
        :return: -
        """
        transposed_matrix = self.state_matrix.T

        # Check the rows for a winner
        for x in self.state_matrix:
            total = np.sum(x)
            if total == 3*self.player1_marker:
                self.player1_win_flag = True
            if total == 3*self.player2_marker:
                self.player2_win_flag = True
        # Check the columns for a winner
        for x in transposed_matrix:
            total = np.sum(x)
            if total == 3*self.player1_marker:
                self.player1_win_flag = True
            if total == 3*self.player2_marker:
                self.player2_win_flag = True
        # Checking the diagonals by looking at the trace of the original state_matrix and a transformed matrix where
        # the diagonal elements are taken from the bottom left corner to the top right corner of the state matrix.
        trafo_matrix = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        trace = np.trace(self.state_matrix)
        trafo_trace = np.trace(np.matmul(trafo_matrix, self.state_matrix))
        if trace == 3*self.player1_marker or trafo_trace == 3*self.player1_marker:
            self.player1_win_flag = True
        if trace == 3*self.player2_marker or trafo_trace == 3*self.player2_marker:
            self.player2_win_flag = True

    def init_game_state(self):
        """
        Initializes the state corresponding to the start of a game.
        :return: -
        """
        self.state = 1
        self.turn = 1
        self.state_matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.player1_win_flag = False
        self.player2_win_flag = False
        self.draw_flag = False

    def refresh_state(self, row_index, column_index):
        """
        Defines the actions that are performed, when the screen is clicked and a new graphic is add to the tic-tac-toe
        grid.
        :return:
        """
        if self.state_matrix[row_index][column_index] == 0:
            if self.turn % 2 != 0:
                self.set_state_matrix_component(row_index, column_index, self.player1_marker)
            else:
                self.set_state_matrix_component(row_index, column_index, self.player2_marker)
            self.turn += 1
            # You need at least 5 turns before you can win
            if self.turn >= 6:
                self.win_check()
                if self.player1_win_flag:
                    self.game_state = 2
                elif self.player2_win_flag:
                    self.game_state = 3
                elif self.turn >= 10:
                    self.game_state = 4
        else:
            print("You can not make this move.")
