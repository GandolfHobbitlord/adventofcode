from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def parse_line(line):
    return [int(i) for i in re.findall(r'-?\d+', line)]
def parse_last_line(line):
    return [i for i in re.findall(r'[\+\*]', line)]

# with open(Path("2025") / "day6" / "day6_input.txt") as f:
with open(Path("2025") / "day6" / "day6_test.txt") as f:
    data = [line for line in f.read().split('\n')]
numbers = np.array([parse_line(l) for l in data[:-1]])
ops = parse_last_line(data[-1])
print(numbers)
print(ops)

def part1(ops, numbers):
    ans = 0
    for op, col in zip(ops,numbers.T):
        print(op,col)
        if op == '+':
            ans += col.sum()
        elif op == '*':
            ans += np.prod(col,dtype=np.longlong)
        else:
            raise RuntimeError(op)
        print(ans)

def part2(ops, numbers):
    numbers = np.array(numbers,dtype=str)
    num_chars = max([len(n) for n in numbers.flatten()])
    for i in range(numbers.shape[0]):
        for j in range(numbers.shape[1]):
            numbers[i,j] = numbers[i,j].ljust(num_chars,'0')

    for op, col in zip(ops,numbers.T):
        print(col)
        a = np.array([list(l) for l in col],dtype=int)
        print(a)

part2(ops,numbers)