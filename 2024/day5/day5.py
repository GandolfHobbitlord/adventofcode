from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def parse_line(line):
    return [int(i) for i in re.findall(r'-?\d+', line)]
    return int(lo), int(hi), char, password
def parse_rules(rules):
    r = defaultdict(list)
    for rule in rules.splitlines():
        a, b = [int(d) for d in rule.split('|')]
        r[a].append(b)
    return r

# def parse_blob(blob):
# with open(Path("2024") / "day5" / "day5_input.txt") as f:

with open(Path("2024") / "day5" / "day5_test.txt") as f:
    rules, blob = f.read().split('\n\n')
    # data = [parse_line(line) for line in f.read().split('\n')]
qs = [parse_line(l) for l in blob.splitlines()]
rules = parse_rules(rules)

for q in qs:
    for i in range()
print(qs)
print(rules)


