from pathlib import Path
import functools


with open(Path("2025") / "day7" / "day7_input.txt") as f:
# with open(Path("2025") / "day7" / "day7_test.txt") as f:
    data = [list(line) for line in f.read().split('\n')]

grid_len_y = len(data)
grid_len_x = len(data[0])
def is_inside_grid(x,y):
    if x< 0 or x >= grid_len_x:
        return False
    if y < 0 or y >= grid_len_y:
        return False
    return True

@functools.cache
def get_number_of_splits(pos):
    x,y = pos
    y += 1
    if y >= grid_len_y:
        return 1
    if data[y][x] == '.':
        if is_inside_grid(x,y):
            return get_number_of_splits((x,y))
    else:
        return sum([get_number_of_splits((new_x,y)) for new_x in [x+1, x-1] if is_inside_grid(new_x,y)])

start = (data[0].index('S'),0)
print(f"Answer part2: {get_number_of_splits(start)}")
