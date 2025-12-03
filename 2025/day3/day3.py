from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def parse_line(line):
    return [int(i) for i in line]
    return int(lo), int(hi), char, password

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
    return largest,line[i+1:]

ans = []
tot = 12
for line in data:
    s = ""
    curr_ind = 0
    l = line.copy()
    for pos in range(tot):
        largest,l = get_largest(l,pos,tot)
        s+=str(largest)
    ans.append(int(s))
    # second = sorted(line[i+1:])[-1]
    # res = int(str(largest) + str(second))
    # print(res)
    # ans += res
print(ans)
print(sum(ans))
# print(ans)