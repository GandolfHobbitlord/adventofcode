from collections import defaultdict
def create_conway(inp, dim = 3):
    active_cubes = set()
    for i, line in enumerate(inp.splitlines()):
        for j, char in enumerate(line):
            if char == '#':
                pos = [i,j]
                for _ in range(2,dim):
                    pos.append(0)
                active_cubes.add(tuple(pos))
    print(active_cubes)
    return active_cubes

# def neighbors(pos):
#     #Prob could use some fancy recursion here
#     x,y,z,w = pos
#     for i in range(x-1,x+2):
#         for j in range(y-1,y+2):
#             for k in range(z-1,z+2):
#                 for l in range(w-1,w+2):
#                     if (i,j,k,l) == pos:
#                         continue
#                     yield (i,j,k,l)
def neighbors(pos):
    pos = list(pos)
    if len(pos) == 1:
        for i in range(pos[0]-1,pos[0]+2):
            yield [i]
    else:
        for i in range(pos[0]-1, pos[0]+2):
            yield list(neighbors(pos[:-1])).append(i)

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
    # assert len(conway) == 112
    print([ c for c in conway if c[2] == -1])
# run_test()

inp = """....#...
.#..###.
.#.#.###
.#....#.
...#.#.#
#.......
##....#.
.##..#.#"""
active_cubes = create_conway(inp,4)
x = list(neighbors([0,1]))
for _ in range(6):
    active_cubes = cycle(active_cubes)
print(len(active_cubes))