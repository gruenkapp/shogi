from abc import ABC, abstractmethod


class Piece(ABC):
    """
    A Piece can move on the board. Each kind of piece allows only a set of movements.
    """
    @abstractmethod
    def move(self, pos_from, pos_to):
        pass
