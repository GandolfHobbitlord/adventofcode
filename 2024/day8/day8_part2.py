from pathlib import Path
import numpy as np
import itertools

with open(Path("2024") / "day8" / "day8_input.txt") as f:
# with open(Path("2024") / "day8" / "day8_test.txt") as f:
    data = [list(line) for line in f.read().split('\n')]
    # data = [parse_line(line) for line in f.read().split('\n')]
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
# This code doesn't handle if dx,dy has a common denominator like 4,4
for type in antenna_types:
    ys, xs = np.where(data==type)
    poss = list(zip(xs,ys))
    for (x0,y0) , (x1,y1)  in itertools.permutations(poss,2):
        dx = x1 - x0
        dy = y1 - y0
        pos = (x0,y0)
        print(pos)
        while is_valid_pos(pos):
            nodes.add(pos)
            pos = pos[0] + -dx, pos[1] - dy
print(len(nodes))