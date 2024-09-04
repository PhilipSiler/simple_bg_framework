from board import *
import random

class Game:

    def __init__(self):
        self.nodes = []
        self.board = Board()

    def roll_dice(self):
        dice = []
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        if a == b:
            dice = [a, a, a, a]
        else:
            dice = [a, b]
        return dice
    
    def select_option(self, options, node_reward_map):
        chance_pick_other_than_best = .5
        max_val = 0
        for i, opt in enumerate(options):
            if opt in node_reward_map: #check if we have been to this board state / node before
                max_val = max(max_val, node_reward_map[opt])

        if random.random() > chance_pick_other_than_best:
            for opt in options:
                if opt in node_reward_map and node_reward_map[opt] == max_val:
                    return opt

        return random.choice(options) #return from the remaining list of options.

    #return selected next node
    def take_turn(self, node_reward_map):
        dice = self.roll_dice()
        self.board.dice = dice
        options = self.board.list_moves()
        #review options to see if any of them result in a victory
        for opt in options:
            if opt.is_won():
                return True
        
        #otherwise, simply choose randomly
        my_choice = self.select_option(options, node_reward_map)
        self.nodes.append(my_choice)
        self.board = my_choice.reverse() #update what the board is with the reversed next node selected
        return False
            

