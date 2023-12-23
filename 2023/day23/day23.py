from pathlib import Path
import numpy as np
import re

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
q = [(start, set())]
max_steps = []
while q:
    curr_pos, visited = q.pop()
    if curr_pos == finish:
        max_steps.append(len(visited))
        continue
    visited.add(curr_pos)
    if data[curr_pos] in dir:
        forced_dir_y, forced_dir_x = dir[data[curr_pos]]
        new_pos = (curr_pos[0] + forced_dir_y, curr_pos[1] + forced_dir_x)
        if new_pos not in visited:
            q.append((new_pos, visited.copy()))
    else:
        for neighbor in get_neighbor(data,curr_pos):
            if data[curr_pos] != '#' and neighbor not in visited:
                q.append((neighbor, visited.copy()))
print(sorted(max_steps,reverse=True))