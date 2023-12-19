from pathlib import Path
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
        out_rules.append((cat, operator, num, dest))
    out_rules.append(rules[-1])
    return key, out_rules

# Dear diary, today i made spaghetti
# Tactic: create a new range for each logical operator, continue parsing as if the statment was false
#         and create a new range with destination for each that is true

def get_next(part,rules):
    possible_out = []
    for cat, operator, num, dest in rules[:-1]:
        lo,  hi = part[cat]
        if operator =='<':
            new_hi = min(hi, num-1)
            if new_hi > lo:
                new_part = deepcopy(part)
                new_part[cat] = (lo,new_hi)
                possible_out.append((dest,new_part))
            lo = num
        elif operator == '>':
            new_lo = max(lo, num+1)
            if new_lo <  hi:
                new_part = deepcopy(part)
                new_part[cat] = (new_lo, hi)
                possible_out.append((dest,new_part))
            hi = num
        #Can we keep going?
        if lo <  hi:
            part[cat] = (lo, hi)
        else:
            return possible_out
    possible_out.append((rules[-1], part))
    return possible_out

with open(Path("2023") / "day19" / "day19_input.txt") as f:
# with open(Path("2023") / "day19" / "day19_test.txt") as f:
    wfs, parts  = f.read().split('\n\n')
parts = [parse_part(part) for part in parts.splitlines()]
wfs = dict([parse_workflow(wf) for wf in wfs.splitlines()])

part = {c: (1,4000) for c in 'xmas'}
parts = [('in' , part)]
passed = []
while parts:
    dest, part = parts.pop()
    if dest == 'A':
        passed.append(part)
    elif dest == 'R':
        continue
    else:
        new_possible = get_next(part,wfs[dest])
        parts += new_possible

ans = 0
for part in passed:
    comb = 1
    for lo, hi in part.values():
        comb *= hi - lo + 1
    ans += comb

print(f'Answer part 2: {ans}')
