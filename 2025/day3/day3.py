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

ans = 0
for line in data:
    largest = sorted(line)[-1]
    i = line.index(largest)
    if i == len(line)-1:
        largest = sorted(line)[-2]
        i = line.index(largest)

    print(largest, i)
    second = sorted(line[i+1:])[-1]
    res = int(str(largest) + str(second))
    print(res)
    ans += res
print(ans)