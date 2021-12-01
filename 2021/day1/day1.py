from pathlib import Path

def part_1(depths):
   return sum([old < new for old, new in zip(depths, depths[1:])])

def part_2(depths):
   return sum([old < new for old, new in zip(depths, depths[3:])])

with open(Path("2021") / "day1" / "day1_input.txt") as f:
   depths = [int(depth) for depth in f.read().splitlines()]

print(f"Answer of part 1 is {part_1(depths)}")
print(f"Answer of part 2 is {part_2(depths)}")