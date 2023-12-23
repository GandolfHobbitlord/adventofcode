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

def get_neighbor(mat, pos):
    x,y  = pos
    neighbors = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    for n in neighbors:
        if in_range(mat,n):
            yield n

def parse_line(line):
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

dir = {'^' : (-1,0),'>' : (0,1), 'v' : (1,0), '<' : (0,-1)}
with open(Path("2023") / "day23" / "day23_input.txt") as f:
# with open(Path("2023") / "day23" / "day23_test.txt") as f:
    data = np.array([list(line) for line in f.read().split('\n')])
    # data = [parse_line(line) for line in f.read().split('\n')]

def find_next_junction(visited,pos,edge_map, steps = 1):
    new_pos = pos
    if len(edge_map[pos]) == 2:
        visited.add((pos))
        for edge in edge_map[pos]:
            if edge not in visited:
                steps,new_pos = find_next_junction(visited.copy(),edge, edge_map, steps +1)
    return steps, new_pos

def warp(data):
    edge_map = {}
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if val != '#':
                edges = []
                for n in get_neighbor(data,(i,j)):
                    if data[n] != '#':
                        edges.append(n)
                edge_map[(i,j)] = edges
    shrunken = defaultdict(list)
    for pos, edges in edge_map.items():
        # print(pos)
        for edge in edges:
            steps, new_pos = find_next_junction(set([pos]), edge,edge_map)
            shrunken[pos].append((new_pos,steps))
    return shrunken


edge_map = warp(data)
print(edge_map[(1,2)])
print('shrinked')
def find_start_end(data):
    for i, val in enumerate(data[0]):
        if val == '.':
            start = (0,i)
            break
    finish_row, _ = data.shape
    finish_row -= 1
    for i, val in enumerate(data[-1]):
        if val == '.':
            finish = (finish_row,i)
            break
    return start, finish
# print(data)
start, finish = find_start_end(data)
q = [(start, set(),0)]
max_steps = []
while q:
    curr_pos, visited, steps = q.pop()
    if curr_pos == finish:
        max_steps.append((steps))
        continue
    visited.add(curr_pos)
    for neighbor,step in edge_map[curr_pos]:
        if neighbor not in visited:
            q.append((neighbor, visited.copy(),steps+step))
print(max(max_steps))