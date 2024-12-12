from pathlib import Path
import numpy as np


with open(Path("2024") / "day10" / "day10_input.txt") as f:
# with open(Path("2024") / "day10" / "day10_test.txt") as f:
    data = [list(line) for line in f.read().split('\n')]
    data = np.array(data).astype(int)
print(data)

def in_range(mat,n):
    bounds = mat.shape
    for pos, bound in zip(n,bounds):
        if pos < 0 or pos >= bound:
            return False
    return True

def get_neighbor(mat, pos):
    x,y  = pos
    neighbors = [(y-1,x), (y+1,x), (y,x-1), (y,x+1)]
    for n in neighbors:
        if in_range(mat,n):
            yield n[1], n[0]

yy,xx = np.where(data== 0)

tot_trail_heads = 0
for x, y in zip(xx,yy):
    q = []
    q.append(((x,y),set()))
    visited_heads = set()
    trail_heads = 0
    while q:
        (x,y), visited = q.pop()
        visited.add((x,y))
        curr_val = data[y,x]
        if curr_val == 9 and (x,y) not in visited_heads:
            trail_heads += 1
            # visited_heads.add((x,y))
            continue
        for nx, ny in get_neighbor(data,(x,y)):
            if data[ny,nx] == curr_val +1:
                q.append(((nx,ny), visited))
    print(trail_heads)
    tot_trail_heads += trail_heads
print(tot_trail_heads)