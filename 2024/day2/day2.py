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

def is_safe(l):
    d = [x-y for x,y in zip(l,l[1:])]
    # print(d)
    d = np.array(d)
    safe = np.all(d < 0) | np.all(d > 0)
    safe = safe and np.all(np.abs(d) < 4) and np.all(d != 0)
    return safe

def solve(data,part2=False):
    ans=0
    for l in data:
        if is_safe(l):
            ans+=1
        elif part2:
            for i in range(1,len(l)+1):
                a = l[0:i-1] + l[i:]
                if is_safe(a):
                    ans += 1
                    break
    return ans
with open(Path("2024") / "day2" / "day2_input.txt") as f:
# with open(Path("2024") / "day2" / "day2_test.txt") as f:
    # data = [line for line in f.read().split('\n')]
    data = [parse_line(line) for line in f.read().split('\n')]
    ans = 0

print(solve(data))
print(solve(data,part2=True))
