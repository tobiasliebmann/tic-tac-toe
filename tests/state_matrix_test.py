import unittest as ut

# This module is imported from the parent directory
from .. import state_machine as sm

import numpy as np


class GameMatrixTest(ut.TestCase):

    # Import class for the game matrix.
    game_matrix = sm.State()

    # Tests for the turn variable of the game matrix. This variable corresponds to the current in the game.
    def test_turn_errors(self):
        with self.assertRaises(TypeError):
            self.game_matrix.turn = "Hello"
        with self.assertRaises(ValueError):
            self.game_matrix.turn = 12

    # Test getter and setter methods for the game state.
    def test_state_errors(self):
        with self.assertRaises(ValueError):
            self.game_matrix.state = 13

    def test_state_changed_flag_errors(self):
        with self.assertRaises(TypeError):
            self.game_matrix.state_changed_flag = "Hello"

    def test_state_matrix_errors(self):
        with self.assertRaises(TypeError):
            self.game_matrix.set_state_matrix = 1


if __name__ == "__main__":
    ut.main()
