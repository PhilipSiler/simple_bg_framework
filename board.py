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
    
    def list_single_moves(self):
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

                        

    def list_moves_no_double(self): #should not send back duplicates
        child_boards = []
        #if checker on bar
        if self.h_bar > 0: 
            child_boards.extend(self.list_moves_in_from_bar()) #finds all ways to get one checker off of the bar
            if len(child_boards) == 0:
                return [self] #cannot come in from bar, so we return the current board state as we cannot make any changes

            #check if a checker is still on the bar:
            if child_boards[0].h_bar > 0:
                temp_child_boards = []
                for c_b in child_boards:
                    if c_b.h_bar > 0: # check if still have checker on the bar
                        temp_child_boards.extend(c_b.list_moves_in_from_bar())

                #if we could did have two checkers on the bar but could only bring ONE checker in, then temp_child_boards should have len = 0 and we can return child_boards
                if len(temp_child_boards) == 0:
                    b = child_boards.fin
                    return find_unique_and_sort(child_boards)
                #else, we were able to bring in two checkers and thus should return temp_child_boards, which should really only have one item in it
                else:
                    return find_unique_and_sort(temp_child_boards)

        #if checker not on bar, this must also account for what to do when 
        #so potentially one, or two dice to use
        #first, check if child_boards has any existing boards, which would mean we came in from the bar. check for legal moves from those positions, those now become child_boards
        if len(child_boards) > 0:
            temp_child_boards = []
            for c_b in child_boards:
                temp_child_boards.extend(c_b.list_single_moves()) #get single
            child_boards = temp_child_boards
            return child_boards 
        
        #at this point, no checkers were on the bar so we just need to list legal moves without worrying about coming in
        child_boards = self.list_single_moves()
        temp_child_boards = []
        for c_b in child_boards:
            temp_child_boards.extend(c_b.list_single_moves())

        return temp_child_boards

        
    
    def list_moves_double(self):
        return []
    
    #splits up requests into list_moves_double and list_moves_no_double
    def list_moves(self):
        if len(self.dice) == 4:
            return self.list_moves_double()
        else:
            return self.list_moves_no_double()
        #returns a list of possible next moves, given a Board
        #first, check if we are on the bar
        

            

        return True
    
    def has_won(self):
        #checks if there are any remaining positive values in points. If yes, returns False, if no, returns True.
        return True
    