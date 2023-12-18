from pathlib import Path
import numpy as np
import re

N = (0,-1)
W = (-1,0)
E = (1,0)
S = (0,1)
change_dir = {
    ('\\', N) : [W],
    ('\\', W) : [N],
    ('\\', E) : [S],
    ('\\', S) : [E],
    ('/', N)  : [E],
    ('/', W)  : [S],
    ('/', E)  : [N],
    ('/', S)  : [W],
    ('-', N)  : [W,E],
    ('-', W)  : [W],
    ('-', E)  : [E],
    ('-', S)  : [W,E],
    ('|', N)  : [N],
    ('|', W)  : [N,S],
    ('|', E)  : [N,S],
    ('|', S)  : [S],
    ('.', N)  : [N],
    ('.', W)  : [W],
    ('.', E)  : [E],
    ('.', S)  : [S],
}

with open(Path("2023") / "day16" / "day16_input.txt") as f:
# with open(Path("2023") / "day16" / "day16_test.txt") as f:
    data = np.array([list(line) for line in f.read().split('\n')])

def is_valid_pos(pos):
    x, y = pos
    max_y, max_x = data.shape
    if x < 0 or x >= max_x:
        return False
    if y < 0 or y >= max_y:
        return False
    return True

def calc_energized(data,beam):
    beams = [beam]
    energized = np.zeros_like(data,dtype=int)
    # energized[:] = '.'
    seen = set()
    while beams:
        # print(beams)
        (x,y), dir = beams.pop()
        energized[y,x] = energized[y,x] + 1
        val = data[y,x]
        for new_dir in change_dir[(val,dir)]:
            new_pos = (x+new_dir[0], y+new_dir[1])
            if is_valid_pos(new_pos) and (new_pos,new_dir) not in seen:
                seen.add((new_pos,new_dir))
                beams.append((new_pos,new_dir))
    tot_energized = np.sum(energized > 0)
    return tot_energized

part1 = calc_energized(data,((0,0),E))
print(f'Answer Part 1: {part1}')
max_y, max_x = data.shape
starts = []
for col_pos in range(max_x):
    starts.append(((col_pos, 0), S))
    starts.append(((col_pos, max_y-1), N))

for row_pos in range(max_y):
    starts.append(((0, row_pos), E))
    starts.append(((max_x-1, row_pos), W))

best = 0
for beam in starts:
    val = calc_energized(data,beam)
    if val > best:
        best = val
print(f'Answer Part 2: {best}')
