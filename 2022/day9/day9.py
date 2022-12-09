from pathlib import Path
import re
from collections import Counter
from collections import defaultdict
import itertools
import numpy as np
dirs = {'R': (1,0), 'U' :(0,1), 'D' :(0,-1),'L' :(-1,0),}
def parse_line(line):
    m = re.match(r'(\w) (\d+)', line)
    dir, steps =  m.groups()
    return dir, int(steps)

    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

with open(Path("2022") / "day9" / "day9_input.txt") as f:
    data = [parse_line(x) for x in f.read().splitlines()]

visited = defaultdict(int)
visited[(0,0)] += 1
tail_pos = (0,0)
head_pos = (0,0)

for d, steps in data:
    print(d,steps)
    for _ in range(steps):
        head_pos = (head_pos[0] + dirs[d][0], head_pos[1] + dirs[d][1])
        h_x = head_pos[0]
        h_y = head_pos[1]
        t_x = tail_pos[0]
        t_y = tail_pos[1]
        diff_x = h_x - t_x
        diff_y = h_y - t_y
        move_x = 0
        move_y = 0
        if abs(diff_x) + abs(diff_y) > 2:
            move_x = np.clip(diff_x,-1,1)
            move_y = np.clip(diff_y,-1,1)
        elif abs(diff_x) > 1:
            move_x = np.clip(diff_x,-1,1)
        elif abs(diff_y) > 1:
            move_y = np.clip(diff_y,-1,1)
        tail_pos = (tail_pos[0] + move_x, tail_pos[1] + move_y)
        # print('Tail',tail_pos)
        visited[tail_pos] += 1
    # print('Head',head_pos)
    # print(tail_pos)
print(visited)
print(len(visited))

# print(data)
