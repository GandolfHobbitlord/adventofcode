from pathlib import Path
import numpy as np

# Stole some code from the beam puzzle last year

N = (0,-1)
W = (-1,0)
E = (1,0)
S = (0,1)

with open(Path("2024") / "day6" / "day6_input.txt") as f:
# with open(Path("2024") / "day6" / "day6_test.txt") as f:
    data = np.array([list(line) for line in f.read().split('\n')])

def is_valid_pos(pos):
    x, y = pos
    max_y, max_x = data.shape
    if x < 0 or x >= max_x:
        return False
    if y < 0 or y >= max_y:
        return False
    return True

y, x = [v[0] for v in np.where(data == '^')]
pos = (x,y)

dbg = data.copy()

def part1(pos):
    visited = set()
    dirs = [N,E,S,W]
    while True:
        visited.add((pos))
        dbg[pos[1],pos[0]] = 'X'
        # print(dbg)
        curr_dir = dirs[0]
        new_pos = pos[0] + curr_dir[0], pos[1] + curr_dir[1]
        if not is_valid_pos(new_pos):
            is_valid_pos(new_pos)
            break
        elif data[new_pos[1], new_pos[0]] != '#':
            pos = new_pos
        else:
            dirs = dirs[1:] + dirs[:1]
    return len(visited)

def is_loop(pos,mappy):
    visited = set()
    dirs = [N,E,S,W]
    while True:
        dbg[pos[1],pos[0]] = 'X'
        curr_dir = dirs[0]
        if (pos,curr_dir) in visited:
            return True
        visited.add((pos,curr_dir))
        new_pos = pos[0] + curr_dir[0], pos[1] + curr_dir[1]
        if not is_valid_pos(new_pos):
            return False
        elif mappy[new_pos[1], new_pos[0]] != '#':
            pos = new_pos
        else:
            dirs = dirs[1:] + dirs[:1]

def part2(pos):
    ans = 0
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i,j] == '.':
                dist = np.copy(data)
                dist[i,j] = '#'
                if is_loop(pos,dist):
                    print(f"loop at{j,i}")
                    ans+=1
    return ans
print(f"Answer part1: {part1(pos)}")
print(f"Answer part1: {part2(pos)}")