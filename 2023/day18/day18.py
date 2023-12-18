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

# with open(Path("2023") / "day18" / "day18_input.txt") as f:
with open(Path("2023") / "day18" / "day18_test.txt") as f:
    # data = [line for line in f.read().split('\n')]
    data = [parse_line(line) for line in f.read().split('\n')]
def print_dig(dug):
    maxx = max([x for x,y in dug])
    maxy = max([y for x,y in dug])
    digmap = np.zeros((maxy,maxx))


print(data)
pos = (0,0)
dug = set()
dug.add(pos)
for dir, val, hex in data:
    x,y  = dirmap[dir]
    pos = (pos[0] + x, pos[1] + y)
    dug.add(pos)
print(dug)