import numpy as np

from board import Board

board = Board()
board.draw()
n_black = 6
n_white = 2
while not n_black == 0:
    # Move black pawn
    init_black = np.array([n_black, 4])
    n_black -= 1
    targ_black = np.array([n_black, 4])

    print("From [row col]")
    print(init_black)
    print("To [row col]")
    print(targ_black)

    board.move(init_black, targ_black)

    # Move white pawn
    init_white = np.array([n_white, 3])
    n_white += 1
    targ_white = np.array([n_white, 3])

    print("From [row col]")
    print(init_white)
    print("To [row col]")
    print(targ_white)

    board.move(init_white, targ_white)
