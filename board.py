import logging

import pandas as pd
import numpy as np

from piece import Piece
from pieces import Pawn, King, Bishop, Rook, Lance


class Board(object):
    """
    The shogi board.
    Its positions are numbered from 0 to 8, columns as well as rows.
    The board contains a list of pieces and knows the position of each piece.
    """
    DIM = 9
    EMPTY_CELL = "   "

    def __init__(self):
        self.captured = {
            Piece.colors['BLACK']: [],
            Piece.colors['WHITE']: []
        }
        self.board = pd.DataFrame(self.EMPTY_CELL, index=range(self.DIM), columns=range(self.DIM))
        self.board.at[6, 4] = Pawn(color=Piece.colors['BLACK'])
        self.board.at[8, 4] = King(color=Piece.colors['BLACK'])
        self.board.at[7, 1] = Bishop(color=Piece.colors['BLACK'])
        self.board.at[7, 7] = Rook(color=Piece.colors['BLACK'])
        self.board.at[8, 0] = Lance(color=Piece.colors['BLACK'])
        self.board.at[2, 3] = Pawn(color=Piece.colors['WHITE'])

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
        :return: nothing. If everything was ok, it will draw its new status. Otherwise it will throw an error.
        """

        row1, col1 = pos_from
        row2, col2 = pos_to

        if np.any(pos_to > self.DIM - 1) or np.any(pos_to < 0):
            raise ValueError("Out of the Board: the board's dimensions are " + str(self.DIM) + "x" + str(self.DIM) +
                             ". You cannot move a piece beyond the board's edge.")

        piece = self.board.at[row1, col1]
        if piece == self.EMPTY_CELL:
            raise ValueError("No Piece at start position: there is no piece at " + str(pos_from))

        piece_at_target = self.board.at[row2, col2]
        if piece_at_target != self.EMPTY_CELL:
            if piece_at_target.color == piece.color:
                raise ValueError("Target position contains a friend piece.")
            else:
                logging.debug(str(piece) + " captured piece " + str(piece_at_target) + " color " + piece_at_target.color
                              + " on position " + str(pos_to))
                self.captured[piece_at_target.color] += [piece_at_target]

        mv_range = piece.move(pos_from, pos_to)
        # TODO: mv_range to be used to make sure no piece is on the way
        self.board.at[row1, col1] = self.EMPTY_CELL
        self.board.at[row2, col2] = piece
        self.draw()

    def draw(self):
        print("Captured:")
        print(', '.join([str(p) for p in self.captured[Piece.colors['WHITE']]]))
        print(self.board)
        print("Captured:")
        print(', '.join([str(p) for p in self.captured[Piece.colors['BLACK']]]))
