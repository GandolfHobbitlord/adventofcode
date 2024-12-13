from pathlib import Path
import numpy as np

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

def get_same_neighbor(mat,pos):
    for x,y in get_neighbor(mat,pos):
        if data[pos[1],pos[0]] == data[y,x]:
            yield x,y


def get_fences(mat,blob):
    num = 0
    for pos in blob:
        num += 4 - len(list(get_same_neighbor(mat,pos)))
    return num

with open(Path("2024") / "day12" / "day12_input.txt") as f:
# with open(Path("2024") / "day12" / "day12_test.txt") as f:
    data = np.array([list(line) for line in f.read().split('\n')])
# data = [parse_line(line) for line in f.read().split('\n')]
print(data)
h,w = data.shape
visited = set()
blobs =[]
for x in range(w):
    for y in range(h):
        if (x,y) in visited:
            continue
        val = data[y,x]
        q = [(x,y)]
        blob = set()
        while q:
            pos = q.pop()
            blob.add(pos)
            q += [(nx,ny) for nx,ny in get_same_neighbor(data,pos) if (nx,ny) not in blob]
        visited |= blob
        blobs.append(blob)
print(blobs)

ans = [get_fences(data,b) * len(b) for b in blobs]
print(sum(ans))