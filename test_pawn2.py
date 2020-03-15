# Module defining a TestCase for testing the Pawn
import unittest

import numpy as np

from board import Board
from pawn import Pawn

class TestPawn(unittest.TestCase):

    def setUp(self):
        # Empty board with 1 Pawn in (6,4)
        self.board = Board()

    def test_pawn_movement(self):
        init = np.array([6, 4])
        targ = np.array([5, 4])
        self.board.move(init, targ)
        # Retrieve the element at (5,4) and check if it is a Pawn object
        self.assertIsInstance(self.board.board.at[5, 4], Pawn, msg = "Pawn not in position")

    def test_invalid_pawn_movement_large_step(self):
        init = np.array([6, 4])
        targ = np.array([4, 4])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
            # Tries to move to the invalid position
            self.board.move(init, targ)

    def test_invalid_pawn_movement_back_step(self):
        init = np.array([6, 4])
        targ = np.array([7, 4])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
            # Tries to move to the invalid position
            self.board.move(init, targ)

    def tearDown(self):
        pass


# a simple way to run the test
if __name__ == '__main__':
    unittest.main()

# python -m unittest
