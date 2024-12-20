from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict
import functools
def parse_towles(line):
    return [i for i in re.findall(r'\w+', line)]


with open(Path("2024") / "day19" / "day19_input.txt") as f:
# with open(Path("2024") / "day19" / "day19_test.txt") as f:
    lines = [line for line in f.read().split('\n')]
    towels = set(parse_towles(lines[0]))
    patterns = lines[2:]

@functools.cache
def parse(pattern):
    if pattern == '':
        return True
    possible =  [towl for towl in towels if pattern.startswith(towl)]
    for p in possible:
        s = pattern[len(p):]
        res = parse(s)
        if res:
            return True
    return False

for pattern in patterns:
    # print(pattern)
    print(parse(pattern),pattern)
print(sum([parse(pattern) for pattern in patterns]))