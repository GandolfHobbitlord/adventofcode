from pathlib import Path
import numpy as np

dirmap = {
'U' : (0,-1),
'L' : (-1,0),
'R' : (1,0),
'D' : (0,1)}

def parse_line(line):
    dir, val, hex,  = line.split(' ')
    return    dir, int(val), hex[2:-1]

with open(Path("2023") / "day18" / "day18_input.txt") as f:
# with open(Path("2023") / "day18" / "day18_test.txt") as f:
    # data = [line for line in f.read().split('\n')]
    data = [parse_line(line) for line in f.read().split('\n')]
def print_dig(dug):
    maxx = max([x for x,y in dug])
    maxy = max([y for x,y in dug])
    digmap = np.zeros((maxy+1,maxx+1),dtype=str)
    digmap[:] = '.'
    for x,y in dug:
        digmap[y,x] = '#'
    return digmap

def neighbors(pos):
    for i in [-1,1]:
        yield pos[0] + i, pos[1]
        yield pos[0] , pos[1]+i
def get_area(dug):
    area = 0
    for (x0,y0), (x1,y1) in zip(list(dug),list(dug)[1:]):
        area += (y0 + y1+2)*(x1-x0) / 2
    area = int(abs(area))
    print(area)
    return area
# print(data)
pos = (0,0)
dug = set()
dug.add(pos)
pts = []
conv = ['R','D','L','U']

for _, _, hex in data:
    dir = conv[int(hex[-1])]
    val = int(hex[:-1],16)
    print(dir,val)
    for i in range(val):
        x,y  = dirmap[dir]
        pos = (pos[0] + x, pos[1] + y)
        dug.add(pos)
    pts.append(pos)

#Pick strikes again!
area = get_area(pts + [pts[0]])
b = len(dug)
internal = area - len(dug)/2 + 1
tot_points = internal + len(dug)

print(f'{tot_points=}')
