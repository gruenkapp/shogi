# Module defining a TestCase for testing the Pawn movement
import unittest

import numpy as np

from board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_movement_limits_with_pawn(self):
        with self.assertRaises(ValueError) as cm:
            n = 6
            while True:  # not n == 0:
                init = np.array([n, 4])
                n -= 1
                targ = np.array([n, 4])
                self.board.move(init, targ)
        exception = cm.exception
        self.assertEqual(str(exception),
                    "Out of Board: the board's dimensions are 9x9. You cannot move a piece beyond the board's edge.")

    def tearDown(self):
        pass


# a simple way to run the test
if __name__ == '__main__':
    unittest.main()

# python -m unittest
