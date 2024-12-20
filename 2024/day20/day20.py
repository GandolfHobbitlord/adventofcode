from pathlib import Path
import numpy as np
from collections import defaultdict
import heapq

def find_pos(mat,char):
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

start= find_pos(data,'S')
goal = find_pos(data,'E')
cost = dijkstra(data,start,goal)
saves = []

def get_cheats(cost,max_mann):
    saves = []
    for k0 in cost.keys():
        for k1 in cost.keys():
            if cost[k0] > cost[k1]: # bug of the day to forget this line
                continue
            man_dist = abs(k0[0] - k1[0]) + abs(k0[1] - k1[1])
            if man_dist <= max_mann:
                saves.append(abs(cost[k0] - cost[k1]) - man_dist)
    return saves
ans1 = len([s for s in get_cheats(cost,max_mann=2) if s >= 100 ])
ans2 = len([s for s in get_cheats(cost,max_mann=20) if s >= 100 ])

print(f'Answer part 1 {ans1}')
print(f'Answer part 2 {ans2}')
