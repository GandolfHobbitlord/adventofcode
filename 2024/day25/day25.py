from pathlib import Path
import numpy as np
import itertools

def to_array(chart):
    return np.array([list(n) for n in chart.splitlines()])

with open(Path("2024") / "day25" / "day25_input.txt") as f:
# with open(Path("2024") / "day25" / "day25_test.txt") as f:
    data = [to_array(chart) for chart in f.read().split('\n\n')]

valid = 0
for a,b in itertools.combinations(data,2):
        if not np.any(np.logical_and(a == '#',b == '#')):
            valid += 1
print(valid)