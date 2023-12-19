from pathlib import Path
import numpy as np
import re

# This years dirty eval!
def parse_part(part):
    for val in 'xmas':
        part = part.replace(f'{val}=',f'"{val}":')
    return eval(part)

def parse_workflow(wf):

    key, rest = wf.split('{')
    rules = rest[:-1].split(',')
    out_rules = []
    for rule in rules[:-1]:

        e, dest = rule.split(':')
        cat = e[0]
        operator = e[1]
        num = int(e[2:])
        out_rules.append((cat, operator, num,dest))
    out_rules.append(rules[-1])
    return key, out_rules

def get_next(part,rules):
    for cat, operator, num, dest in rules[:-1]:
        if operator =='<':
            if part[cat] < num:
                return dest
        elif operator == '>':
            if part[cat] > num:
                return dest
    return rules[-1]

with open(Path("2023") / "day19" / "day19_input.txt") as f:
# with open(Path("2023") / "day19" / "day19_test.txt") as f:
    wfs, parts  = f.read().split('\n\n')
parts = [parse_part(part) for part in parts.splitlines()]
wfs = dict([parse_workflow(wf) for wf in wfs.splitlines()])
print(wfs)
ans = 0

for part in parts:
    loc = 'in'
    while not (loc == 'A' or loc == 'R'):
        loc = get_next(part, wfs[loc])
    if loc == 'A':
        ans += sum(part.values())

print(ans)