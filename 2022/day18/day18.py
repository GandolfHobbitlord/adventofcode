from pathlib import Path
import re
def parse_line(line):
    return tuple([int(x) for x in  re.findall(r'(-?\d+)', line)])


with open(Path("2022") / "day18" / "day18_input.txt") as f:
    data = set([parse_line(x) for x in f.read().splitlines()])

def get_neighbor(center):
    x,y,z = center
    yield (x+1,y,z)
    yield (x-1,y,z)
    yield (x,y+1,z)
    yield (x,y-1,z)
    yield (x,y,z+1)
    yield (x,y,z-1)

sides = 0
for val in data:
    seen_sides = 6
    for neighbor in get_neighbor(val):
        if neighbor in data:
            seen_sides -= 1
    sides += seen_sides
print(sides)