from pathlib import Path
from collections import Counter
import re

def parse_line(line):
    m = re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line)
    return [int(x) for x in m.groups()]

with open(Path("2022") / "day4" / "day4_input.txt") as f:
    data = [parse_line(x) for x in f.read().splitlines()]

def within(line):
    start1, end1, start2, end2 = line
    if start1 <= start2 and end1 >= end2:
        return True
    if start2 <= start1 and end2 >= end1:
        return True
    return False

def within2(line):
    start1, end1, start2, end2 = line
    if start1 <= start2 and end1 >= start2:
        return True
    if start2 <=start1 and end2 >= start1:
        return True
    return False

def part1(data):
    return sum(within(line) for line in data)

def part2(data):
    return sum(within2(line) for line in data)

print(f"Answer part 1: {part1(data)}")
print(f"Answer part 2: {part2(data)}")
