from pathlib import Path
import numpy as np
import re
from collections import defaultdict
N = (0,-1)
W = (-1,0)
E = (1,0)
S = (0,1)
dirs = [N,W,E,S]

chars = {
    '|' : [N, S],
    '-' : [W, E],
    'L' : [N, E],
    'J' : [N, W],
    '7' : [S, W],
    'F' : [S, E],
    '.' : []}

def parse_map(map):
    out = defaultdict(lambda: '.')
    for y, line in enumerate(map.splitlines()):
        for x, char in enumerate(line):
            if char == 'S':
                start = (x,y)
            out[(x,y)] = char
    return out,start

def get_possible(data,pos):
    new_pos = []
    for d in chars[data[pos]]:
        a = (pos[0] + d[0], pos[1] + d[1])
        new_pos.append(a)
    return new_pos


# with open(Path("2023") / "day10" / "day10_input.txt") as f:
with open(Path("2023") / "day10" / "day10_test.txt") as f:
    data,start = parse_map(f.read())
print(start)

for d in dirs:
    pos = (start[0] + d[0], start[1] + d[1])
    print('curr', pos)
    if start in get_possible(data,pos):
        start_dir = pos
        break

visited = [start,start_dir]
steps = 1
pos = start_dir
next_pos = [start_dir]

while next_pos:
    pos = next_pos.pop()
    visited.append(pos)
    for new_pos in get_possible(data,pos):
        if new_pos not in visited:
            steps += 1
            next_pos.append(new_pos)

print('Tot steps', (steps + 1) // 2)
    # for entrance in chars[data[pos]]:
    #     print(entrance)