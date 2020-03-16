import time

import numpy as np

from shogi import Board

game = [
    [[6, 8], [5, 8]],
    [[2, 0], [3, 0]],
    [[6, 0], [5, 0]],
    [[3, 0], [4, 0]],
    [[5, 0], [4, 0]],
    [[0, 0], [4, 0]],
    [[8, 0], [4, 0]],
    [[1, 1], [1, 0]],
    [[6, 2], [5, 2]],
    [[1, 0], [4, 0]],
    [[7, 1], [2, 6]],
    [[0, 4], [1, 4]],
    [[2, 6], [1, 5]],
    [[1, 4], [1, 5]],
    [[7, 7], [7, 3]],
    [[4, 0], [8, 0]]
]

board = Board()

turns = ['black', 'white']
t = 0
for move in game:
    print()
    print()
    print()
    print()
    print("Turn " + str(t) + ": " + turns[t % 2])
    t += 1
    init = np.array(move[0])
    targ = np.array(move[1])
    print("From [row col]")
    print(init)
    print("To [row col]")
    print(targ)
    time.sleep(1)
    board.move(init, targ)
    time.sleep(1)

print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("End of the game")
