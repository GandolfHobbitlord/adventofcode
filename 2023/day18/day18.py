from pathlib import Path
import numpy as np
import re
dirmap = {
'U' : (0,-1),
'L' : (-1,0),
'R' : (1,0),
'D' : (0,1)}

def parse_line(line):
    print(line)
    print(line.split(' '))

    dir, val, hex,  = line.split(' ')
    return    dir, int(val), hex

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

def fill(dug):
    x,y = 1,1
    while (x,y) in dug:
        y +=1
    print(x,y)
    pos_to_fill = [(x,y)]
    dug.add((x,y))
    while pos_to_fill:
        p = pos_to_fill.pop()
        # d = print_dig(dug)
        # d[p[1],p[0]] = 'O'
        # print(d)
        # print('\n')
        for neighbor in neighbors(p):
            if neighbor not in dug:
                pos_to_fill.append(neighbor)
                dug.add(neighbor)
    return dug

def neighbors(pos):
    for i in [-1,1]:
        yield pos[0] + i, pos[1]
        yield pos[0] , pos[1]+i


print(data)
pos = (0,0)
dug = set()
dug.add(pos)
for dir, val, hex in data:
    for i in range(val):
        x,y  = dirmap[dir]
        pos = (pos[0] + x, pos[1] + y)
        dug.add(pos)
        print(pos)
print(dug)
print_dig(dug)
d=fill(dug)
print_dig(d)
print(list(neighbors((1,1))))
print(len(d))