from itertools import product 

import numpy as np

from piece import Piece


class Pawn(Piece):
    """
    A Pawn can move only 1 position forward.
    """
    _moves = [[1, 0]]
    _str_rep = "P"
    error_msg = "Pawns can only move 1 step forward"

    def __init__(self, color):
        super().__init__(color)


class King(Piece):
    """
    A King can move only 1 position in any direction, including diagonally.
    """
    # _moves = filter(lambda x: not np.array_equal(x, (0, 0)), list(product([0, 1, -1], repeat=2)))
    # [[1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 0], [-1, 1], [-1, -1]]
    _str_rep = "K"
    error_msg = "A King can move only 1 position at a time"

    def __init__(self, color):
        super().__init__(color)

    @property
    def _moves(self):
        # [[1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 0], [-1, 1], [-1, -1]]
        aux = list(product([0, 1, -1], repeat=2))
        aux.remove((0, 0))
        return aux


class Bishop(Piece):
    """
    A Bishop can move diagonally any number of squares
    """
    _moves = []
    _str_rep = "B"
    error_msg = "A Bishop can only move diagonally"

    def __init__(self, color):
        super().__init__(color)

    def move(self, pos_from, pos_to):
        diff = pos_to - pos_from
        n_rows, n_cols = diff
        if n_rows == 0:
            raise ValueError("You can't leave the piece on its position")
        range_rows = np.array(range(1, abs(n_rows)+1))
        range_cols = range_rows.copy()
        if n_rows < 0:
            range_rows *= -1
        if n_cols < 0:
            range_cols *= -1

        sq_range = list(zip(range_rows, range_cols))
        if not np.array_equal(pos_from + sq_range[-1], pos_to):
            raise ValueError(self.error_msg)

        return sq_range


class Rook(Piece):
    """
    A Rook can move any number of squares vertically and horizontally
    """
    _moves = []
    _str_rep = "B"
    error_msg = "A Bishop can only move diagonally"

    def __init__(self, color):
        super().__init__(color)

    def move(self, pos_from, pos_to):
        diff = pos_to - pos_from
        n_rows, n_cols = diff
        if n_rows == 0:
            raise ValueError("You can't leave the piece on its position")
        r = n_rows * -1 if n_rows < 0 else n_rows
        range_rows = np.array(range(1, r+1))
        range_cols = range_rows.copy()
        if n_rows < 0:
            range_rows *= -1
        if n_cols < 0:
            range_cols *= -1

        sq_range = list(zip(range_rows, range_cols))
        if not np.array_equal(pos_from + sq_range[-1], pos_to):
            raise ValueError(self.error_msg)

        return sq_range
