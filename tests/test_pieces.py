import unittest
import logging

import numpy as np

from shogi.board import Board
from shogi.pieces import Pawn, King, Bishop, Rook, Lance

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


class TestPieces(unittest.TestCase):

    def setUp(self):
        # Empty board with 1 Pawn in (6,4)
        self.board = Board()

    def test_lance(self):
        ## 1. Try to jump over other pieces
        init = np.array([8, 0])
        targ = np.array([2, 0])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
             # Tries to move to the invalid position
             self.board.move(init, targ)

        ## 2. Move across the board
        # First, get Pawn out of the way
        n = 2
        while not n == 6:
            init = np.array([n, 8])
            n += 1
            targ = np.array([n, 8])
            print("From [row col]")
            print(init)
            print("To [row col]")
            print(targ)
            self.board.move(init, targ)
        # White Pawn kills Black Pawn
        init = np.array([8, 8])
        targ = np.array([6, 8])
        print("From [row col]")
        print(init)
        print("To [row col]")
        print(targ)
        self.board.move(init, targ)  # Kill white Pawn
        init = np.array([6, 8])
        targ = np.array([2, 8])
        print("From [row col]")
        print(init)
        print("To [row col]")
        print(targ)
        self.board.move(init, targ)
        # Retrieve the element at (2, 8) and check whether it is a Bishop object
        self.assertIsInstance(self.board.board.at[2, 8], Lance, msg="Lance not in position")

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
        ## 1. Try to jump
        init = np.array([7, 7])
        targ = np.array([2, 7])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
            # Tries to move to the invalid position
            self.board.move(init, targ)

        ## 2. Move across the board
        # First, get Pawn out of the way
        n = 2
        while not n == 6:
            init = np.array([n, 7])
            n += 1
            targ = np.array([n, 7])
            print("From [row col]")
            print(init)
            print("To [row col]")
            print(targ)
            self.board.move(init, targ)
        # White Pawn kills Black Pawn
        init = np.array([7, 7])
        targ = np.array([6, 7])
        self.board.move(init, targ)  # Kill Pawn
        init = np.array([6, 7])
        targ = np.array([1, 7])
        self.board.move(init, targ)  # Kill other Rook
        # Retrieve the element at (1, 7) and check whether it is a Rook object
        self.assertIsInstance(self.board.board.at[1, 7], Rook, msg="Rook not in position")

        ## 3. Move from position where there is no one
        init = np.array([7, 7])
        targ = np.array([7, 3])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
            # Tries to move to the invalid position
            self.board.move(init, targ)

        ## 4. Illegal move
        init = np.array([1, 7])
        targ = np.array([2, 6])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
            # Tries to move to the invalid position
            self.board.move(init, targ)

    def test_bishop(self):
        ## 1. Move over other pieces
        init = np.array([7, 1])
        targ = np.array([0, 8])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
            # Tries to move to the invalid position
            self.board.move(init, targ)
        init = np.array([6, 2])
        targ = np.array([5, 2])
        self.board.move(init, targ)
        init = np.array([7, 1])
        targ = np.array([0, 8])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
            # Tries to move to the invalid position
            self.board.move(init, targ)

        ## 1. Move across the board
        init = np.array([7, 1])
        targ = np.array([2, 6])
        self.board.move(init, targ)
        # Retrieve the element at (2, 6) and check whether it is a Bishop object
        self.assertIsInstance(self.board.board.at[2, 6], Bishop, msg="Bishop not in position")

        ## 3. Illegal move
        init = np.array([2, 6])
        targ = np.array([3, 5])
        self.board.move(init, targ)
        init = np.array([3, 5])
        targ = np.array([3, 4])
        with self.assertRaises(ValueError, msg="ValueError exception not launched") as cm:
            # Tries to move to the invalid position
            self.board.move(init, targ)

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
