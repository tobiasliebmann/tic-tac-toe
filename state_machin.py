import numpy as np

class State:

    state = 1
    turn = 1
    state_matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    player1_win_flag = False
    player2_win_flag = False
    draw_flag = False

    def get_state(self):
        """

        :return:
        """
        return self.state

    def set_state(self, new_state):
        """

        :param new_state
        :return:
        """
        self.state = new_state

    def get_turn(self):
        """

        :return:
        """
        return self.turn

    def set_turn(self, new_turn):
        """

        :param new_turn:
        :return:
        """
        self.turn = new_turn

    def get_state_matrix(self):
        """

        :return:
        """
        return state_matrix

    def set_state_matrix(self, new_state_matrix):
        """

        :param new_state_matrix:
        :return:
        """
        self.state_matrix = new_state_matrix

    def get_player1_win_falg(self):
        """

        :return:
        """
        return self.player1_win_flag

    def set_player1_win_falg(self, new_player1_win_flag):
        """

        :param new_player1_win_flag:
        :return:
        """
        self.player1_win_flag = new_player1_win_flag

    def get_player2_win_falg(self):
        """

        :return:
        """
        return self.player2_win_flag

    def set_player2_win_falg(self, new_player1_win_flag):
        """

        :param new_player1_win_flag:
        :return:
        """
        self.player2_win_flag = new_player2_win_flag

    def get_draw_flag(self):
        """

        :return:
        """
        return self.draw_flag

    def set_draw_flag(self, new_draw_flag):
        """

        :param new_draw_flag:
        :return:
        """
        self.draw_flag = new_draw_flag

    def set_state_matrix_component(self, row_index, column_index, value):
        """

        :param row_index:
        :param column_index:
        :param value:
        :return:
        """
        self.state_matrix[row_index, column_index] = value
