from pathlib import Path
import re
import itertools
from operator import mul, add

def parse_line(line):
    a, l = line.split(':')
    return int(a), [int(i) for i in re.findall(r'-?\d+', l)]

with open(Path("2024") / "day7" / "day7_input.txt") as f:
# with open(Path("2024") / "day7" / "day7_test.txt") as f:
    data = [parse_line(line) for line in f.read().split('\n')]

def concat(a,b):
    return int(str(a) + str(b))

def calc(data,operands):
    ans = 0
    for target, nums in data:
        for ops in itertools.product(operands, repeat=len(nums)-1):
            part_sum = nums[0]
            for num, op in zip(nums[1:],ops):
                part_sum = op(part_sum,num)
            if part_sum == target:
                ans += part_sum
                break
    return ans

print(f"Part 1 answer: {calc(data,operands=[add,mul])}")
print(f"Part 2 answer: {calc(data,operands=[add,mul,concat])}")
