import re
from pathlib import Path
import numpy as np
from collections import Counter
from collections import defaultdict
a = {}
enumerate('SabcdefghijklmnopqrstuvwxyzE')
for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
    a[letter] = i
a['S'] = -1
a['E'] = 26


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

def find_shortest_path(grid_levels, start_pos, finish_pos):
    tot_risk = np.full(grid_levels.shape, np.inf)
    q = []
    q.append(start_pos)
    tot_risk[start_pos] = 0
    visited = set()

    while q:
        vertice = q.pop()
        if vertice in visited:
            continue
        curr_risk = tot_risk[vertice]
        for neighbor in get_neighbor(grid_levels, vertice):
            if grid_levels[neighbor] - grid_levels[vertice] > 1:
                continue
            # new_risk = curr_risk + grid_levels[neighbor]
            new_risk = curr_risk + 1 #grid_levels[neighbor]

            if new_risk < tot_risk[neighbor]:
                # tot_risk[neighbor] = new_risk
                tot_risk[neighbor] = int(new_risk)

            if (neighbor not in visited):
                q.append(neighbor)
        visited.add(vertice)
        # TODO Use a heap, list is sorted each time but developer time < runtime
        q = sorted(q, key=lambda x: tot_risk[x], reverse=True)
    # print(tot_risk)
    return tot_risk[finish_pos]

def parse_line(line):
    m = re.findall(r'(\w)', line)
    return [a[letter] for letter in m]

with open(Path("2022") / "day12" / "day12_input.txt") as f:
    data = np.array([parse_line(x) for x in f.read().splitlines()])
print(data)


target = np.where(data == a['E'])
target = list(zip(*np.where(data == a['E'])))[0]
start = list(zip(*np.where(data == a['S'])))[0]
data[start] = a['a']
data[target] = a['z']
tars = []
# for s in list(zip(*np.where(data == a['a']))):
#     tars.append(find_shortest_path(data,start,target))


