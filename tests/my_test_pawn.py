import numpy as np

from shogi.board import Board

board = Board()
board.draw()
n = 6
while not n == 0:
    init = np.array([n, 4])
    n -= 1
    targ = np.array([n, 4])

    print("From [row col]")
    print(init)
    print("To [row col]")
    print(targ)

    board.move(init, targ)
