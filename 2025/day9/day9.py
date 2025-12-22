from pathlib import Path
import re
import itertools
from matplotlib import pyplot as plt

def parse_line(line):
    return tuple(int(i) for i in re.findall(r'-?\d+', line))

with open(Path("2025") / "day9" / "day9_input.txt") as f:
# with open(Path("2025") / "day9" / "day9_test.txt") as f:
    points = [parse_line(line) for line in f.read().split('\n')]

def part1(points):
    areas = []
    for a,b in itertools.combinations(points,2):
        areas.append((abs(a[0]-b[0])+1)*(1+abs(a[1]-b[1])))

    return max(areas)

def intersect(s0,s1,l0,l1):
    x0,y0 = s0
    x1,y1 = s1
    low_x,top_x  = (x0, x1) if x0 < x1 else (x1,x0)
    low_y,top_y  = (y0, y1) if y0 < y1 else (y1,y0)
    # This is not enough but given the input shape it works
    if (low_x >= l0[0] and low_x >= l1[0]) or (top_x <= l0[0] and top_x <= l1[0]):
        return False
    if (low_y >= l0[1] and low_y >= l1[1]) or (top_y <= l0[1] and top_y <= l1[1]):
        return False
    return True

def part2(points):
    areas = []
    points = points + [points[0]]
    for a,b in itertools.combinations(points,2):
        areas.append(((abs(a[0]-b[0])+1)*(1+abs(a[1]-b[1])),(a,b)))
    areas.sort(reverse=True)
    lines = [(a,b) for a,b in zip(points,points[1:])]
    x,y = zip(*points)
    plt.fill(x,y)
    plt.savefig('myplt.png') #visually inspect, its a circle with a cutout
    for area,  (a, b) in areas:
        found = True
        for l1, l2 in lines:
            if (intersect(a,b,l1,l2)):
                found = False
                break
        if found:
            return area

print(f"Answer part1: {part1(points)}")
print(f"Answer part2: {part2(points)}")