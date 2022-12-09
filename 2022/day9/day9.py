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

def simulate_rope(number_of_knots):
    visited = set()
    visited.add((0,0))
    knots = [(0,0) for _ in range(number_of_knots)]
    for d, steps in data:
        for _ in range(steps):
            knots[0] = (knots[0][0] + dirs[d][0], knots[0][1] + dirs[d][1])
            for i in range(0,len(knots)-1):
                head_pos = knots[i][0], knots[i][1]
                tail_pos = knots[i+1][0], knots[i+1][1]
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
                knots[i+1] = tail_pos
                # print('Tail',tail_pos)
            visited.add(knots[-1])
        # print('Head',head_pos)
        # print(tail_pos)
    print(len(visited))
simulate_rope(2) # Why isn't head a knot :(
simulate_rope(10)

# print(data)
