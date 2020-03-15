# Test suite containing all the TestCases.

from test_board import TestBoard
from test_pawn2 import TestPawn

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestBoard)
    suite.addTest(TestPawn)
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

# python -m unittest test_shogi.py