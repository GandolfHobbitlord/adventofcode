from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict
import heapq

def parse_line(line):
    # [int(i) for i in re.findall(r'-?\d+', line)]
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password
def find_pos(mat,char ='S'):
    pos = np.where(mat==char)
    y,x = pos[0][0], pos[1][0]
    return x,y
with open(Path("2024") / "day20" / "day20_input.txt") as f:
# with open(Path("2024") / "day20" / "day20_test.txt") as f:
    data = np.array([list(line) for line in f.read().split('\n')])
    # data = [parse_line(line) for line in f.read().split('\n')]

def in_range(mat,n):
    bounds = mat.shape
    for pos, bound in zip(n,bounds):
        if pos < 0 or pos >= bound:
            return False
    return True

#pos is (x,y) return is (x,y)
def get_neighbor(mat, pos):
    x,y  = pos
    neighbors = [(y-1,x), (y+1,x), (y,x-1), (y,x+1)]
    for n in neighbors:
        if in_range(mat,n):
            yield n[1], n[0]


def dijkstra(data,start,stop,cheat = False):
    q =[]
    score_dict = defaultdict(lambda: 1e12)
    # q = (steps, pos,dir)
    visited = set()
    q.append((0,start,cheat))
    heapq.heapify(q)
    while q:
        score, pos, cheat_available = heapq.heappop(q)

        if score > score_dict[(pos)] or pos in visited:
            continue
        score_dict[(pos,cheat_available)] = score

        if pos == stop:
            return score
        visited.add(pos)

        for nx,ny in get_neighbor(data,pos):
            if data[ny][nx] != '#':
                    s = (score+1 ,(nx,ny),cheat_available)
                    heapq.heappush(q,s)


print(data)
start = find_pos(data,'S')
goal = find_pos(data,'E')
no_cheat = dijkstra(data,start,goal)
cheats = []
for y in range(1,len(data)-1):
    print(y)
    for x in range(1,len(data[0])-1):
        if data[y,x] == '#':
            cheat_data = data.copy()
            cheat_data[y,x] = '.'
            cheats.append(dijkstra(cheat_data,start,goal))

saves = sorted([no_cheat-c for c in cheats])
saves = [i for i in saves if i > 0]
print(Counter(saves))

saves = sorted([no_cheat-c for c in cheats])
saves = [i for i in saves if i >= 100]
print(len(saves))
