from pathlib import Path
import numpy as np
import re
import heapq
from collections import defaultdict
def in_range(mat,n):
    bounds = mat.shape
    for pos, bound in zip(n,bounds):
        if pos < 0 or pos >= bound:
            return False
    return True

dir = {(-1,0) : 'N', (1,0) : 'S', (0,-1): 'W', (0,1) : 'E'}
backward = {'S': 'N', 'N' : 'S', 'W' : 'E', 'E' :'W'}

def get_dir(new,old):
    diff_y, diff_x = (new[0]-old[0], new[1]-old[1])
    return dir[(diff_y,diff_x)]

def get_neighbor(mat, pos):
    x,y  = pos
    neighbors = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    for n in neighbors:
        if in_range(mat,n):
            yield n

def is_valid_part1(neighbor,vertice,dir_str):
    d = get_dir(neighbor,vertice)
    if dir_str != '' and backward[d] == dir_str[-1]:
        return ''
    if dir_str.startswith(d):
        neighbor_dirstr = dir_str + d
    else:
        neighbor_dirstr = d
    if len(neighbor_dirstr) > 3:
        return ""
    return neighbor_dirstr

def is_valid_part2(neighbor,vertice,dir_str):
    d = get_dir(neighbor,vertice)
    if dir_str == '':
        return d
    if backward[d] == dir_str[-1]:
        return ''
    if len(dir_str) < 4:
        if dir_str.startswith(d):
            return dir_str + d
        return ""
    elif len(dir_str) < 10:
        if dir_str.startswith(d):
            return dir_str + d
        return d
    else:
        if dir_str.startswith(d):
            return ""
        return d

#modified djikstra
def find_shortest_path(grid_levels, start_pos, finish_pos):
    q = []
    dct = defaultdict(lambda: float('inf'))
    dct[(start_pos,"")] = 0
    q.append((0,"",start_pos, []))
    visited = set()
    heapq.heapify(q)
    while q:
        curr_heat ,dir_str, vertice, curr_path = heapq.heappop(q)
        if vertice == finish_pos and len(dir_str) > 3:
            print('found pos', finish_pos)
            print(curr_path)
            print(dct[(finish_pos,dir_str)])
            exit()
        if (vertice,dir_str) in visited:
            continue
        for neighbor in get_neighbor(grid_levels, vertice):
            neighbor_dirstr = is_valid_part2(neighbor,vertice,dir_str)
            if neighbor_dirstr == '':
                continue
            new_heat = curr_heat + grid_levels[neighbor]
            if new_heat < dct[(neighbor,neighbor_dirstr)]:
                 dct[(neighbor,neighbor_dirstr)] = new_heat
            if ((neighbor,neighbor_dirstr) not in visited):
                cp = curr_path.copy()
                cp.append(vertice)
                heapq.heappush(q,(new_heat,neighbor_dirstr, neighbor, cp))
        visited.add((vertice,dir_str))
    raise RuntimeError('Uh oh, no path to object')

def parse_line(line):
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

with open(Path("2023") / "day17" / "day17_input.txt") as f:
# with open(Path("2023") / "day17" / "day17_test.txt") as f:
    data = np.array([list(line) for line in f.read().split('\n')],dtype=int)
    # data = [parse_line(line) for line in f.read().split('\n')]

print(data)
finish = data.shape
finish = (finish[0] -1, finish[1] -1)
print(find_shortest_path(data,start_pos=(0,0),finish_pos=finish))