from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict
N = (0,-1)
W = (-1,0)
E = (1,0)
S = (0,1)
grid_size_x = None
grid_size_y = None
dir_map = {"^" : N, ">" : E, 'v' : S, "<" : W}

opposite = {}
opposite[N] = S
opposite[S] = N
opposite[W] = E
opposite[E] = W
def parse_line(line):
    # [int(i) for i in re.findall(r'-?\d+', line)]
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

def print_grid(grid):
    for y in range(grid_size_y):
        line = ""
        for x in range(grid_size_x):
            line += grid[x,y]
        print(line)

def parse_map(data):
    global grid_size_x
    global grid_size_y
    data = data.splitlines()
    grid = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            grid[(x,y)] = data[y][x]
    grid_size_x = x
    grid_size_y = y

    return grid

def get_start(grid):
    for k,v in grid.items():
        if v == '@':
            return k

def get_next_space(grid, pos,v):
    while pos in grid:
        if grid[pos] == '.':
            return pos
        elif grid[pos] == '#':
            return None
        pos = pos[0] + v[0], pos[1] +v[1]
    raise RuntimeError("Out of Bounds")

def score_grid(grid):
    return sum([x+100*y for (x,y) ,v in grid.items() if v == 'O'])
with open(Path("2024") / "day15" / "day15_input.txt") as f:
# with open(Path("2024") / "day15" / "day15_test.txt") as f:
    m, moves = [line for line in f.read().split('\n\n')]
    grid =parse_map(m)

pos  = get_start(grid)
print_grid(grid)
print(moves)

for move in moves:
    if move == '\n':
        continue
    v = dir_map[move]
    nx,ny = pos[0] + v[0], pos[1] + v[1]
    space_pos = get_next_space(grid,pos,v)
    if space_pos == None:
        continue
    while space_pos != pos:
        next_pos = (space_pos[0] - v[0], space_pos[1] - v[1])
        grid[space_pos] = grid[next_pos]
        grid[next_pos] = '.' #just for clarity
        space_pos = next_pos
    # print_grid(grid)
    pos = (nx,ny)

print(score_grid(grid))