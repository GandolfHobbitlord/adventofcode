from pathlib import Path
import numpy as np
import re

def parse_line(line):
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

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

with open(Path("2023") / "day21" / "day21_input.txt") as f:
# with open(Path("2023") / "day21" / "day21_test.txt") as f:
    data = np.array([list(line) for line in f.read().split('\n')])
    # data = [parse_line(line) for line in f.read().split('\n')]


start = np.where(data=='S')
def print_map(mat, pos):
    m = mat.copy()
    for p in pos:
        m[p] = 'O'
    for row in m:
        print(''.join(r for r in row))
    # print(m)
positions = set([(start[0][0], start[1][0])])
print(positions)
data[start] = '.'
print(positions)
for step in range(64):
    new_pos = set()
    for pos in positions:
        for neighbor in get_neighbor(data,pos):
            if data[neighbor] == '.':
                new_pos.add(neighbor)
    print(f'{step=}')
    print_map(data,new_pos)
    positions = new_pos.copy()
print(len(positions))
