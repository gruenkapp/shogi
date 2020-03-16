# shogi
A program that simulates two people playing Shogi.

It is quite basic as of now:
* You have the complete board with all the pieces. 
* Each piece allows only legal movements. Check Shogi rules here: https://en.wikipedia.org/wiki/Shogi. 
* Also, it is not allowed for a piece to go beyond the board's edges or to jump over other pieces, unless it is a Knight.
* You also have captured pieces at each side of the board.

```
Captured:
P^
     0    1    2    3    4    5    6    7    8
0   Lv   Nv   Sv   Gv   Kv   Gv   Sv   Nv   Lv
1        Rv                            R^
2   Pv   Pv   Pv   Pv   Pv   Pv   Pv        Pv
3
4
5
6   P^   P^   P^   P^   P^   P^   P^        P^
7        B^
8   L^   N^   S^   G^   K^   G^   S^   N^   L^
Captured:
Pv, Pv, Bv
```

The white pieces are on the upper side and the black ones are on the lower side of the board.
The blacks always start the game. See the example in this repo's shogi.py

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

Note: you can use shogi.py as an example and develop your own games.
You can even create a program that reads the moves from command line and avoids crash when illegal moves are made, giving the players a second chance.

# Contributions
These functionalities are not yet developed:
* Promotion of pieces (crowning) (see https://en.wikipedia.org/wiki/Shogi#Promotion)
* Drops (see https://en.wikipedia.org/wiki/Shogi#Drops)
* Check and checkmate (see https://en.wikipedia.org/wiki/Shogi#Check)

Also, see the issues that don't have any related pull request in this repo.

Have fun! :)
