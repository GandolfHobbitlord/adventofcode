from pathlib import Path
import numpy as np
import re

def print_if_potential_tree(grid,sec):
    grid = grid.astype(str)
    grid[grid != '0'] = 'X'
    grid[grid == '0'] = '.'
    ss = [''.join(row) for row in grid]
    if sum(['XXXXXXX' in s for s in ss]) != 0 :
        print(sec)
        for s in ss:
            print(s)

def xy_to_grid(a, size):
    res = np.zeros((size)).astype(np.int16)
    xx,yy = tuple(zip(*a))
    np.add.at(res, (yy,xx), 1)
    return res

def parse_line(line):
    x,y, vx,vy =[int(i) for i in re.findall(r'-?\d+', line)]
    return np.array((x,y)), np.array((vx,vy))

with open(Path("2024") / "day14" / "day14_input.txt") as f:
    h,w = 103,101
    bots = [parse_line(line) for line in f.read().split('\n')]

def move_bot(bot,sec):
    pos, v = bot
    new_pos =pos + v*sec
    new_pos[0] = new_pos[0] % w
    new_pos[1] = new_pos[1] % h
    return new_pos, v

def score(mat):
    #assume odd
    h,w = mat.shape
    a = h // 2
    b = w // 2
    return np.prod([np.sum(mat[:a,:b]), np.sum(mat[:a,b+1:]), np.sum(mat[a+1:,:b]), np.sum(mat[a+1:,b+1:])])

a = [move_bot(bot,100)[0] for bot in bots]
print(f'Answer part1: {score(xy_to_grid(a,(h,w)))}')


#Part2
for i in range(0,10000):
    a = [move_bot(bot,i)[0] for bot in bots]
    print_if_potential_tree(xy_to_grid(a,(h,w)),sec=i)


