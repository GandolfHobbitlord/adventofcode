import numpy as np
from pathlib import Path
from collections import defaultdict

def part1(adapters):
    adapters.sort()
    diffs = np.diff(adapters,prepend=0,append=adapters[-1]+3)
    return (diffs==1).sum(), (diffs == 3).sum()

def part2(adapters):
    adapters.sort()
    adapters = np.append(adapters, adapters[-1]+3)
    comb = defaultdict(int)
    comb[0] = 1 # number of combinations for key
    for x in adapters:
        comb[x] = comb[x-1] + comb[x-2] + comb[x-3] #if adapter doesn't exist it will default to 0
    return comb[adapters[-1]]

def run_tests():
    inp = np.array([16,10,15,5,1,11,7,19,6,12,4])
    assert part1(inp.copy()) == (7,5)
    assert part2(inp.copy()) == 8

    inp = np.array([28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3])
    assert part1(inp.copy()) == (22,10)
    assert part2(inp.copy()) == 19208

run_tests()

with open(Path("2020") / "day10" / "day10_input.txt") as f:
    inp = np.array([int(x) for x in f.read().splitlines()])

ones,threes = part1(inp)
print(f"One jumps {ones} and threes {threes}, ans {ones*threes} ")
print(f"Number of combinations of adapters {part2(inp)}")