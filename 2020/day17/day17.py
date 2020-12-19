from collections import defaultdict
def create_conway(inp):
    active_cubes = []
    for i, line in enumerate(inp.splitlines()):
        for j, char in enumerate(line):
            if char == '#':
                active_cubes.append((i,j,0))
    return active_cubes

def neighbors(pos):
    x,y,z = pos
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            for k in range(z-1,z+2):
                if (i,j,k) == pos:
                    continue
                yield (i,j,k)

def get_active_neighbors(pos,active_cubes):
    return len([n for n in neighbors(pos) if n in active_cubes])

def cycle(active_cubes):
    new_active_cubes = set()
    for cube in active_cubes:
        active_neighbors = get_active_neighbors(cube,active_cubes)
        if 2 <= active_neighbors <= 3:
            new_active_cubes.add(cube)
        for neighbor in neighbors(cube):
            active_neighbors = get_active_neighbors(neighbor,active_cubes)
            if neighbor not in active_cubes and active_neighbors == 3:
                new_active_cubes.add(neighbor)
    return new_active_cubes

def run_test():
    inp = """.#.
..#
###"""
    conway = create_conway(inp)
    print(conway)
    for _ in range(6):
        conway = cycle(conway)
    assert len(conway) == 112
    print([ c for c in conway if c[2] == -1])
run_test()

inp = """....#...
.#..###.
.#.#.###
.#....#.
...#.#.#
#.......
##....#.
.##..#.#"""
active_cubes = create_conway(inp)
for _ in range(6):
    active_cubes = cycle(active_cubes)
print(len(active_cubes))