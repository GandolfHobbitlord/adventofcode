from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def parse_line(line):
    return [int(i) for i in re.findall(r'\d+', line)]

with open(Path("2025") / "day5" / "day5_input.txt") as f:
# with open(Path("2025") / "day5" / "day5_test.txt") as f:
    ranges, fruit = f.read().split('\n\n')
    ranges = [parse_line(line) for line in ranges.split('\n')]
    fruit = [int(f) for f in fruit.split('\n')]


def is_fresh(fruit,ranges):
    for lo, hi in ranges:
        if lo <= fruit and hi >= fruit:
            return True
    return False
ans = 0
print(ranges)
print(fruit)
for f in fruit:
    if is_fresh(f,ranges):
        # print("fresh", f)
        ans += 1

print(ans)