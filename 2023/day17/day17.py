from pathlib import Path
import numpy as np
import re
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

def find_shortest_path(grid_levels, start_pos, finish_pos):
    tot_risk = np.full(grid_levels.shape, np.inf)
    q = []
    dct = defaultdict(lambda: float('inf'))
    dct[(start_pos,"")] = 0
    q.append((start_pos,"",0, []))
    visited = set()
    path = defaultdict(list)
    while q:
        vertice ,dir_str, curr_heat, curr_path = q.pop()
        if vertice == finish_pos:
            print('found pos', finish_pos)
            print(dct[(finish_pos,dir_str)])
            exit()
            print(tot_risk[finish_pos])
        # print(visited)
        if (vertice,dir_str) in visited:
            continue
        for neighbor in get_neighbor(grid_levels, vertice):
            d = get_dir(neighbor,vertice)
            if dir_str:
                if backward[d] == dir_str[-1]:
                    continue
            if dir_str.startswith(d):
                neighbor_dirstr = dir_str + d
            else:
                neighbor_dirstr = d
            if len(neighbor_dirstr) > 3:
                continue
            new_heat = curr_heat + grid_levels[neighbor]
            if new_heat < dct[(neighbor,neighbor_dirstr)]:
                 dct[(neighbor,neighbor_dirstr)] = new_heat
            if ((neighbor,neighbor_dirstr) not in visited):
                cp = curr_path.copy()
                cp.append(vertice)
                q.append((neighbor,neighbor_dirstr, new_heat,cp))
        visited.add((vertice,dir_str))
        # print(len(visited))

        path[vertice] = curr_path
        # TODO Use a heap, list is sorted each time but developer time < runtime
        q = sorted(q, key=lambda x: x[2], reverse=True)
    print(tot_risk.astype(int))


    index = tuple(np.array(list(zip(*path[finish_pos]))))
    grid_levels[index] = -1
    print(grid_levels)
    print([heat for (pos, _), heat in dct.items() if finish_pos == pos])
    return tot_risk[finish_pos]

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