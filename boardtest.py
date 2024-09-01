import unittest
from board import *

class TestComeInFromBar(unittest.TestCase):
    #default Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [0,0])
    def test_come_in_single_checker(self):
        board = Board([1,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 1, 0, [6,4])
        result = board.list_moves_in_from_bar()
        result.sort()
        expected = [Board([1,0,0,1,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [6])] #we expect to use the [4] die to come in on index 3 in board.
        self.assertEqual(result, expected)

    def test_come_in_single_checker_with_options(self):
        board = Board([1,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 1, 0, [5,4])
        result = board.list_moves_in_from_bar()
        result.sort()
        expected = [Board([1,0,0,1,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [5]), Board([1,0,0,0,1,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [4])] 
        expected.sort()
        self.assertEqual(result, expected) 

    def test_come_in_single_checker_hit(self):
        board = Board([1,0,-2,-2,-1,-3,0,0,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 1, 0, [5,4])
        result = board.list_moves_in_from_bar()
        result.sort()
        expected = [Board([1,0,-2,-2,1,-3,0,0,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 1, [4])]
        expected.sort()
        self.assertEqual(result, expected)

    def test_come_in_single_checker_closed_out(self):
        board = Board([-2,-2,-3,-4,-2,-5,0,0,0,0,0,5,0,0,0,0,3,0,5,0,0,0,0,0], 1, 0, [6,4])
        result = board.list_moves_in_from_bar()
        result = len(result)
        expected = 0 #should be no change, as no moves are possible
        self.assertEqual(result, expected)

    def test_come_in_two_checkers_no_hit_no_double(self):
        board = Board([0,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 2, 0, [5,4])
        result = board.list_moves()
        expected = [Board([0,0,0,1,1,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [])]
        self.assertEqual(result, expected)

    def test_come_in_two_checkers_one_hit_no_double(self):
        board = Board([0,0,0,0,-1,-4,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 2, 0, [5,4])
        result = board.list_moves()
        expected = [Board([0,0,0,1,1,-4,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 1, [])]
        self.assertEqual(result, expected)

    def test_come_in_two_checkers_hit_twice_no_double(self):
        board = Board([0,0,0,-1,-1,-3,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 2, 0, [5,4])
        result = board.list_moves()
        expected = [Board([0,0,0,1,1,-3,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 2, [])]
        self.assertEqual(result, expected)

    def test_list_single_moves_1(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [1])
        result = board.list_single_moves()
        expected = sorted([Board([1,1,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,2,1,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,4,1,0,0,0,-2], 0, 0, [])])
        self.assertEqual(result, expected)
        
    def test_list_single_moves_2(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [2])
        result = board.list_single_moves()
        expected = sorted([Board([1,0,1,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,4,-5,1,0,0,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,2,0,6,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,4,0,1,0,0,-2], 0, 0, [])])
        self.assertEqual(result, expected)

    def test_list_single_moves_3(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [3])
        result = board.list_single_moves()
        expected = sorted([Board([1,0,0,1,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,4,-5,0,1,0,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,2,0,5,1,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,4,0,0,1,0,-2], 0, 0, [])])
        self.assertEqual(result, expected)

    def test_list_single_moves_4(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [4])
        result = board.list_single_moves()
        expected = sorted([Board([1,0,0,0,1,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,4,-5,0,0,1,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,2,0,5,0,1,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,4,0,0,0,1,-2], 0, 0, [])])
        self.assertEqual(result, expected)

    def test_list_single_moves_5(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [5])
        result = board.list_single_moves()
        expected = sorted([Board([2,0,0,0,0,-5,0,-3,0,0,0,4,-5,0,0,0,4,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,2,0,5,0,0,1,0,-2], 0, 0, [])])
        self.assertEqual(result, expected)

    def test_list_single_moves_6(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [6])
        result = board.list_single_moves()
        expected = sorted([Board([1,0,0,0,0,-5,1,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,4,-5,0,0,0,3,1,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,2,0,5,0,0,0,1,-2], 0, 0, [])])
        self.assertEqual(result, expected)

    def test_list_moves_no_double(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [6,5])
        result = board.list_single_moves()
        expected = []
        self.assertEqual(result, expected)





if __name__ == '__main__':
    unittest.main()