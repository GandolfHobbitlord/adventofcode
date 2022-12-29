from pathlib import Path
import re
import numpy as np
def parse_line(line):
    return tuple([int(x) for x in  re.findall(r'(-?\d+)', line)])


with open(Path("2022") / "day18" / "day18_input.txt") as f:
    data = list([parse_line(x) for x in f.read().splitlines()])

def get_neighbor(center):
    x,y,z = center
    yield (x+1,y,z)
    yield (x-1,y,z)
    yield (x,y+1,z)
    yield (x,y-1,z)
    yield (x,y,z+1)
    yield (x,y,z-1)

A=np.array(data)
print(A.shape)
data = set(data)
MAX= np.max(A,axis=0) + 1
MIN= np.min(A,axis=0) - 1

def in_bounds(pos):
    return all([MIN[i] <= pos[i] and MAX[i] >= pos[i] for i in range(3)])

q = [tuple(MAX)]

exposed_outside = 0
visited = set()
while q:
    pos = q.pop()
    if pos in data:
        exposed_outside +=1
        continue
    if pos not in visited:
        visited.add(pos)
        for n in get_neighbor(pos):
            if in_bounds(n):
                q.append(n)

sides = 0
for val in data:
    seen_sides = 6
    for neighbor in get_neighbor(val):
        if neighbor in data:
            seen_sides -= 1
    sides += seen_sides
print(exposed_outside)
print(sides)