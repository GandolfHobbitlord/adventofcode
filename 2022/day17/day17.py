from pathlib import Path

data = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
with open(Path("2022") / "day17" / "day17_input.txt") as f:
    data = f.read()
DOWN = 'v'
import itertools
def spawn_rock(tower, rock_number):
    highest_point = max([y for _,y in tower])
    line = [(2,0), (3,0), (4,0), (5,0)]
    cross = [(3,2), (2,1), (3,1), (4,1),(3,0)]
    l = [(2,0), (3,0), (4,0), (4,1), (4,2)]
    vert = [(2,3),(2,2),(2,1),(2,0)]
    cube = [(2,0),(2,1),(3,0),(3,1)]
    shapes = [line,cross,l,vert,cube]
    rock = shapes[rock_number %len(shapes)]
    return set([(x,y+highest_point+4) for x,y in rock])

def move_rock(rock, dir):
    if dir == '<':
        return set([(x-1,y) for x, y  in rock])
    if dir == '>':
        return set([(x+1,y) for x, y  in rock])
    if dir == DOWN:
        return set([(x,y-1) for x, y  in rock])
    raise NameError("Uh OH")

tower = set((i,0) for i in range(7))
dir = itertools.cycle(data)

# print(len(data) * 5)
# exit()
for i in range(2020):
    rock = spawn_rock(tower, i)
    valid = True
    # print(i)
    while valid:
        new_pos = move_rock(rock,next(dir))
        if not new_pos & tower and all( x >= 0 and x < 7 for x, _ in new_pos):
            rock = new_pos
        new_pos = move_rock(rock,DOWN)
        if not new_pos & tower:
            rock = new_pos
        else:
            valid = False
    tower = tower | rock
print(max([y for _,y in tower]))
