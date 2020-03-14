import pandas as pd
from pawn import Pawn


class Board(object):
    DIM = 9

    def __init__(self):
        self.board = pd.DataFrame(index=range(self.DIM), columns=range(self.DIM))
        self.board.loc[6,4] = Pawn()

    def draw(self):
        print(self.board)
