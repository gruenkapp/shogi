# Test suite containing all the TestCases.

from .test_board import TestBoard
from .test_pieces import TestPieces


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestBoard)
    suite.addTest(TestPieces)
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

# python -m unittest test_shogi.py