from pathlib import Path
import numpy as np
import re
from collections import Counter, defaultdict
from itertools import cycle
def parse_line(line):
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password
def parse_map(m):
    map = {}
    for line in m.splitlines():
        # m = re.match(r'\((w+)\)= \((\w+), (\w+)\))', line)
        lo, left, right = re.findall(r'\w+',line)
        # lo, left, right = m.groups()
        print(lo,left,right)
        map[lo] = (left,right)
    return map
with open(Path("2023") / "day8" / "day8_input.txt") as f:
# with open(Path("2023") / "day8" / "day8_test.txt") as f:
    step_order, m = [line for line in f.read().split('\n\n')]
    # data = [parse_line(line) for line in f.read().split('\n\n')]
stepper = cycle(step_order)
map = parse_map(m)
key = 'AAA'
step = 0
dir = {'L' : 0, 'R' : 1}

while key != 'ZZZ':
    step += 1
    d = next(stepper)
    key = map[key][dir[d]]
print(step)
