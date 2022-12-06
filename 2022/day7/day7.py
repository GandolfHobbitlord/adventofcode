from pathlib import Path
import re

def parse_line(line):
    m = re.match(r'(\d+)', line)
    return [int(x) for x in m.groups()]

with open(Path("2022") / "day7" / "day7_input.txt") as f:
    data = [x for x in f.read().splitlines()]
print(data)