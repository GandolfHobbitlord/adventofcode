from pathlib import Path
import numpy as np
import re
import itertools

with open(Path("2024") / "day8" / "day8_input.txt") as f:
# with open(Path("2024") / "day8" / "day8_test.txt") as f:
    data = [list(line) for line in f.read().split('\n')]
data = np.array(data)

def is_valid_pos(pos):
    x, y = pos
    max_y, max_x = data.shape
    if x < 0 or x >= max_x:
        return False
    if y < 0 or y >= max_y:
        return False
    return True

antenna_types = set(data[np.where(data != '.')])
nodes = set()
for type in antenna_types:
    ys, xs = np.where(data==type)
    print(type)
    poss = list(zip(xs,ys))
    for (x0,y0) , (x1,y1)  in itertools.permutations(poss,2):
        dx = x1 - x0
        dy = y1 - y0
        pos = x0 - dx, y0 - dy
        print(pos)
        if is_valid_pos(pos):
            nodes.add(pos)
print(len(nodes))