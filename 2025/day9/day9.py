from pathlib import Path
import re
import itertools

def parse_line(line):
    return tuple(int(i) for i in re.findall(r'-?\d+', line))

with open(Path("2025") / "day9" / "day9_input.txt") as f:
# with open(Path("2025") / "day9" / "day9_test.txt") as f:
    points = set(parse_line(line) for line in f.read().split('\n'))

areas = []
for a,b in itertools.combinations(points,2):
    areas.append((abs(a[0]-b[0])+1)*(1+abs(a[1]-b[1])))

print(max(areas))