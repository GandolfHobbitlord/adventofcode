import re
from pathlib import Path
import numpy as np

blizz_dirs = {'>' : (1,0), '<' : (-1,0), 'v' : (0,1), '^' : (0,-1)}
dir_map = {v: k for (k, v) in blizz_dirs.items()}
with open(Path("2022") / "day24" / "day24_input.txt") as f:
# with open(Path("2022") / "day24" / "day24_test.txt") as f:
    data = [list(x) for x in f.read().splitlines()]
visited_pos = set()
data = np.array(data)

RIGHT_WALL = len(data[0]) -1
BOTTOM_WALL = len(data) -1
print(BOTTOM_WALL)
print(BOTTOM_WALL)

cols = 0
def parse_data(data):
    rows = len(data)
    cols = len(data[0])
    blizzards = set()
    walls = set()

    for x in range(cols):
        for y in range(rows):
            if data[y][x] in blizz_dirs:
                dir = blizz_dirs[data[y][x]]
                print(x,y, dir)
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

    # print(map)
    for pos_x, pos_y, steps in q:
        pos = (pos_y,pos_x)
        if map[pos] != '.':
            raise NameError(f'DANGER DANGER {pos_x,pos_y}')
        map[pos] = 'X'

    print(map)
    # print("\n")



blizz, walls = parse_data(data)
print(f'{walls=}')
print(f'{blizz=}')

new_q = set()
current_step = 0
new_q.add((1,0))
# print_map(blizz,walls,q)
target_number  = 0
for i in range(1000000000):
    print(i)
    blizz = advance_blizz(blizz,walls)
    q = new_q.copy()
    new_q = set()
    while q:
        pos_x, pos_y = q.pop()
        blizz_pos = list([pos for pos, dir in blizz])
        neighbors = [(pos_x,pos_y), (pos_x-1,pos_y), (pos_x+1,pos_y), (pos_x,pos_y-1), (pos_x,pos_y+1)]
        for n in neighbors:
            if n not in walls and n not in blizz_pos and n[1] >= 0:
                new_q.add(n)
                if target_number == 0:
                    if n == (RIGHT_WALL-1,BOTTOM_WALL):
                        print('Found pos, ', i+1)
                        new_q = set()
                        new_q.add(n)
                        q.clear()
                        target_number +=1
                if target_number == 1:
                    if n == (1,0):
                        print('Found pos, ', i+1)
                        new_q = set()
                        new_q.add(n)
                        q.clear()
                        target_number +=1
                if target_number == 2:
                    if n == (RIGHT_WALL-1,BOTTOM_WALL):
                        print('Found pos, ', i+1)
                        exit()