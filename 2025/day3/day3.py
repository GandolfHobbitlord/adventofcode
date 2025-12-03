from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def parse_line(line):
    return [int(i) for i in line]

with open(Path("2025") / "day3" / "day3_input.txt") as f:
# with open(Path("2025") / "day3" / "day3_test.txt") as f:
    # data = [line for line in f.read().split('\n')]
    data = [parse_line(line) for line in f.read().split('\n')]

def get_largest(line, pos,tot):
    num_to_right = tot - (pos+1)
    if num_to_right:
        largest = sorted(line[:-num_to_right])[-1]
    else:
        largest = sorted(line)[-1]
    i = line.index(largest)
    return largest, line[i+1:]

def get_joltage(data,num_batteries):
    ans = []
    for line in data:
        s = ""
        l = line.copy()
        for pos in range(num_batteries):
            largest,l = get_largest(l,pos,num_batteries)
            s+=str(largest)
        ans.append(int(s))
    return sum(ans)
print(f"Total joltage part 1: {get_joltage(data,2)}")
print(f"Total joltage part 2: {get_joltage(data,12)}")
