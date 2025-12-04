from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def get_neighbors(r, c, grid,diag=False):
    ### Get valid neighbors for a cell in the grid. ###
    neighbors = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if diag == True:
        dirs += [(-1,-1),(1,-1), (-1,1), (1,1)]
    for dr, dc in dirs:  # Up, Down, Left, Right
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            neighbors.append((nr, nc))
    return neighbors

def parse_line(line):
    return [s for s in line]
    return int(lo), int(hi), char, password

with open(Path("2025") / "day4" / "day4_input.txt") as f:
# with open(Path("2025") / "day4" / "day4_test.txt") as f:
    # data = [line for line in f.read().split('\n')]
    data = [parse_line(line) for line in f.read().split('\n')]
valids = []
print(data)
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] != '@':
            continue
        # print(x,y)
        rolls = 0
        for yy,xx in get_neighbors(y,x,data,diag=True):
            if data[yy][xx] == '@':
                rolls +=1
        if rolls < 4:
            valids.append((x,y))

for x,y in valids:
    data[y][x] = 'X'
print(np.array(data))

print(len(valids))
