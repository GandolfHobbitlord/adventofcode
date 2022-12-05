import re
from pathlib import Path


def part1(moves, stacks):
    for num_pop, start, dest in moves:
        print(f"{num_pop}=")
        for i in range(num_pop):
            stacks[dest].append(stacks[start].pop())
    return score(stacks)

def part2(moves, stacks):
    for num_pop, start, dest in moves:
        print(f"{num_pop}=")
        new_stack = []
        for i in range(num_pop):
            new_stack.insert(0,stacks[start].pop())

        stacks[dest].extend(new_stack)
    return score(stacks)

def parse_crates(crates):
    crates = crates.splitlines()
    stacks = list()
    for i in range(20):
        stacks.append([])

    for line in crates[:-1]:
        for num, char in enumerate(line[1::4],1):
            if char != ' ':
                stacks[num].insert(0,char)
    return stacks

def parse_moves(line):
    m = re.findall(r'\d+', line)
    return [int(x) for x in m]

def score(stacks):
    score =""
    for s in stacks:
        if len(s) !=0:
            score += s[-1]
    print(score)

with open(Path("2022") / "day5" / "day5_input.txt") as f:
    crates, moves = [x for x in f.read().split('\n\n')]
stacks = parse_crates(crates)
print(moves)
moves = [parse_moves(move) for move in moves.splitlines()]
print(stacks)

part1(moves.copy(),stacks.copy())
part2(moves.copy(),stacks.copy())
# print(stacks)