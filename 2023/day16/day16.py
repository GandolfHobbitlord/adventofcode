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
def parse_line(line):
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password


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

energized = np.zeros_like(data,dtype=int)
# energized[:] = '.'
beams = [((0,0),E)]
seen = set()
while beams:
    print(beams)
    (x,y), dir = beams.pop()
    energized[y,x] = energized[y,x] + 1
    val = data[y,x]
    for new_dir in change_dir[(val,dir)]:
        new_pos = (x+new_dir[0], y+new_dir[1])
        if is_valid_pos(new_pos) and (new_pos,new_dir) not in seen:
            seen.add((new_pos,new_dir))
            beams.append((new_pos,new_dir))
        print(new_pos)
    print(energized)
print(data)
print(energized)
print(np.sum(energized > 0))