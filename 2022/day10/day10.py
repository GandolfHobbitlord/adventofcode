from pathlib import Path
import re
from collections import Counter
from collections import defaultdict
import itertools
import numpy as np
dirs = {'R': (1,0), 'U' :(0,1), 'D' :(0,-1),'L' :(-1,0),}
def parse_line(line):
    m = re.match(r'(\w) (\d+)', line)
    dir, steps =  m.groups()
    return dir, int(steps)

with open(Path("2022") / "day10" / "day10_input.txt") as f:
    data = [x for x in f.read().splitlines()]

print(data)
cycle = 0
start = 0
X = [1]
for line in data:
    cmd = line.split()
    if cmd[0] == 'noop':
        cycle += 1
        X.append(X[-1])
        continue
    elif cmd[0] == 'addx':
        for _ in range(1):
            X.append(X[-1])
        print(cmd[1])
        cycle += 1
        X.append(X[-1] + int(cmd[1]))
    else:
        print("ERROR")
# X.pop(0)
# print(X)
get_signals = [20, 60, 100, 140, 180, 220]
print(sum([X[x-1]*x for x in get_signals]))