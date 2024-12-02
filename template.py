from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def parse_line(line):
    # [int(i) for i in re.findall(r'-?\d+', line)]
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

# with open(Path("2024") / "dayx" / "dayx_input.txt") as f:
with open(Path("2024") / "dayx" / "dayx_test.txt") as f:
    data = [line for line in f.read().split('\n')]
    data = [parse_line(line) for line in f.read().split('\n')]

print(data)