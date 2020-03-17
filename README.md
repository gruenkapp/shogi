# Shogi
A program that simulates two people playing Shogi.

It is quite basic as of now:
* You have the complete board with all the pieces. 
* Each piece allows only legal movements. Check Shogi rules here: https://en.wikipedia.org/wiki/Shogi. 
* Also, it is not allowed for a piece to go beyond the board's edges or to jump over other pieces, unless it is a Knight.
* You also have captured pieces at each side of the board.

```
Turn 9: white
From [row col]
[1 0]
To [row col]
[4 0]
Rv captured piece L^ color black on position [4 0]
================ White (v) =====================
Captured:
P^, L^
     0    1    2    3    4    5    6    7    8
0        Nv   Sv   Gv   Kv   Gv   Sv   Nv   Lv
1                                      Bv     
2        Pv   Pv   Pv   Pv   Pv   Pv   Pv   Pv
3                                             
4   Rv                                        
5             P^                            P^
6        P^        P^   P^   P^   P^   P^     
7        B^                            R^     
8        N^   S^   G^   K^   G^   S^   N^   L^
Captured:
Pv, Lv
================ Black (^) =====================
```

The white pieces are on the upper side and the black ones are on the lower side of the board.
The blacks always start the game. 

The moves are defined by a starting position and an end position. Both positions must be squares of the board. They must be [numpy](https://numpy.org/) vectors of (x, y). The initial position must contain a piece and the end position must be the result of a valid move for that kind of piece.

See the example in this repo's [shogi.py](shogi.py) (also see section [Usage](#usage) below).

# Installing
Clone the repo and then go to its root directory:

```sh
git clone https://github.com/gruenkapp/shogi.git
cd shogi
```

Install shogi
```sh
pip install .
```

Test
```sh
python shogi.py
```

Enjoy!

Note: you can use [shogi.py](shogi.py) as an example and develop your own games.
You can even create a program that reads the moves from command line and avoids crash when illegal moves are made, giving the players a second chance.

# Usage
As stated above, you can use the [shogi.py](shogi.py) file as a how-to.

It is also explained here for convenience:
1. Once you have installed the package, import the Board class:
```py
from shogi import Board
```
And create a new board:
```py
board = Board()
```

2. Define a move:
You'll need to import numpy:

```py
import numpy as np

init = np.array([6, 4])
targ = np.array([5, 4])
```

3. Make the move:
```py
board.move(init, targ)
```
Note: you should start by a black piece. Black pieces are at the bottom of the board (ranks 6 to 8) and have symbol `^` next to them.

# Contributions
These functionalities are not yet developed:
* Promotion of pieces (crowning) (see https://en.wikipedia.org/wiki/Shogi#Promotion)
* Drops (see https://en.wikipedia.org/wiki/Shogi#Drops)
* Check and checkmate (see https://en.wikipedia.org/wiki/Shogi#Check)

Also, the interface could be improved: it could become a graphic interface, and/or allow for user's input. However, this would be more a development on top of this package.

Also, see the issues that don't have any related pull request in this repo.

Have fun! :)
