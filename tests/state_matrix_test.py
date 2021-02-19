import unittest as ut

from .. import state_machine as sm


class GameMatrixTest(ut.TestCase):

    game_matrix = sm.State()

    def test_turn(self):
        self.assertEqual(self.game_matrix.turn, 1)
        with self.assertRaises(TypeError):
            self.game_matrix.turn = "Hello"
        with self.assertRaises(ValueError):
            self.game_matrix.turn = 12

    def test_state(self):
        


if __name__ == "__main__":
    ut.main()
