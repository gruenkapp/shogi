from abc import ABC, abstractmethod
from itertools import zip_longest

import numpy as np


class Piece(ABC):
    """
    A Piece can move on the board. Each kind of piece allows only a set of movements.
    """
    colors = {
        'BLACK': 'black',
        'WHITE': 'white'
    }

    def __init__(self, color):
        self.color = color
        if self.color == self.colors['BLACK']:
            self.str_rep = self._str_rep + '^'
        elif self.color == self.colors['WHITE']:
            self.str_rep = self._str_rep + 'v'
        else:
            raise ValueError("Pieces can only be these colors: " + ', '.join(self.colors.values()))

    @property
    @abstractmethod
    def _str_rep(self):
        pass

    @property
    @abstractmethod
    def _error_msg(self):
        pass

    @abstractmethod
    def can_move(self, pos_from, pos_to):
        """
        Assuming that this piece is in pos_from, would it be legal for it to move to pos_to?
        :param pos_from: initial position
        :param pos_to: target position
        :return: True if movement is legal, False otherwise.
        """
        pass

    @abstractmethod
    def move(self, pos_from, pos_to):
        pass        
        
    def __str__(self):
        return self.str_rep


class OneStepPiece(Piece):
    """
    A OneStepPiece can move only one square at a time.
    The directions allowed depend on the type of OneStepPiece.
    """
    def __init__(self, color):
        super().__init__(color)
        self.moves = [np.array(l) for l in self._moves]
        if self.color == self.colors['BLACK']:
            self.moves = np.array([-1 * m for m in self.moves])

    @property
    @abstractmethod
    def _moves(self):
        """
        A collection of all the directions allowed for this type of OneStepPiece.
        :return: a list of vectors
        """
        pass

    def can_move(self, pos_from, pos_to):
        return np.any([np.array_equal(pos_to, pos) for pos in [pos_from + m for m in self.moves]])

    def move(self, pos_from, pos_to):
        if self.can_move(pos_from, pos_to):
            return [pos_to]
        else:
            raise ValueError(self._error_msg)


class RangePiece(Piece):
    """
    A RangePiece can move a range of squares at one time.
    The directions allowed depend on the type of RangePiece.
    """
    def __init__(self, color):
        super().__init__(color)

    @abstractmethod
    def can_move(self, pos_from, pos_to):
        pass

    def move(self, pos_from, pos_to):
        if not self.can_move(pos_from, pos_to):
            raise ValueError(self._error_msg)
        diff = pos_to - pos_from
        n_rows, n_cols = diff
        if abs(n_rows) + abs(n_cols) == 0:
            raise ValueError("You can't leave the piece on its position")
        range_rows = np.array(range(1, abs(n_rows)+1))
        range_cols = np.array(range(1, abs(n_cols)+1))
        if n_rows < 0:
            range_rows *= -1
        if n_cols < 0:
            range_cols *= -1

        diff_range = list(zip_longest(range_rows, range_cols, fillvalue=0))
        sq_range = pos_from + diff_range
        if not np.array_equal(sq_range[-1], pos_to):
            raise ValueError(self._error_msg)

        return sq_range
