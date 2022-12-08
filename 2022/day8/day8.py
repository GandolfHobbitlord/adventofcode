from pathlib import Path
from collections import Counter
from collections import defaultdict
import re
import numpy as np

def parse_line(line):
    m = re.findall(r'(\d)', line)
    return [int(x) for x in m]

def see_trees(arr):
    curr_largest = -1
    visible = np.zeros(arr.shape)
    for i, val in enumerate(arr):
        if val > curr_largest:
            visible[i] = 1
            curr_largest = val
        else:
            continue
    curr_largest = -1
    for i, val in enumerate(np.flip(arr),):
        if val > curr_largest:
            visible[len(visible)-1-i] = 1
            curr_largest = val
        else:
            continue
    return visible

def part1(data):
    row_list = []
    col_list = []
    for row in data:
        row_list.append(see_trees(row))
    for col in data.T:
        col_list.append(see_trees(col))
    a1 = np.array(row_list)
    a2 = np.array(col_list).T
    a3 = np.logical_or(a1 ==1 , a2 == 1)
    print(np.sum(a3))

dirs = [(-1,0), (1,0), (0,1), (0,-1)]

def part_2(grid):
    output = np.ones_like(grid)
    i,j = grid.shape
    for ii in range(i):
        for jj in range(j):
            for dir in dirs:
                dir_count = 0
                di = ii
                dj = jj
                orig = grid[ii,jj]
                while True:
                    di += dir[0]
                    dj += dir[1]
                    if di < 0 or dj < 0:
                        break
                    if di >= i or dj >= j:
                        break
                    dir_count +=1
                    if grid[di,dj] >= orig:
                        break
                output[ii,jj] *= dir_count
    print(np.max(output))

with open(Path("2022") / "day8" / "day8_input.txt") as f:
    data = np.array([parse_line(x) for x in f.read().splitlines()])

part1(data)
part_2(data)