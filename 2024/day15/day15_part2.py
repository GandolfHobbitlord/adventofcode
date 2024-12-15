from pathlib import Path

N = (0,-1)
W = (-1,0)
E = (1,0)
S = (0,1)
grid_size_x = None
grid_size_y = None
dir_map = {"^" : N, ">" : E, 'v' : S, "<" : W}

def print_grid(grid):
    for y in range(grid_size_y+1):
        line = ""
        for x in range(grid_size_x+1):
            line += grid[(x,y)]
        print(line)

def convert_grid(data):
    data = data.replace('#', '##')
    data = data.replace('O', '[]')
    data = data.replace('.', '..')
    data = data.replace('@', '@.')
    return data


def parse_map(data):
    global grid_size_x
    global grid_size_y
    data = convert_grid(data)
    data = data.splitlines()
    grid = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            grid[(x,y)] = data[y][x]
    grid_size_x = x
    grid_size_y = y

    return grid

def find_pos(grid):
    for k,v in grid.items():
        if v == '@':
            return k

def get_next_space_LR(grid, pos,v):
    while pos in grid:
        if grid[pos] == '.':
            return pos
        elif grid[pos] == '#':
            return None
        pos = pos[0] + v[0], pos[1] +v[1]
    raise RuntimeError("Out of Bounds")


def push_blocks_UD(grid,pos,v):
    to_move = set()
    q = [pos]
    #Find all things to move
    while q:
        pos = q.pop(0)
        if grid[pos] == '.'or pos in to_move:
            continue
        elif grid[pos] == '#':
            return grid # we can't move anything
        elif grid[pos] == '[':
            q.append((pos[0] + 1, pos[1]))
        elif grid[pos] == ']':
            q.append((pos[0] - 1, pos[1]))
        to_move.add(pos)
        pos = pos[0], pos[1] + v[1]
        q.append(pos)
    # Move them, we need to swap in correct order, from furthest away to finally ourselves
    to_move = sorted(list(to_move),key=lambda x: x[1],reverse= v==S)
    for m in to_move:
        targ = m[0] + v[0], m[1] + v[1]
        grid[targ], grid[m] = grid[m], grid[targ]
    return grid

def score_grid(grid):
    return sum([x+100*y for (x,y) ,v in grid.items() if v == '['])

with open(Path("2024") / "day15" / "day15_input.txt") as f:
# with open(Path("2024") / "day15" / "day15_test.txt") as f:
    m, moves = [line for line in f.read().split('\n\n')]
    grid =parse_map(m)

for move in moves:
    pos = find_pos(grid) #find where we are because I can't be bothered to keep track
    if move == '\n':
        continue
    v = dir_map[move]
    if v in [W,E]: #just use old solution
        space_pos = get_next_space_LR(grid,pos,v)
        if space_pos == None:
            continue
        while space_pos != pos:
            next_pos = (space_pos[0] - v[0], space_pos[1] - v[1])
            grid[space_pos] = grid[next_pos]
            grid[next_pos] = '.' #just for clarity
            space_pos = next_pos
    else:
        grid = push_blocks_UD(grid,pos,v)
print_grid(grid)
print(score_grid(grid))