from pathlib import Path
import re
import numpy as np

def parse_line(line):
    return [int(i) for i in re.findall(r'-?\d+', line)]

with open(Path("2024") / "day1" / "day1_input.txt") as f:
    data = [parse_line(l) for l in f.read().strip().splitlines()]
xx = [x for x, _ in data]
yy = [y for _, y in data]

def part1(xx,yy):
    d = [abs(x-y) for x,y in zip(sorted(xx),sorted(yy))]
    return sum(d)

def part2(xx,yy):
    yy= np.array(yy)
    score = [x * np.sum(x==yy) for x in xx]
    return sum(score)

print(f'Answer part1: {part1(xx,yy)}')
print(f'Answer part2: {part2(xx,yy)}')
