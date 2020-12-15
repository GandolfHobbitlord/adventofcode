
from collections import defaultdict
def part1(starting_num, max_turn):
    memory = defaultdict(list)
    for turn, num in enumerate(starting_num):
        memory[num].append(turn)
    turn = len(starting_num)
    last_num = starting_num[-1]
    while(turn < max_turn):
        if len(memory[last_num]) == 1:
            memory[0].append(turn)
            last_num = 0
        elif len(memory[last_num]) > 1:
            diff = memory[last_num][-1] - memory[last_num][-2]
            memory[diff].append(turn)
            last_num = diff
        turn+=1
    return last_num

def run_test():
    assert 0 == part1([0,3,6],10)
    assert 1 == part1([1,3,2],2020)

run_test()
print(f"Answer part1 {part1([9,12,1,4,17,0,18],2020)}")
print(f"Answer part2 {part1([9,12,1,4,17,0,18],30000000)}")
