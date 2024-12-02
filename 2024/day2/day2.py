from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def parse_line(line):
    # print(line)
    return [int(i) for i in re.findall(r'-?\d+', line)]
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

with open(Path("2024") / "day2" / "day2_input.txt") as f:
# with open(Path("2024") / "day2" / "day2_test.txt") as f:
    # data = [line for line in f.read().split('\n')]
    data = [parse_line(line) for line in f.read().split('\n')]
    ans = 0
    for l in data:
        d = [x-y for x,y in zip(l,l[1:])]
        # print(d)
        d = np.array(d)
        safe = np.all(d < 0) | np.all(d > 0)
        safe = safe and np.all(np.abs(d) < 4) and np.all(d != 0)
        # print(l)
        # print(d)
        # print(safe)
        if safe:

            ans += 1
print(data)
print(ans)
