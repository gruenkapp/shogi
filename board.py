import pandas as pd
import numpy as np

from pawn import Pawn


class Board(object):
    """
    The shogi board.
    Its positions are numbered from 0 to 8, columns as well as rows.
    The board contains a list of pieces and knows the position of each piece.
    """
    DIM = 9

    def __init__(self):
        self.board = pd.DataFrame("", index=range(self.DIM), columns=range(self.DIM))
        self.board.at[6, 4] = Pawn()

    def move(self, pos_from, pos_to):
        """
        Move one piece from its position to a new position.
        The piece is identified by its position. This means that it is not provided for you to say "move Pawn to A4".
        Instead, you say "Move the piece that's in (0, 2) to (0,3)".
        It will raise the following exceptions:
        - Out of the board's boundaries: You tried to move a piece out of the board's boundaries.
        - No piece to move: The initial position that you passed contains no piece.
        - Illegal move: The piece you are trying to move does not allow the move you are specifying.
        :param pos_from: initial position. This position must contain a piece.
        :param pos_to: target position. This position must be within the board and it must be the result of a movement
        that is legal for the piece that you are moving.
        :return:
        """

        row1, col1 = pos_from
        row2, col2 = pos_to

        if np.any(pos_to > self.DIM) or np.any(pos_to < 0):
            raise ValueError("Out of the Board: the board's dimensions are " + str(self.DIM) + "x" + str(self.DIM) +
                             ". You cannot move a piece beyond the board's edge.")
        piece = self.board.at[row1, col1]
        if piece == "":
            raise ValueError("No Piece at start position: there is no piece at " + str(pos_from))
        if piece.move(pos_from, pos_to) == 0:
            self.board.at[row1, col1] = ""
            self.board.at[row2, col2] = piece
        self.draw()

    def draw(self):
        print(self.board)
