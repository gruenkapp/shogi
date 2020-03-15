from abc import ABC, abstractmethod
import numpy as np


class Piece(ABC):
    """
    A Piece can move on the board. Each kind of piece allows only a set of movements.
    """

    def __init__(self):
        self.moves = [np.array(l) for l in self._moves]

    @property
    @abstractmethod
    def str_rep(self):
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
        if np.any([np.array_equal(pos_to, pos) for pos in [pos_from - m for m in self.moves]]):
            return 0
        else:
            raise ValueError(self.error_msg)

    def __str__(self):
        return self.str_rep
