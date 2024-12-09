from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict


N = (0,-1)
W = (-1,0)
E = (1,0)
S = (0,1)
dirs = [N,E,S,W]



def parse_line(line):
    # [int(i) for i in re.findall(r'-?\d+', line)]
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

with open(Path("2024") / "day6" / "day6_input.txt") as f:
# with open(Path("2024") / "day6" / "day6_test.txt") as f:
    data = np.array([list(line) for line in f.read().split('\n')])
print(data)

def is_valid_pos(pos):
    x, y = pos
    max_y, max_x = data.shape
    if x < 0 or x >= max_x:
        return False
    if y < 0 or y >= max_y:
        return False
    return True

y, x = [v[0] for v in np.where(data == '^')]
pos = (x,y)

visited = set()
dbg = data.copy()
while True:
    visited.add((pos))
    dbg[pos[1],pos[0]] = 'X'
    # print(dbg)
    curr_dir = dirs[0]
    new_x, new_y = pos[0] + curr_dir[0], pos[1] + curr_dir[1]
    if not is_valid_pos((new_x,new_y)):
        is_valid_pos((new_x,new_y))
        break
    elif data[new_y, new_x] != '#':
        pos = (new_x, new_y)
    else:
        dirs = dirs[1:] + dirs[:1]
print(dbg)
print(len(visited))
print(np.sum(dbg=='X'))