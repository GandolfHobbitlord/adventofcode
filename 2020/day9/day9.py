import itertools
from pathlib import Path
import numpy as np
from operator import add

with open(Path("2020") / "day9" / "day9_input.txt") as f:
    numbers = [int(x) for x in f.read().splitlines()]

def get_perm(s):
    return set(sum(perm) for perm in itertools.permutations(s,2))

def run_test():
    keys = [i for i in range(1,26)]
    s = get_perm(keys)
    assert 26 in s
    assert 49 in s
    assert 100 not in s
    assert 50 not in s

run_test()

# part 1
for i in range(25,len(numbers)):
    valid = get_perm(numbers[i-25:i])
    if numbers[i] not in valid:
        ans1 = numbers[i]
        break
print(f"Part 1: First invalid number is: {ans1}")
# part 2
for start in range(len(numbers)):
    for end in range(start+2, len(numbers)):
        window = numbers[start:end]
        sum_ = sum(numbers[start:end])
        if sum_ == ans1:
            print(f"Part 2: Sum of min and max is: {min(window) + max(window)}")
            exit(1)
        elif sum_ > ans1: #optimization
            break
