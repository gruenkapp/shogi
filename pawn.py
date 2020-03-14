import numpy as np

from piece import Piece


class Pawn(Piece):
    """
    A Pawn can move only 1 position forward.
    """
    str_rep = "P"

    moves = [np.array(l) for l in [[1, 0]]]

    def move(self, pos_from, pos_to):
        if np.any([np.array_equal(pos_to, pos) for pos in [pos_from - m for m in self.moves]]):
            return 0
        else:
            raise ValueError("Pawns can only move 1 step forward")
