

from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict
import heapq
global grid_size_x
global grid_size_y
N = (0,-1)
W = (-1,0)
E = (1,0)
S = (0,1)


with open(Path("2024") / "day16" / "day16_input.txt") as f:
# with open(Path("2024") / "day16" / "day16_test.txt") as f:
    data = np.array([list(line) for line in f.read().split('\n')])
print(data)

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
def print_path(data,visited):
    m = data.copy()
    for x,y in visited:
        m[y,x] = 'X'
    print(m)

def djikstra(data,start,stop):
    q =[]
    score_dict = defaultdict(lambda: 1e12)
    # q = (steps, pos,dir, visited)
    q.append((0,start,E,set()))
    heapq.heapify(q)
    while q:
        score,pos,curr_dir,v = heapq.heappop(q)
        if score > score_dict[(pos,curr_dir)]:
            continue
        score_dict[(pos,curr_dir)] = score
        visited = v.copy()
        if pos == stop:
            return score
        visited.add(pos)
        for nx,ny in get_neighbor(data,pos):
            if data[ny][nx] != '#' and (nx,ny) not in visited:
                    new_dir = (nx-pos[0], ny-pos[1])
                    if new_dir != curr_dir:
                        n_score = score + 1001
                    else:
                        n_score = score + 1
                    s = (n_score,(nx,ny),new_dir,visited.copy())
                    heapq.heappush(q,s)

start = np.where(data == 'S')
start = start[1][0], start[0][0]
end = np.where(data == 'E')
end = end[1][0], end[0][0]
print(djikstra(data,start,end))
print(start)
print(end)