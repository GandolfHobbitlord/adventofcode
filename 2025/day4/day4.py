from pathlib import Path

def get_neighbors(r, c, grid,diag=False):
    ### Get valid neighbors for a cell in the grid. ###
    neighbors = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if diag == True:
        dirs += [(-1,-1),(1,-1), (-1,1), (1,1)]
    for dr, dc in dirs:  # Up, Down, Left, Right
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            neighbors.append((nr, nc))
    return neighbors

def parse_line(line):
    return [s for s in line]

with open(Path("2025") / "day4" / "day4_input.txt") as f:
# with open(Path("2025") / "day4" / "day4_test.txt") as f:
    data = [parse_line(line) for line in f.read().split('\n')]

valids = [True]
tot_removed = 0
part1 = None

while len(valids) != 0:
    valids = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] != '@':
                continue
            roll_neighbors = len([(yy,xx) for yy,xx in get_neighbors(y,x,data,diag=True) if data[yy][xx] == '@'])
            if roll_neighbors < 4:
                valids.append((x,y))

    for x,y in valids:
        data[y][x] = '.'
    if part1 is None:
        part1 = len(valids)
    tot_removed += len(valids)

print(f"Answer part1: {part1}")
print(f"Answer part2: {tot_removed}")

