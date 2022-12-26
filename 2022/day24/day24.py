from pathlib import Path
import numpy as np

blizz_dirs = {'>' : (1,0), '<' : (-1,0), 'v' : (0,1), '^' : (0,-1)}
dir_map = {v: k for (k, v) in blizz_dirs.items()}

with open(Path("2022") / "day24" / "day24_input.txt") as f:
    data = [list(x) for x in f.read().splitlines()]

RIGHT_WALL = len(data[0]) -1
BOTTOM_WALL = len(data) -1

def parse_data(data):
    rows = len(data)
    cols = len(data[0])
    blizzards = set()
    walls = set()

    for x in range(cols):
        for y in range(rows):
            if data[y][x] in blizz_dirs:
                dir = blizz_dirs[data[y][x]]
                blizzards.add(((x,y), dir))
            elif data[y][x] == '#':
                walls.add((x,y))

    return blizzards,walls

def advance_blizz(blizz, walls):
    new_set = set()
    # print(walls)
    for pos, dir in blizz:
        pos_x,pos_y = pos
        dir_x,dir_y = dir
        n_x = pos_x + dir_x
        n_y = pos_y + dir_y

        if (n_x,n_y) in walls:
            if n_x == 0:
                n_x = RIGHT_WALL -1
            elif n_x == RIGHT_WALL:
                n_x = 1
            elif n_y == 0:
                n_y = BOTTOM_WALL -1
            elif n_y == BOTTOM_WALL:
                n_y = 1
            else:
                raise IndexError("Uh OH")
        new_set.add(((n_x,n_y),dir))
    return new_set

def print_map(blizz,walls,q):
    map =np.full((BOTTOM_WALL+1,1+RIGHT_WALL),'.')
    for w in walls:
        w = (w[1],w[0])
        map[w] = '#'
    for cord, dir in blizz:
        cord = (cord[1], cord[0])
        if map[cord] == '.':
            map[cord] = dir_map[dir]
        elif map[cord] in blizz_dirs:
            map[cord] = '2'
        else:
            map[cord] = str(int(map[cord]) +1)
    for pos_x, pos_y in q:
        pos = (pos_y,pos_x)
        if map[pos] != '.':
            raise NameError(f'DANGER DANGER {pos_x,pos_y}')
        map[pos] = 'X'

    print(map)

blizz, walls = parse_data(data)
new_q = set()
current_step = 0
new_q.add((1,0))
target_number  = 0
targets = [(RIGHT_WALL-1,BOTTOM_WALL), (1,0), (RIGHT_WALL-1,BOTTOM_WALL)]

for i in range(1000000000):
    if targets[target_number] in new_q:
        print(f'Found pos after {i} steps ')
        new_q = set([targets[target_number]])
        target_number +=1
        if target_number > 2:
            exit()

    blizz = advance_blizz(blizz,walls)
    q = new_q.copy()
    new_q = set()
    blizz_pos = set([pos for pos, dir in blizz])
    occupied = walls | blizz_pos
    while q:
        pos_x, pos_y = q.pop()
        neighbors = [(pos_x,pos_y), (pos_x-1,pos_y), (pos_x+1,pos_y), (pos_x,pos_y-1), (pos_x,pos_y+1)]
        for n in neighbors:
            if n not in occupied and n[1] >= 0:
                new_q.add(n)
