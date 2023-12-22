from pathlib import Path
import numpy as np
import re
from matplotlib import pyplot as plt
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
row, col = data.shape
num_tiles = 1
positions = set([(start[0][0] + row * (num_tiles // 2), start[1][0] + row * (num_tiles // 2))])
data = np.tile(data,(num_tiles,num_tiles))

data[data=='S'] = '.'
def print_map(mat, pos):
    m = mat.copy()
    for p in pos:
        m[p] = 'O'
    for row in m:
        print(''.join(r for r in row))
    # print(m)
print(positions)
data[start] = '.'
print(positions)
max_steps = 5
steps = range(max_steps)
ans = []
seen = set()
seen_len = []
for step in steps:
    seen |= positions
    new_pos = set()
    for pos in positions:
        for neighbor in get_neighbor(data,pos):
            if data[neighbor] == '.':
                new_pos.add(neighbor)
    print(f'{step=}')
    # print_map(data,new_pos)
    positions = new_pos.copy()
    seen |= positions
    ans.append(len(positions))
    seen_len.append(len(seen))
s = start[0][0]
print_map(data,seen)
print((data[s-max_steps:s+max_steps+1, s-max_steps:s+max_steps+1]))
print(seen_len)
print(ans)
plt.plot(steps,ans)
plt.show()