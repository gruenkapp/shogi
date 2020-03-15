# Module defining a TestCase for testing the Board
import unittest

import numpy as np

from board import Board

from pieces import Pawn

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_board_draw(self):
        self.board.draw()
        self.assertTrue(True) # If everything executed, the test is passed

    def test_board_structure(self):
        # Is there a pawn at the given position?
        self.assertIsInstance(self.board.board.at[6, 4], Pawn, msg="Expected an instance of " + Pawn.__name__)

    def test_movement_limits_with_pawn(self):
        with self.assertRaises(ValueError, msg="Out of the Board exception not launched") as cm:
            n = 6
            while True:  # not n == 0:
                init = np.array([n, 4])
                n -= 1
                targ = np.array([n, 4])
                self.board.move(init, targ)
        exception = cm.exception
        self.assertEqual(str(exception), "Out of the Board: the board's dimensions are "
                         + str(self.board.DIM) + "x" + str(self.board.DIM) +
                         ". You cannot move a piece beyond the board's edge.")

    def tearDown(self):
        pass

# a simple way to run the test
if __name__ == '__main__':
    unittest.main()

# python -m unittest

