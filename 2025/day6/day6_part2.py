from pathlib import Path
import numpy as np

with open(Path("2025") / "day6" / "day6_input.txt") as f:
# with open(Path("2025") / "day6" / "day6_test.txt") as f:
    data = [line for line in f.read().split('\n')]

data = np.array([list(l) + [' '] for l in data])
numbers = data[:-1]
ops = data[-1]

def part2(ops, numbers):
    curr_op = None
    ans  = 0
    curr_nums = []

    for op, col in zip(ops,numbers.T):
        if np.all(col == ' '):
            ans += curr_op(curr_nums)
            curr_nums = []
            continue
        if op != ' ':
            curr_op = np.sum if op == '+' else lambda x : np.prod(x,dtype=np.longlong)
        curr_nums.append(int("".join(col)))
    return ans

print(f"Answer {part2(ops,numbers)}")