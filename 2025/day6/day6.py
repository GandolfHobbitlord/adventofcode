from pathlib import Path
import numpy as np
import re


def parse_line(line):
    return [int(i) for i in re.findall(r'-?\d+', line)]
def parse_last_line(line):
    return [i for i in re.findall(r'[\+\*]', line)]

with open(Path("2025") / "day6" / "day6_input.txt") as f:
# with open(Path("2025") / "day6" / "day6_test.txt") as f:
    data = [line for line in f.read().split('\n')]
numbers = np.array([parse_line(l) for l in data[:-1]])
ops = parse_last_line(data[-1])

def part1(ops, numbers):
    return sum([col.sum() if op == '+' else np.prod(col,dtype=np.longlong) for op, col in zip(ops,numbers.T)]) # too much?

print(f"Answer part1: {part1(ops,numbers)}")