from pathlib import Path

data = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
# with open(Path("2022") / "day17" / "day17_input.txt") as f:
#     data = f.read()
DOWN = 'v'
import itertools
def spawn_rock(highest_point, rock_number):
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


def to_hash(tower):
    maxY = max([y for (x,y) in tower])
    return frozenset([(x,maxY-y) for (x,y) in tower if maxY-y<=20])

tower = set((i,0) for i in range(7))
dir = enumerate(itertools.cycle(data))

# print(len(data) * 5)
# exit()
hashes = {}
dir_nr = 0
turn = 0
max_turns = int(1e12)

while turn < max_turns:
    h = (to_hash(tower),turn % 5,dir_nr %len(data))
    if h in hashes:
        start_turn, start_height = hashes[h]
        turns_in_cycle = turn - start_turn
        height_increase_per_cycle = highest_point - hashes[h][1]
        turns_left = max_turns - turn
        cycles = turns_left // turns_in_cycle
        turn += cycles * turns_in_cycle
        tower = set([(x, y +height_increase_per_cycle * cycles) for x, y in tower])
        hashes = {}
    highest_point = max([y for _,y in tower])
    rock = spawn_rock(highest_point, turn)
    hashes[h] = (turn,highest_point)

    valid = True
    # print(i)
    while valid:
        dir_nr, direction = next(dir)
        new_pos = move_rock(rock,direction)
        if not new_pos & tower and all( x >= 0 and x < 7 for x, _ in new_pos):
            rock = new_pos
        new_pos = move_rock(rock,DOWN)
        if not new_pos & tower:
            rock = new_pos
        else:
            valid = False
    tower = tower | rock
    turn += 1
print(max([y for _,y in tower]))
