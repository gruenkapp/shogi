class Board(object):
    DIM = 9

    def __init__(self):
        pass

    def draw(self):
        print("   0  1  2  3  4  5  6  7  8 ")  # 9*3=27+2=29 alt 10*3=30-1=29
        print("+----------------------------+")
        for row in range(self.DIM):
            printstr = str(row) + "|" + " " * (29-2) + "|"
            print(printstr)
        print("+----------------------------+")
