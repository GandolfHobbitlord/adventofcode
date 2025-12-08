from pathlib import Path
import numpy as np

def print_grid(grid):
    for y in range(len(grid)):
        line = ""
        for x in range(len(grid[0])):
            line += grid[y][x]
        print(line)

with open(Path("2025") / "day7" / "day7_input.txt") as f:
# with open(Path("2025") / "day7" / "day7_test.txt") as f:
    data = [list(line) for line in f.read().split('\n')]
start = data[0].index('S')


def is_inside_grid(x,y):
    if x< 0 or x >= grid_len_x:
        return False
    if y < 0 or y >= grid_len_y:
        return False
    return True

grid_len_y = len(data)
grid_len_x = len(data[0])
grid = np.array(data)
splits = set()

tachyons = [(start,0)]
while tachyons:
    x,y = tachyons.pop()
    y += 1
    if y >= grid_len_y or (x,y) in splits:
        continue
    if data[y][x] == '.':
        if is_inside_grid(x,y):
            tachyons.append((x,y))
        grid[y,x] = '|'
    else:
        splits.add((x,y))
        for new_x in [x+1, x-1]:
            if is_inside_grid(new_x,y):
                tachyons.append((new_x,y))
                grid[y,new_x] = '|'

print(f"Answer part1: {len(splits)}")