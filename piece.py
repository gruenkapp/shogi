from abc import ABC, abstractmethod
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
        self.moves = [np.array(l) for l in self._moves]
        self.color = color
        if self.color == self.colors['BLACK']:
            self.str_rep = self._str_rep + '^'
            self.moves = np.array([-1 * m for m in self.moves])
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
    def _moves(self):
        pass

    @property
    @abstractmethod
    def error_msg(self):
        pass

    def move(self, pos_from, pos_to):
        if np.any([np.array_equal(pos_to, pos) for pos in [pos_from + m for m in self.moves]]):
            return 0
        else:
            raise ValueError(self.error_msg)

    def __str__(self):
        return self.str_rep
