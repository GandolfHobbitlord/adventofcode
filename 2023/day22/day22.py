from pathlib import Path
import re
from collections import defaultdict

def parse_line(line):
    x0,y0,z0, x1,y1,z1 = [int(x) for x in re.findall(r'\d+',line)]
    pos = [(x0,x1), (y0,y1), (z0,z1)]
    return [tuple(sorted(p)) for p in pos]

with open(Path("2023") / "day22" / "day22_input.txt") as f:
# with open(Path("2023") / "day22" / "day22_test.txt") as f:
    data = [parse_line(line) for line in f.read().split('\n')]
data = sorted(data, key=lambda pos : pos[2])
data = [tuple(d) for d in data]


def drop(block, ground):
    ground_below_block = []
    (x0,x1), (y0,y1), (z0,z1) = block
    for x in range(x0,x1+1):
        for y in range(y0,y1+1):
            ground_below_block.append(ground[(x,y)])
    top = max(ground_below_block)
    dz = z0-top - 1
    return (x0,x1), (y0,y1), (z0-dz,z1-dz)

def drop_blocks(blocks):
    ground = defaultdict(int)
    new_tower = []
    fallen= 0
    for block in blocks:
        # print(block)
        dropped_block = drop(block,ground)
        new_tower.append(dropped_block)
        if dropped_block != block:
            fallen += 1
        (x0,x1), (y0,y1), (z0,z1) = dropped_block
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                ground[(x, y)] = z1
    return new_tower, fallen

fallen_tower, _ = drop_blocks(data)
assert fallen_tower == drop_blocks(fallen_tower.copy())[0]
assert 0 == drop_blocks(fallen_tower.copy())[1]

total_fallen = 0
ok_to_remove = 0
for i in range(len(fallen_tower)):
    new_tower = fallen_tower[:i] + fallen_tower[i+1:]
    _, fallen = drop_blocks(new_tower.copy())
    if fallen == 0:
        ok_to_remove += 1
    total_fallen += fallen

print(f'Answer part 1:{ok_to_remove}')
print(f'Answer part 2:{total_fallen}')
