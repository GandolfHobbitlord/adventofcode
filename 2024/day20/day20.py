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


def dijkstra(data,start,stop):
    q =[]
    score_dict = defaultdict(lambda: 1e12)
    # q = (steps, pos,dir)
    visited = set()
    q.append((0,start))
    heapq.heapify(q)
    while q:
        score, pos = heapq.heappop(q)

        if score > score_dict[(pos)] or pos in visited:
            continue
        score_dict[(pos)] = score

        if pos == stop:
            return score_dict
        visited.add(pos)

        for nx,ny in get_neighbor(data,pos):
            if data[ny][nx] != '#':
                    s = (score+1 ,(nx,ny))
                    heapq.heappush(q,s)

print(data)
start= find_pos(data,'S')
goal = find_pos(data,'E')
cost = dijkstra(data,start,goal)
saves = []
for y in range(len(data)):
    print(y)
    for x in range(0,len(data[0])):
        if data[y,x] == '#':
            costs = sorted([cost[(nx,ny)] for nx,ny in get_neighbor(data,(x,y)) if data[ny,nx] != '#'])
            # print(costs)
            if len(costs) >1:
                save = costs[-1] - costs[0] -2
                print((x,y), save)
                saves.append(save)
# for (kx,ky), v in cost.items():
#     print(v)
#     data[ky,kx] = int(v)
# print(data)
print(sorted(saves))
print(sum([s > 99 for s in saves]))
# print(len(sorted(saves)))


# saves = sorted([no_cheat-c for c in cheats])
# saves = [i for i in saves if i >= 100]
# print(len(saves))
