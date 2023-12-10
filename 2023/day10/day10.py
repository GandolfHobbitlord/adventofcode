from pathlib import Path
from collections import defaultdict

N = (0,-1)
W = (-1,0)
E = (1,0)
S = (0,1)
dirs = [N,W,E,S]

chars = {
    '|' : [N, S],
    '-' : [W, E],
    'L' : [N, E],
    'J' : [N, W],
    '7' : [S, W],
    'F' : [S, E],
    '.' : []}

def parse_map(map):
    out = defaultdict(lambda: '.')
    for y, line in enumerate(map.splitlines()):
        for x, char in enumerate(line):
            if char == 'S':
                start = (x,y)
            out[(x,y)] = char
    return out,start

def get_possible_moves(data,pos):
    new_pos = []
    for d in chars[data[pos]]:
        a = (pos[0] + d[0], pos[1] + d[1])
        new_pos.append(a)
    return new_pos


# with open(Path("2023") / "day10" / "day10_input.txt") as f:
with open(Path("2023") / "day10" / "day10_test.txt") as f:
    data,start = parse_map(f.read())

# Get start dir as we don't know which way we can go from "S"
for d in dirs:
    pos = (start[0] + d[0], start[1] + d[1])
    if start in get_possible_moves(data,pos):
        start_dir = pos
        break

visited = [start]
steps = 1
next_pos = [start_dir]

while next_pos:
    pos = next_pos.pop() #No need for array but it was quick to do
    visited.append(pos)
    for new_pos in get_possible_moves(data,pos):
        if new_pos not in visited:
            steps += 1
            next_pos.append(new_pos)

print(f'Answer part 1: {(steps+1) // 2}')

# Spent a long time until i realised it just asked for the area of the polygon of all the points
# after some googling found shoelace formula
visited.append(start)
area = 0
for (x0,y0), (x1,y1) in zip(visited,visited[1:]):
    area += (y0 + y1+2)*(x1-x0) / 2
area = int(abs(area))

# Was then stumped and had to get a tip about "Pick's formula" to get all the way. TIL
i = area - (len(visited) -1)/ 2 + 1
print(f'Answer part 2: {int(i)}')