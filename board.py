import unittest

def find_unique_and_sort(boards):
    return sorted(list(set(boards)))

class Board:
    #h_bar = hero checkers on bar, v_bar = villain checkers on bar. Dice is an array of either len 0, 2, or 4.
    #hero is trying to go left to right.
    def __init__(self, points = None, h_bar = 0, v_bar = 0, dice = None):
        if points is None:
            self.points = [2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2]
        else:
            self.points = points

        if dice is None:
            self.dice = []
        else:
            self.dice = dice
        self.h_bar = h_bar
        self.v_bar = v_bar

    def __eq__(self, other):
        if not isinstance(other, Board):
            return False
        return (self.points == other.points and
                self.h_bar == other.h_bar and
                self.v_bar == other.v_bar and
                self.dice == other.dice)
    
    def __hash__(self):
        return hash((tuple(self.points), self.h_bar, self.v_bar, tuple(self.dice)))
    
    def __repr__(self):
        return (f"BackgammonBoard(points={self.points}, "
                f"h_bar={self.h_bar}, v_bar={self.v_bar}, dice={self.dice})")
    
    def __lt__(self, other):
        if not isinstance(other, Board):
            return NotImplemented
        return (self.points, self.h_bar, self.v_bar, self.dice) < (other.points, other.h_bar, other.v_bar, other.dice)
    
    def update_board(self, start, end):
        #implements the movement of a single die, expressed as a start point or an end point. -1 start is the bar, anything above 23 has been moved off the board
        return True
    
    def is_move_legal(self, end):
        if end >= 0 and end < 24 and self.points[end] >= -1:
            return True
        
    def is_move_legal_bearoff(self, start, die):
        min_index_with_checker = 0 #used to determine whether we can use larger rolls to bear checkers off of smaller points
        #for instance, can we use a 6 to bear off a 3, or a 2 to bear off a 1.
        for i in range(23, 16, -1):
            if self.points[i] > 0:
                min_index_with_checker = i

        if start + die <= 24: #moving piece forward or bearing it off using the exact number
            return True
        if start == min_index_with_checker: #moving piece from the back always allowed,
            return True
        return False
        
    def is_on_bar(self):
        return self.h_bar > 0
    
    def is_bearing_off(self):
        for p in self.points[:18]:
            if p > 0:
                return False #there is at least one hero checker on points 0 - 17
        return True #there is not at least one checker on points 0 - 17
        
    def is_won(self):
        #checks if there are any remaining positive values in points. If yes, returns False, if no, returns True.
        return True
        
    def list_moves_in_from_bar(self): #these will only return any next positions that use up one die if there are any. 
        child_boards = []
        for i, d in enumerate(self.dice):
            if self.is_move_legal(d - 1):
                temp_dice = self.dice.copy()
                temp_dice.pop(i) #remove the used dice
                temp_h_bar = self.h_bar
                temp_h_bar -= 1
                temp_v_bar = self.v_bar
                temp_points = self.points.copy()
                temp_points[d - 1] += 1
                if temp_points[d - 1] == 0: #this checks to see if we came in and hit a blot
                    #if we did come in and hit a blot, then we need to put the enemy checker 
                    #where points[point] was equal to -1, now it is equal to 0 after we incremented it) 
                    temp_v_bar += 1
                    #and we need to increment the point we came in on again, to actually put our chcker
                    temp_points[d - 1] += 1
                temp_board = Board(temp_points, temp_h_bar, temp_v_bar, temp_dice)
                child_boards.append(temp_board)
        return child_boards
    
    def list_moves_bearing_off(self):
        child_boards = []
        for i_p, p in enumerate(self.points[17:]): #points for hero's home board, represented as indices [17:23]
            if p > 0: #if there is a checker on point i_p
                for i_d, d in enumerate(self.dice): #check all possible dice that we can use to move that checker
                    if self.is_move_legal(i_p, d):
                        temp_dice = self.dice.copy()
                        temp_dice.pop(i_d) #remove the used die
                        temp_h_bar = self.h_bar #should always be zero
                        temp_v_bar = self.v_bar
                        temp_points = self.points.copy()
                        temp_points[i_p] -= 1 #subtract a checker from the start point p
                        if i_p + d <= 23: #if checker is still on the board and has not yet been borne off
                            temp_points[i_p + d] += 1 # add a checker to the new point p + d
                            #if new point p + d == 0, that means we just hit a blot
                            if temp_points[i_p + d] == 0: 
                                temp_v_bar += 1 #add one checker to villain bar
                                temp_points[i_p + d] += 1
                        temp_board = Board(temp_points, temp_h_bar, temp_v_bar, temp_dice)
                        child_boards.append(temp_board)
        return child_boards.append()
    
    def list_moves_standard(self):
        child_boards = []
        for i_p, p in enumerate(self.points):
            if p > 0: #there is a checker on this point, find all ways to use different dice to move this
                for i_d, d in enumerate(self.dice):
                    if self.is_move_legal(i_p + d):
                        temp_dice = self.dice.copy()
                        temp_dice.pop(i_d) #remove the used die
                        temp_h_bar = self.h_bar
                        temp_v_bar = self.v_bar
                        temp_points = self.points.copy()
                        temp_points[i_p] -= 1 #subtract a checker from the start point p
                        temp_points[i_p + d] += 1 # add a checker to the new point p + d
                        #if new point p + d == 0, that means we just hit a blot
                        if temp_points[i_p + d] == 0:
                            temp_v_bar += 1 #add one checker to villain bar
                            temp_points[i_p + d] += 1
                        temp_board = Board(temp_points, temp_h_bar, temp_v_bar, temp_dice)
                        child_boards.append(temp_board)
        return child_boards

    
    def list_moves_helper(self):
        if self.is_on_bar():
            return self.list_moves_in_from_bar()
        elif self.is_bearing_off():
            return self.list_moves_bearing_off()
        else:
            return self.list_moves_standard()

    def list_moves(self):
        #basic idea: for as long as there are dice to be moved and new moves being generated in each successive generation of possible moves, we continue to generate new child_board sets
        child_boards = []
        child_boards = self.list_moves_helper() #first die
        next_child_boards = []
        for c_b in child_boards:
            next_child_boards.extend(c_b.list_moves_helper()) #second die

        next_child_boards = sorted(list(set(next_child_boards)))
        if len(self.dice) > 2: #this only happens if doubles were rolled
            child_boards = next_child_boards
            next_child_boards = []
            for c_b in child_boards:
                next_child_boards.extend(c_b.list_moves_helper()) #third die
            next_child_boards = sorted(list(set(next_child_boards)))
            child_boards = next_child_boards
            next_child_boards = []
            for c_b in child_boards:
                next_child_boards.extend(c_b.list_moves_helper()) #third die

        return sorted(list(set(next_child_boards))) # return
        
    
