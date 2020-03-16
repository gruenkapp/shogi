from itertools import product

from piece import Piece, OneStepPiece, RangePiece


class Pawn(OneStepPiece):
    """
    A Pawn can move only 1 position forward.
    """
    _moves = [[1, 0]]
    _str_rep = "P"
    _error_msg = "Illegal Move: Pawns can only move 1 step forward"

    def __init__(self, color):
        super().__init__(color)


class King(OneStepPiece):
    """
    A King can move only 1 position in any direction, including diagonally.
    """
    # _moves = filter(lambda x: not np.array_equal(x, (0, 0)), list(product([0, 1, -1], repeat=2)))
    # [[1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 0], [-1, 1], [-1, -1]]
    _str_rep = "K"
    _error_msg = "Illegal Move: a King can move only 1 position at a time"

    def __init__(self, color):
        super().__init__(color)

    @property
    def _moves(self):
        # [[1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 0], [-1, 1], [-1, -1]]
        aux = list(product([0, 1, -1], repeat=2))
        aux.remove((0, 0))
        return aux


class Bishop(RangePiece):
    """
    A Bishop can move diagonally any number of squares
    """
    _str_rep = "B"
    _error_msg = "Illegal Move: a Bishop can only move diagonally"

    def __init__(self, color):
        super().__init__(color)

    def can_move(self, pos_from, pos_to):
        diff = pos_to - pos_from
        r, c = diff
        return r == c or r == -1 * c


class Rook(RangePiece):
    """
    A Rook can move any number of squares vertically and horizontally
    """
    _str_rep = "R"
    _error_msg = "Illegal Move: a Rook can move forwards, backwards and to the sides any number of squares"

    def __init__(self, color):
        super().__init__(color)

    def can_move(self, pos_from, pos_to):
        diff = pos_to - pos_from
        r, c = diff
        return r == 0 or c == 0


class Lance(RangePiece):
    """
    A Lance can move any number of squares forward
    """
    _str_rep = "R"
    _error_msg = "Illegal Move: A Lance can move any number of squares forward"

    def __init__(self, color):
        super().__init__(color)

    def can_move(self, pos_from, pos_to):
        diff = pos_to - pos_from
        r, c = diff
        return c == 0 and \
               ((self.color == Piece.colors['WHITE'] and r > 0) or (self.color == Piece.colors['BLACK'] and r < 0))
