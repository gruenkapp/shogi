# Module defining a TestCase for testing the Pawn
import unittest

import numpy as np

from board import Board
from pieces import Pawn


class TestPawn(unittest.TestCase):

    def setUp(self):
        # Empty board with 1 Pawn in (6,4)
        self.board = Board()

    def test_piece_crash(self):
        init = np.array([8, 4])
        targ = np.array([7, 4])
        self.board.move(init, targ)
        init = np.array([7, 4])
        targ = np.array([6, 4])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
            # Tries to move to the invalid position
            self.board.move(init, targ)

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

    def test_pawn_BnW(self):
        n_black = 6
        n_white = 2
        while not n_black == 0:
            # Move black pawn
            init_black = np.array([n_black, 4])
            n_black -= 1
            targ_black = np.array([n_black, 4])
            self.board.move(init_black, targ_black)

            # Move white pawn
            init_white = np.array([n_white, 3])
            n_white += 1
            targ_white = np.array([n_white, 3])
            self.board.move(init_white, targ_white)

        # Assert pawns at position
        self.assertIsInstance(self.board.board.at[0, 4], Pawn)
        self.assertIsInstance(self.board.board.at[8, 3], Pawn)

        # Assert pawns color
        self.assertEqual(str(self.board.board.at[0, 4]), Pawn._str_rep + '^')
        self.assertEqual(str(self.board.board.at[8, 3]), Pawn._str_rep + 'v')

    def tearDown(self):
        pass


# a simple way to run the test
if __name__ == '__main__':
    unittest.main()

# python -m unittest
