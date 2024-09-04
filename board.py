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
    
    def print_points(self):
        print("================" + ("x" * self.h_bar)) #print hero bar
        for point in self.points:
            if point == 0:
                print("|")
            elif point > 0:
                print("x" * point) #print hero points
            else:
                print("o" * point) #print villain points
        print("================" + ("o" * self.v_bar)) #print villain bar

    def reverse(self):
        reversed_points = self.points[::-1]
        for i in range(len(reversed_points)):
            reversed_points[i] *= -1
        reversed = Board(reversed_points, self.v_bar, self.h_bar, []) #instantiate new board
        return reversed
    
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
        for p in self.points:
            if p > 0:
                return False
        if self.h_bar > 0: #if any checkers on bar
            return False
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
        for i_p in range(17, 24): #points for hero's home board, represented as indices [17:23]
            p = self.points[i_p]
            if p > 0: #if there is a checker on point i_p
                for i_d, d in enumerate(self.dice): #check all possible dice that we can use to move that checker
                    if self.is_move_legal_bearoff(i_p, d):
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
        return child_boards
    
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


    def remove_incomplete_moves(self, child_boards): #removes moves which did not use as many dice as possible
        next_child_boards = []
        min_dice_remaining = 4 #if we could not use any die during doubles

        for c_b in child_boards:
            min_dice_remaining = min(len(c_b.dice), min_dice_remaining)

        for c_b in child_boards:
            if len(c_b.dice) == min_dice_remaining:
                next_child_boards.append(c_b)
        
        return next_child_boards
    
    def remove_moves_which_used_smaller_die(self, child_boards): #rare edge case: if you have a board where you can move either a 6 or a 3, but not both, you must move the 6.
        next_child_boards = []
        smallest_die_remaining = 6
        for c_b in child_boards:
            smallest_die_remaining = min(smallest_die_remaining, c_b.dice[0]) #only one die remaining, so we can just pull the single die at index 0

        for c_b in child_boards:
            if c_b.dice[0] == smallest_die_remaining: #if the die is the smallest die, and therefore the larger die has been used, return those boards
                next_child_boards.append(c_b)

        return next_child_boards
    
    def finalize_move_list(self, child_boards):
        next_child_boards = self.remove_incomplete_moves(child_boards) #remove moves which don't use as many of the dice as possible
        num_dice_remaining = len(next_child_boards[0].dice)
        if num_dice_remaining == 1:
            next_child_boards = self.remove_moves_which_used_smaller_die(next_child_boards)
        return next_child_boards

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

        if len(next_child_boards) > 0:
            child_boards = next_child_boards
        child_boards = sorted(list(set(child_boards)))
        if len(child_boards) == 0: #if there are no legal moves
            child_boards.append(self) #append the current board as the next node
        child_boards = self.finalize_move_list(child_boards)
        return child_boards #return next possible boards
    
