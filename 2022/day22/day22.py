import re
from pathlib import Path
from collections import deque
import numpy as np

def create_map(data):
    points = {}
    for line in range(len(data)):
        for pos in range(len(data[line])):
            if data[line][pos] != ' ':
                points[pos,line] = data[line][pos]
    return points

def create_map(data):
    lines = len(data)
    width = max([len(line) for line in data])
    points = np.full((lines,width), ' ')
    for line in range(len(data)):
        for pos in range(len(data[line])):
            points[line,pos] = data[line][pos]
    return points

with open(Path("2022") / "day22" / "day22_input.txt") as f:
    map, dir = f.read().split('\n\n')
movements = [(int(val[:-1]), val[-1]) for val in re.findall(r'\d+\w',dir)]

map = create_map(map.splitlines())
print(map)

directions = deque([np.array((0,1)), np.array((1,0)), np.array((0,-1)),np.array((-1,0))])
pos = np.array((0,0))
while map[tuple(pos)] == ' ':
    pos += np.array([0,1])

dims = map.shape
for steps, rot in movements:
    current_dir = directions[0]
    for i in range(steps):
        next_pos = (pos + current_dir) % dims
        while map[tuple(next_pos)] == ' ':
            next_pos = (next_pos + current_dir) % dims
        if map[tuple(next_pos)] == '.':
            pos = next_pos
        elif map[tuple(next_pos)] == '#':
            continue
        else:
            raise KeyError('OH Nooo')

    if rot == 'R':
        directions.rotate(-1)
    elif rot == 'L':
        directions.rotate(1)
    else:
        raise KeyError('OH Nooo')
        # elif next_pos not in map:
        #     if current_dir == [1,0]
final_pos = pos +1
print(np.dot(final_pos,[1000,4]))