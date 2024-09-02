import unittest
from board import *

class Test_Moves(unittest.TestCase):
    #default Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [0,0])
    def test_come_in_single_checker(self):
        board = Board([1,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 1, 0, [6,4])
        result = board.list_moves_in_from_bar()
        expected = [Board([1,0,0,1,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [6])] #we expect to use the [4] die to come in on index 3 in board.
        self.assertEqual(result, expected)

    def test_come_in_single_checker_with_options(self):
        board = Board([1,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 1, 0, [5,4])
        result = board.list_moves_in_from_bar()
        expected = [Board([1,0,0,1,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [5]), Board([1,0,0,0,1,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [4])] 
        expected.sort()
        self.assertEqual(result, expected) 

    def test_come_in_single_checker_hit(self):
        board = Board([1,0,-2,-2,-1,-3,0,0,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 1, 0, [5,4])
        result = board.list_moves_in_from_bar()
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
        result = board.list_moves_standard()
        expected = sorted([Board([1,1,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,2,1,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,4,1,0,0,0,-2], 0, 0, [])])
        self.assertEqual(result, expected)
        
    def test_list_single_moves_2(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [2])
        result = board.list_moves_standard()
        expected = sorted([Board([1,0,1,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,4,-5,1,0,0,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,2,0,6,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,4,0,1,0,0,-2], 0, 0, [])])
        self.assertEqual(result, expected)

    def test_list_single_moves_3(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [3])
        result = board.list_moves_standard()
        expected = sorted([Board([1,0,0,1,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,4,-5,0,1,0,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,2,0,5,1,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,4,0,0,1,0,-2], 0, 0, [])])
        self.assertEqual(result, expected)

    def test_list_single_moves_4(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [4])
        result = board.list_moves_standard()
        expected = sorted([Board([1,0,0,0,1,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,4,-5,0,0,1,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,2,0,5,0,1,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,4,0,0,0,1,-2], 0, 0, [])])
        self.assertEqual(result, expected)

    def test_list_single_moves_5(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [5])
        result = board.list_moves_standard()
        expected = sorted([Board([2,0,0,0,0,-5,0,-3,0,0,0,4,-5,0,0,0,4,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,2,0,5,0,0,1,0,-2], 0, 0, [])])
        self.assertEqual(result, expected)

    def test_list_single_moves_6(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [6])
        result = board.list_moves_standard()
        expected = sorted([Board([1,0,0,0,0,-5,1,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,4,-5,0,0,0,3,1,5,0,0,0,0,-2], 0, 0, []),Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,2,0,5,0,0,0,1,-2], 0, 0, [])])
        self.assertEqual(result, expected)

    def test_list_moves_65(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [6,5])
        result = board.list_moves()
        expected = [Board(points=[1, 0, 0, 0, 0, -5, 0, -3, 0, 0, 0, 6, -5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, -2], h_bar=0, v_bar=0, dice=[]),Board(points=[1, 0, 0, 0, 0, -5, 1, -3, 0, 0, 0, 4, -5, 0, 0, 0, 4, 0, 5, 0, 0, 0, 0, -2], h_bar=0, v_bar=0, dice=[]),Board(points=[1, 0, 0, 0, 0, -5, 1, -3, 0, 0, 0, 5, -5, 0, 0, 0, 2, 0, 5, 0, 0, 1, 0, -2], h_bar=0, v_bar=0, dice=[]),Board(points=[2, 0, 0, 0, 0, -5, 0, -3, 0, 0, 0, 3, -5, 0, 0, 0, 4, 1, 5, 0, 0, 0, 0, -2], h_bar=0, v_bar=0, dice=[]),Board(points=[2, 0, 0, 0, 0, -5, 0, -3, 0, 0, 0, 4, -5, 0, 0, 0, 2, 1, 5, 0, 0, 1, 0, -2], h_bar=0, v_bar=0, dice=[]),Board(points=[2, 0, 0, 0, 0, -5, 0, -3, 0, 0, 0, 4, -5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 1, -2], h_bar=0, v_bar=0, dice=[]),Board(points=[2, 0, 0, 0, 0, -5, 0, -3, 0, 0, 0, 5, -5, 0, 0, 0, 1, 0, 5, 0, 0, 1, 1, -2], h_bar=0, v_bar=0, dice=[])]
        self.assertEqual(result, expected)

    def test_bearing_off_66(self):
        board = Board([0,0,0,0,0,-5,0,-3,0,0,0,0,-5,0,0,0,0,0,5,0,3,0,0,-2], 0, 0, [6,6,6,6])
        result = board.list_moves()
        expected = [Board([0,0,0,0,0,-5,0,-3,0,0,0,0,-5,0,0,0,0,0,1,0,3,0,0,-2], 0, 0, [])]
        self.assertEqual(result, expected)

    def test_bearing_off_66_bear_off_from_5(self):
        board = Board([0,0,0,0,0,-5,0,-3,0,0,0,0,-5,0,0,0,0,0,0,2,3,0,0,-2], 0, 0, [6,6,6,6])
        result = board.list_moves()
        expected = [Board([0,0,0,0,0,-5,0,-3,0,0,0,0,-5,0,0,0,0,0,0,0,1,0,0,-2], 0, 0, [])]
        self.assertEqual(result, expected)

    def test_bearing_off_65_from_6_hit_on_1(self):
        board = Board([0,0,0,0,0,-6,0,-3,0,0,0,0,-5,0,0,0,0,0,2,0,0,0,0,-1], 0, 0, [6,5])
        result = board.list_moves()
        expected = [Board([0,0,0,0,0,-6,0,-3,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,0,1], 0, 1, [])]
        self.assertEqual(result, expected)

    def test_bearing_off_65_from_2hit_on_1(self):
        board = Board([0,0,0,0,0,-6,0,-3,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,2,-1], 0, 0, [6,5])
        result = board.list_moves()
        expected = [Board([0,0,0,0,0,-6,0,-3,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,0,-1], 0, 0, [])]
        self.assertEqual(result, expected)

    def test_can_only_move_one_die(self):
        board = Board([1,0,-2,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0, 0, [6,1])
        result = board.list_moves()
        expected = [Board([0,0,-2,0,0,0,1,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0, 0, [1])]
        self.assertEqual(result, expected)

    def test_with_one_checker_on_bar_55(self):
        board = Board([0,0,0,0,0,-5,0,-3,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,0,-2], 1, 0, [5,5,5,5])
        result = board.list_moves()
        expected = [Board([0,0,0,0,0,-5,0,-3,0,0,0,0,-5,0,0,0,0,0,0,1,0,0,0,-2], 0, 0, [])]
        self.assertEqual(result, expected)

    def test_use_both_checkers_or_one_checker(self):
        board = Board([1,0,0,0,0,-2,-2,-2,0,0,-2,1,-3,0,0,0,0,-2,0,0,0,0,0,-2], 0, 0, [6,4])
        result = board.list_moves()
        expected = [Board([1,0,0,0,0,-2,-2,-2,0,0,-2,0,-3,0,0,0,0,-2,0,0,0,1,0,-2], 0, 0, [])]
        self.assertEqual(result, expected)

    def test_is_won_true(self):
        board = Board([0,0,0,0,0,-2,-2,-2,0,0,-2,0,-3,0,0,0,0,-2,0,0,0,0,0,-2], 0, 0, [])
        result = board.is_won()
        expected = True
        self.assertEqual(result, expected)

    def test_is_won_false_checkers_on_board(self):
        board = Board([0,0,0,0,0,-2,-2,-2,0,1,-2,0,-3,0,10,0,0,-2,0,0,1,0,0,-2], 0, 0, [])
        result = board.is_won()
        expected = False
        self.assertEqual(result, expected)

    def test_is_won_false_checkers_on_bar(self):
        board = Board([0,0,0,0,0,-2,-2,-2,0,0,-2,0,-3,0,0,0,0,-2,0,0,0,0,0,-2], 1, 0, [])
        result = board.is_won()
        expected = False
        self.assertEqual(result, expected)

    def test_bear_off_43(self): #test different ways of moving checkers when bearing off
        board = Board([0,0,0,0,0,-5,0,-3,0,0,0,0,-5,0,0,0,0,0,1,0,1,1,0,0], 0, 0, [4,3])
        result = board.list_moves()
        expected = [Board([0,0,0,0,0,-5,0,-3,0,0,0,0,-5,0,0,0,0,0,1,0,0,0,0,0], 0, 0, []),Board([0,0,0,0,0,-5,0,-3,0,0,0,0,-5,0,0,0,0,0,0,0,1,0,1,0], 0, 0, []),Board([0,0,0,0,0,-5,0,-3,0,0,0,0,-5,0,0,0,0,0,0,0,0,2,0,0], 0, 0, []),Board([0,0,0,0,0,-5,0,-3,0,0,0,0,-5,0,0,0,0,0,0,0,0,1,1,1], 0, 0, [])]
        expected.sort()
        self.assertEqual(result, expected)

    def bear_off_with_extra_dice(self):
        board = Board([0,0,0,0,0,-5,0,-3,0,0,0,0,-5,0,0,0,0,0,2,0,0,0,1,-2], 0, 0, [6,6,6,6])
        result = board.list_moves()
        expected = [Board([0,0,0,0,0,-5,0,-3,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,0,-2], 0, 0, [6])]
        self.assertEqual(result, expected)
    
    
    """
    def test_list_moves_11(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [1,1,1,1])
        result = board.list_moves()
        expected = [] #we expect to use the [4] die to come in on index 3 in board.
        self.assertEqual(result, expected)

    def test_list_moves_22(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [2,2,2,2])
        result = board.list_moves()
        expected = [] #we expect to use the [4] die to come in on index 3 in board.
        self.assertEqual(result, expected)

    def test_list_moves_33(self):
        board = Board([2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2], 0, 0, [3,3,3,3])
        result = board.list_moves()
        expected = [] #we expect to use the [4] die to come in on index 3 in board.
        self.assertEqual(result, expected)
    """
if __name__ == '__main__':
    unittest.main()