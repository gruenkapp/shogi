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
