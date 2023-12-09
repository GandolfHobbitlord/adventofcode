from pathlib import Path
import numpy as np

with open(Path("2023") / "day9" / "day9_input.txt") as f:
# with open(Path("2023") / "day9" / "day9_test.txt") as f:
    data = [np.array(line.split(' '),dtype=int) for line in f.read().split('\n')]

def extrapolate_history(line):
    curr = line
    d = []
    while not np.all(curr == 0):
        d.append(curr)
        curr = np.diff(curr)
    return d

def part2(data):
    ans = 0
    for line in data:
        d = extrapolate_history(line)
        d.reverse()
        place_holder = 0
        for arr in d:
            place_holder = arr[0] - place_holder
        ans += place_holder
    return ans

def part1(data):
    ans = 0
    for line in data:
        d = extrapolate_history(line)
        d.reverse()
        place_holder = 0
        for arr in d:
            place_holder = arr[-1] + place_holder
        ans += place_holder
    return ans

print(f'Answer part 1: {part1(data)}')
print(f'Answer part 2: {part2(data)}')