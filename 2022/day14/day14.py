import re
from pathlib import Path
import numpy as np
from collections import Counter
from collections import defaultdict

def parse_line(line):
    print(line)
    return [(int(x), int(y)) for x,y in re.findall(r'(\d+),(\d+)', line)]
    print(m)
    # return int(lo), hi
def print_cave(cave, offset_x=0):
    a = np.zeros(((10,504)),dtype=str)
    a[:] = ' '
    for x,y in cave:
        a[y,x] = '#'
    print(a[:, offset_x:])

def create_map(data):
    cave = set()
    for line in data:
        for p1, p2 in zip(line, line[1:]):
            for x in range(min(p1[0],p2[0]), max(p1[0],p2[0])+1):
                for y in range(min(p1[1],p2[1]), max(p1[1],p2[1])+1):
                    # print(x,y)
                    cave.add((x,y))

    # print_cave(cave,offset_x=494)
    return cave


with open(Path("2022") / "day14" / "day14_input.txt") as f:
# with open(Path("2022") / "day14" / "day14_test.txt") as f:

    data = [parse_line(x) for x in f.read().splitlines()]
cave = create_map(data)
x_sand, y_sand = (500,0)
cnt = 0
# lowest = max([y for x,y in cave])
# print(lowest)
# while True:
#     if y_sand > lowest:
#         print(cnt)
#         exit()
#     if (x_sand, y_sand + 1) not in cave:
#         y_sand += 1
#     elif (x_sand - 1, y_sand + 1) not in cave:
#         x_sand -= 1
#         y_sand += 1
#     elif (x_sand + 1, y_sand + 1) not in cave:
#         x_sand += 1
#         y_sand += 1
#     else:
#         cave.add((x_sand,y_sand))
#         print(f"new sand at {x_sand,y_sand}")
#         x_sand, y_sand = (500,0)
#         cnt += 1
print(data)

lowest = max([y for x,y in cave]) + 2

while True:
    if y_sand == lowest - 1:
        cave.add((x_sand,y_sand))
        print(f"new sand at {x_sand,y_sand}")
        x_sand, y_sand = (500,0)
        cnt += 1
    if (x_sand, y_sand + 1) not in cave:
        y_sand += 1
    elif (x_sand - 1, y_sand + 1) not in cave:
        x_sand -= 1
        y_sand += 1
    elif (x_sand + 1, y_sand + 1) not in cave:
        x_sand += 1
        y_sand += 1
    else:
        cnt += 1
        if y_sand == 0:
            print(cnt)
            exit()
        cave.add((x_sand,y_sand))
        print(f"new sand at {x_sand,y_sand}")
        x_sand, y_sand = (500,0)