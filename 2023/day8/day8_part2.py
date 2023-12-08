from pathlib import Path
import math
import re
from itertools import cycle

def parse_map(m):
    map = {}
    for line in m.splitlines():
        lo, left, right = re.findall(r'\w+',line)
        map[lo] = (left,right)
    return map


with open(Path("2023") / "day8" / "day8_input.txt") as f:
# with open(Path("2023") / "day8" / "day8_test.txt") as f:
    step_order, m = [line for line in f.read().split('\n\n')]
map = parse_map(m)
dir = {'L' : 0, 'R' : 1}
start = [k for k in map.keys() if k[-1] == 'A']
steps = []
# Did some dirty assumptions that the first loop would be the same as the rest
for key in start:
    stepper = cycle(step_order)
    step = 0
    while key[-1] != 'Z':
        step += 1
        d = next(stepper)
        key = map[key][dir[d]]
    steps.append(step)
print(steps)
print(math.lcm(*steps))