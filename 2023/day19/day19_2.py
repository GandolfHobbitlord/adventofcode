from pathlib import Path
import numpy as np
import re
from copy import deepcopy

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

# Dear diary, today i made spaghetti
# Tactic: create a new range for each logical operator, continue parsing as if the statment was false
#         and create a new range with destination for each that is true

def get_next(part,rules):
    possible_out = []
    for cat, operator, num, dest in rules[:-1]:
        mini, maxi = part[cat]
        if operator =='<':
            new_max = min(maxi, num-1)
            if new_max > mini:
                new_part = deepcopy(part)
                new_part[cat] = (mini,new_max)
                possible_out.append((dest,new_part))
            mini = num
        elif operator == '>':
            new_min = max(mini, num+1)
            if new_min < maxi:
                new_part = deepcopy(part)
                new_part[cat] = (new_min,maxi)
                possible_out.append((dest,new_part))
            maxi = num
        if mini < maxi:
            part[cat] = (mini,maxi)
        else:
            return possible_out
    if maxi > mini:
        possible_out.append((rules[-1], deepcopy(part)))
    return possible_out

with open(Path("2023") / "day19" / "day19_input.txt") as f:
# with open(Path("2023") / "day19" / "day19_test.txt") as f:
    wfs, parts  = f.read().split('\n\n')
parts = [parse_part(part) for part in parts.splitlines()]
wfs = dict([parse_workflow(wf) for wf in wfs.splitlines()])
print(wfs)
ans = 0
part = {c: (1,4000) for c in 'xmas'}
print(part)
minimax = [('in' , part)]
passed = []
while minimax:
    dest, part = minimax.pop()
    new_possible = get_next(part,wfs[dest])
    for key, val in new_possible:
        if key == 'A':
            passed.append(val)
        elif key == 'R':
            continue
        else:
            minimax.append((key,val))
    print('hello')

print(passed)
# vals = [minimax]
p2 = 0
for part in passed:
    v = 1
    for lo, hi in part.values():
        v *= hi - lo + 1
    p2 += v
print(p2)
# while vals:
#     key, mm = vals.pop()
#     get_next(mm,wfs[key])

# print(ans)