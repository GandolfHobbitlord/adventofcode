from pathlib import Path
import re

def parse_line(line):
    return [int(i) for i in re.findall(r'\d+', line)]

with open(Path("2025") / "day5" / "day5_input.txt") as f:
# with open(Path("2025") / "day5" / "day5_test.txt") as f:
    ranges, fruit = f.read().split('\n\n')
    ranges = [parse_line(line) for line in ranges.split('\n')]
    fruit = [int(f) for f in fruit.split('\n')]


def is_fresh(fruit, ranges):
    for lo, hi in ranges:
        if lo <= fruit and hi >= fruit:
            return True
    return False

def part1(ranges, fruit):
    ans = 0
    for f in fruit:
        if is_fresh(f,ranges):
            ans += 1
    return ans

def part2(ranges):
    orig_ranges = ranges.copy()
    orig_ranges.sort(reverse=True)
    merged = [orig_ranges.pop()]
    while orig_ranges:
        r_lo,r_hi = orig_ranges.pop()
        if r_lo <= merged[-1][1]:
            merged[-1][1] = max(r_hi,merged[-1][1])
        else:
            merged.append([r_lo,r_hi])
    return sum([hi - lo + 1 for lo, hi in merged])

print(f"Answer part1: {part1(ranges,fruit)}")
print(f"Answer part2: {part2(ranges)}")

