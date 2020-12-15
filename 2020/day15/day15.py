
from collections import defaultdict, deque
from functools import partial
def play_memory_game(starting_num, last_turn):
    memory = defaultdict(partial(deque,maxlen=2))
    for turn, num in enumerate(starting_num): # Turn 0 exists, we are not matlab, lua or julia
        memory[num].append(turn)

    last_num = starting_num[-1]
    for turn in range(len(starting_num), last_turn):
        if len(memory[last_num]) == 1:
            memory[0].append(turn)
            last_num = 0
        else:
            last_num = memory[last_num][1] - memory[last_num][0]
            memory[last_num].append(turn)
    return last_num

def run_test():
    assert 0 == play_memory_game([0,3,6],10)
    assert 1 == play_memory_game([1,3,2],2020)

run_test()
print(f"Answer part1 {play_memory_game([9,12,1,4,17,0,18],2020)}")
print(f"Answer part2 {play_memory_game([9,12,1,4,17,0,18],30000000)}")
