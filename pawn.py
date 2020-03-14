from piece import Piece


class Pawn(Piece):
    """
    A Pawn can move only 1 position forward.
    """
    str_rep = "P"

    def move(self, pos_from, pos_to):
        row1, col1 = pos_from
        row2, col2 = pos_to
        if row2 == row1 - 1 and col2 == col1:
            return 0
        else:
            raise ValueError("Pawns can only move 1 step forward")
