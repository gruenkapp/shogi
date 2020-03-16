import time

import numpy as np

from shogi import Board

game = [
    [[6, 2], [5, 2]],
    [[2, 5], [3, 5]],
    [[6, 5], [5, 5]],
    [[2, 7], [3, 7]],
    [[7, 1], [3, 5]]
]

board = Board()

turns = ['black', 'white']
t = 0
for move in game:
    print("Turn " + str(t) + ": " + turns[t % 2])
    t += 1
    init = np.array(move[0])
    targ = np.array(move[1])
    print("From [row col]")
    print(init)
    print("To [row col]")
    print(targ)
    time.sleep(3)
    board.move(init, targ)
    time.sleep(2)

print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("End of the game")
