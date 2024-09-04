from game import *
from board import *
import time
import collections

def play_game(node_reward_map):
    game = Game()
    is_game_finished = False
    while is_game_finished == False:
        is_game_finished = game.take_turn(node_reward_map)
    return game.nodes
    
def main():
    print("Starting program.")
    num_training_games = 500000
    reward_win = 1
    reward_loss = 1
    node_reward_map = collections.defaultdict(int)
    game_lens = [0] * num_training_games
    start_time = time.time()
    for i in range(num_training_games):
        if i % (num_training_games // min(10000, num_training_games)) == 0:
            progress = (i / num_training_games) * 100
            print(f"Progress: {progress:.2f}%", end="\r")
        nodes = play_game(node_reward_map)
        winner = False
        for node in nodes[::-1]: #iterate through nodes in reverse order to assign rewards
            if winner:
                node_reward_map[node] += reward_win
            else:
                node_reward_map[node] -= reward_loss
            winner = not winner
        game_lens[i] = len(nodes) #record total number of moves. if the program is working, then we would expect this number to roughly go down over time, at least a little bit


    end_time = time.time()
    elapsed_time = (end_time - start_time)
    print(f"\nThe function took {elapsed_time:.2f} seconds to run.")
    print(f"Average of {elapsed_time/num_training_games} per game.")
    print(max(node_reward_map.values()))
    print(min(node_reward_map.values()))
    out_filename = "output.txt"
    with open(out_filename, 'w') as my_file:
        for length in game_lens:
            my_file.write(str(length) + "\r\n")

if __name__ == "__main__":
    main()
