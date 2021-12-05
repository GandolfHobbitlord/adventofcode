import re
from pathlib import Path
from collections import defaultdict
def parse_line(line):
    m = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line)
    return [int(x) for x in m.groups()]


def part1(lines, part2 = False):
    print(lines)
    mappy = defaultdict(int)
    for x0,y0,x1,y1 in lines:
        #print(f"{x0,y0} {x1,y1}")
        if x0 == x1:
            for y in range(y0,y1+1) or range(y1,y0+1): # Ugly use of or operator
                #print(f"Adding {x0,y}")
                mappy[(x0,y)] += 1
        elif y0 == y1:
            for x in range(x0,x1+1) or range(x1,x0+1):
                #print(f"Adding {x,y0}")
                mappy[(x,y0)] += 1
        else:
            print(f"Pass {x0,y0} {x1,y1}")
            if part2:
                for x, y in zip(range(x0,x1+1) or range(x0,x1 -1 ,-1), range(y0,y1+1) or range(y0, y1-1, -1)): # SHAME!
                    # print(f"Adding {x,y}")
                    mappy[(x,y)] += 1
    return len([val for _, val in mappy.items() if val > 1])
def run_tests():
    inp = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
    lines = [parse_line(line) for line in inp.splitlines()]
    assert 5 == part1(lines)
    assert 12 == part1(lines, part2=True)

run_tests()
print(*range(10,5-1,-1))
print()
with open(Path("2021") / "day5" / "day5_input.txt") as f:
   data = [parse_line(line) for line in f.read().splitlines()]
   print(part1(data))
   print(part1(data,True))