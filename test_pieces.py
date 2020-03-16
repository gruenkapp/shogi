import unittest
import logging

import numpy as np

from board import Board
from pieces import Pawn, King, Bishop, Rook, Lance

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


class TestPieces(unittest.TestCase):

    def setUp(self):
        # Empty board with 1 Pawn in (6,4)
        self.board = Board()

    def test_lance(self):
        ## 1. Move across the board
        init = np.array([8, 0])
        targ = np.array([2, 0])
        self.board.move(init, targ)
        # Retrieve the element at (2, 0) and check whether it is a Bishop object
        self.assertIsInstance(self.board.board.at[2, 0], Lance, msg="Lance not in position")

        ## 2. Illegal move
        init = np.array([2, 0])
        targ = np.array([2, 3])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
            # Tries to move to the invalid position
            self.board.move(init, targ)

    def test_not_move(self):
        init = np.array([7, 7])  # Rook
        targ = np.array([7, 7])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
            # Tries to move to the invalid position
            self.board.move(init, targ)

    def test_rook(self):
        ## 1. Move across the board
        init = np.array([7, 7])
        targ = np.array([2, 7])
        self.board.move(init, targ)
        # Retrieve the element at (7, 2) and check whether it is a Bishop object
        self.assertIsInstance(self.board.board.at[7, 2], Rook, msg="Rook not in position")

        ## 2. Illegal move
        init = np.array([2, 7])
        targ = np.array([2, 6])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
            # Tries to move to the invalid position
            self.board.move(init, targ)

    def test_bishop(self):
        ## 1. Move across the board
        init = np.array([7, 1])
        targ = np.array([0, 8])
        self.board.move(init, targ)
        # Retrieve the element at (0, 8) and check whether it is a Bishop object
        self.assertIsInstance(self.board.board.at[0, 8], Bishop, msg="Bishop not in position")

        ## 2. Move beyond the board's edge
        init = np.array([0, 8])
        targ = np.array([0, 9])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
            # Tries to move to the invalid position
            self.board.move(init, targ)

        ## 3. Illegal move
        init = np.array([0, 8])
        targ = np.array([0, 7])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
            # Tries to move to the invalid position
            self.board.move(init, targ)

        ## 4. Kill Pawn
        # Bishop moves
        init = np.array([0, 8])
        targ = np.array([4, 4])
        self.board.move(init, targ)
        # Pawn moves
        init = np.array([2, 3])
        targ = np.array([3, 3])
        self.board.move(init, targ)
        # Bishop kills
        init = np.array([4, 4])
        targ = np.array([3, 3])
        self.board.move(init, targ)
        # Retrieve the element at (0, 8) and check whether it is a Bishop object
        self.assertIsInstance(self.board.board.at[3, 3], Bishop, msg="Bishop doesn't seem to have killed Pawn")
        # TODO: assert that Pawn is in black's captured list

    def test_capture_piece(self):
        n_white = 2
        while not n_white == 7:
            # Move white pawn
            init_white = np.array([n_white, 3])
            n_white += 1
            targ_white = np.array([n_white, 3])
            self.board.move(init_white, targ_white)
        # Move King to kill Pawn
        init = np.array([8, 4])
        targ = np.array([7, 3])
        self.board.move(init, targ)
        self.assertIsInstance(self.board.board.at[7, 3], King, msg="King doesn't seem to have killed Pawn")
    	# TODO: assert that Pawn is in black's captured list
    #
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
        # Retrieve the element at (5,4) and check whether it is a Pawn object
        self.assertIsInstance(self.board.board.at[5, 4], Pawn, msg="Pawn not in position")

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
