from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def parse_line(line):
    return [l for l in line] + [' '] #append ' ' column to make logic work later
def parse_last_line(line):
    return [l for l in line] + [' ']


with open(Path("2025") / "day6" / "day6_input.txt") as f:
# with open(Path("2025") / "day6" / "day6_test.txt") as f:
    data = [line for line in f.read().split('\n')]
numbers = np.array([parse_line(l) for l in data[:-1]])
ops = parse_last_line(data[-1])
print(numbers)
print(ops)

def part2(ops, numbers):
    curr_op = None
    ans  = 0
    # print(numbers)
    curr_nums = []
    for op, col in zip(ops,numbers.T):
        if np.all(col == ' '):
            res = curr_op(curr_nums)
            # print(res, curr_op, curr_nums)
            curr_nums =[]
            ans += res
            continue
        if op != ' ':
            curr_op = np.sum if op == '+' else lambda a : np.prod(a,dtype=np.longlong)
        curr_nums.append(int("".join(col)))
    print(ans)
    # numbers = np.array(numbers,dtype=str)
    # num_chars = max([len(n) for n in numbers.flatten()])
    # for i in range(numbers.shape[0]):
    #     for j in range(numbers.shape[1]):
    #         numbers[i,j] = numbers[i,j].ljust(num_chars,'0')

    # for op, col in zip(ops,numbers.T):
    #     print(col)
    #     a = np.array([list(l) for l in col],dtype=int)
    #     print(a)
part2(ops,numbers)