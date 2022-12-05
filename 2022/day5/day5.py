import re
from pathlib import Path
import copy

def parse_crates(crates):
    num_bins = max(get_numbers(crates))
    stacks = list()
    for _ in range(num_bins+1):
        stacks.append([])

    crates = crates.splitlines()
    for line in crates[:-1]:
        for num, char in enumerate(line[1::4],1):
            if char != ' ':
                stacks[num].insert(0,char)
    return stacks

def get_numbers(line):
    return [int(val) for val in re.findall(r'\d+', line)]

def score(stacks):
    score =  "".join([s[-1] for s in stacks if len(s) != 0 ])
    return score

def part1(moves, stacks):
    stacks = copy.deepcopy(stacks)
    for num_pop, start, dest in moves:
        for i in range(num_pop):
            stacks[dest].append(stacks[start].pop())
    return score(stacks)

def part2(moves, stacks):
    stacks = copy.deepcopy(stacks)
    for num_pop, start, dest in moves:
        new_stack = []
        for i in range(num_pop):
            new_stack.insert(0,stacks[start].pop())
        stacks[dest].extend(new_stack)
    return score(stacks)

with open(Path("2022") / "day5" / "day5_input.txt") as f:
    crates, moves = [x for x in f.read().split('\n\n')]

stacks = parse_crates(crates)
moves = [get_numbers(move) for move in moves.splitlines()]

print(f"Answer Part 1: {part1(moves,stacks)}")
print(f"Answer Part 2: {part2(moves,stacks)}")
# print(stacks)