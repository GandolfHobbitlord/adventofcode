import re
from pathlib import Path

def parse_line(line):
    return [(int(x), int(y)) for x,y in re.findall(r'(\d+),(\d+)', line)]

def create_map(data):
    cave = set()
    for line in data:
        for p1, p2 in zip(line, line[1:]):
            for x in range(min(p1[0],p2[0]), max(p1[0],p2[0])+1):
                for y in range(min(p1[1],p2[1]), max(p1[1],p2[1])+1):
                    cave.add((x,y))
    return cave


with open(Path("2022") / "day14" / "day14_input.txt") as f:
# with open(Path("2022") / "day14" / "day14_test.txt") as f:
    data = [parse_line(x) for x in f.read().splitlines()]

def move_sand(pos, cave):
    x_sand, y_sand = pos
    if (x_sand, y_sand + 1) not in cave:
        y_sand += 1
    elif (x_sand - 1, y_sand + 1) not in cave:
        x_sand -= 1
        y_sand += 1
    elif (x_sand + 1, y_sand + 1) not in cave:
        x_sand += 1
        y_sand += 1
    return x_sand, y_sand

def part1(data):
    cave = create_map(data)
    new_pos = (500,0)
    cnt = 0
    lowest = max([y for x,y in cave])
    while True:
        old_pos = new_pos
        new_pos = move_sand(old_pos,cave)
        if new_pos == old_pos:
            cave.add(new_pos)
            cnt += 1
            new_pos = 500,0
        if new_pos[1] > lowest:
            return cnt

def part2(data):
    cave = create_map(data)
    new_pos = (500,0)
    cnt = 0
    lowest = max([y for _,y in cave]) + 2
    while True:
        old_pos = new_pos
        new_pos = move_sand(old_pos,cave)
        if new_pos[1] == lowest - 1:
            cnt += 1
            cave.add(new_pos)
            new_pos = (500,0)
        elif new_pos == old_pos:
            cnt += 1
            if new_pos[1] == 0:
                return cnt
            cave.add(new_pos)
            new_pos = (500,0)

print(f"Part 1 {part1(data)}")
print(f"Part 2 {part2(data)}")