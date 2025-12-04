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
    # data = [line for line in f.read().split('\n')]
    data = [parse_line(line) for line in f.read().split('\n')]

valids = [True]
tot_removed = 0
while len(valids) != 0:
    valids = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] != '@':
                continue
            rolls = 0
            for yy,xx in get_neighbors(y,x,data,diag=True):
                if data[yy][xx] == '@':
                    rolls +=1
            if rolls < 4:
                valids.append((x,y))

    print(f"removed {len(valids)}")
    tot_removed += len(valids)
    for x,y in valids:
        data[y][x] = '.'
    # print(np.array(data))

print(tot_removed)
