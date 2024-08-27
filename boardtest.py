import unittest
from board import *

class TestComeInFromBar(unittest.TestCase):

    def test_come_in_single_checker(self):
        board = Board([1,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 1, 0, [6,4])
        result = board.list_moves_in_from_bar()
        result.sort()
        expected = [Board([1,0,0,1,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [6])] #we expect to use the [4] die to come in on index 3 in board.
        #print(repr(result[0]))
        #print(repr(expected))
        self.assertEqual(result, expected)

    def test_come_in_single_checker_with_options(self):
        board = Board([1,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 1, 0, [5,4])
        result = board.list_moves_in_from_bar()
        result.sort()
        expected = [Board([1,0,0,1,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [5]), Board([1,0,0,0,1,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [4])] 
        expected.sort()
        #print(repr(result))
        #print(repr(expected))
        self.assertEqual(result, expected) 

    def test_come_in_single_checker_closed_out(self):
        board = Board([-2,-2,-3,-4,-2,-5,0,0,0,0,0,5,0,0,0,0,3,0,5,0,0,0,0,0], 1, 0, [6,4])
        result = board.list_moves_in_from_bar()
        expected = 0 #should be no change, as no moves are possible
        print(result)
        print(expected)
        self.assertEqual(len(result), 0)

    def test_come_in_two_checkers(self):
        assert(True)

    def test_come_in_single_checker_hit_blot(self):
        assert(True)


if __name__ == '__main__':
    unittest.main()