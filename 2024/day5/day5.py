from pathlib import Path
import re
from collections import defaultdict
from functools import cmp_to_key

def parse_q(line):
    return [int(i) for i in re.findall(r'-?\d+', line)]

def parse_rules(rules):
    r = defaultdict(list)
    for rule in rules.splitlines():
        a, b = [int(d) for d in rule.split('|')]
        r[a].append(b)
    return r


with open(Path("2024") / "day5" / "day5_input.txt") as f:
# with open(Path("2024") / "day5" / "day5_test.txt") as f:
    rules, blob = f.read().split('\n\n')
qs = [parse_q(l) for l in blob.splitlines()]
rules = parse_rules(rules)

def is_valid(q):
    for i in reversed(range(1,len(q))):
        a = set(rules[q[i]])
        b = set(q[:i])
        if a & b:
            return False
    return True


def part1(qs):
    middles = []
    for q in qs:
        if is_valid(q):
            middles.append(q[len(q)//2])
    return sum(middles)

# Not sure if this covers all cases but it works...
def comp_pages(a,b):
    if b in rules[a]:
        return -1
    elif a in rules[b]:
        return 1
    else:
        return 0

def part2(qs):
    middles = []
    for q in qs:
        if not is_valid(q):
            s = sorted(q,key=cmp_to_key(comp_pages))
            middles.append(s[len(s)//2])
    return sum(middles)

print(part1(qs))
print(part2(qs))
