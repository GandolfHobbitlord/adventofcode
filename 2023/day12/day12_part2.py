from pathlib import Path
import numpy as np
import re
from itertools import combinations
def parse_line(line):
    springs, groups = line.split(' ')
    groups = [int(x) for x in re.findall(r'\d+',groups)]
    return springs + '.', groups


def calc(springs, groups, i, group_i, curr, choices):
    ans = 0
    if i == len(springs): #appended all strings with "." so we don't need to close anything
        if group_i == len(groups):
            # print(choices)
            return 1
        return 0
    chars = [springs[i]]
    if chars[0] == '?':
        chars = ['#', '.']
    for char in chars:
        c = choices + [char]
        if char == '.':
            if curr == 0:
                #not on any currently
                ans += calc(springs, groups,i+1,group_i,0, c)
            else:
                if groups[group_i] != curr:
                    continue
                else:
                    ans += calc(springs, groups,i+1,group_i+1,0, c)
        else:
            if group_i == len(groups):
                continue
            elif groups[group_i] == curr:
                continue
            else:
                ans += calc(springs, groups,i+1,group_i,curr+1, c)
    return ans


# print(get_possible('???.###'))
with open(Path("2023") / "day12" / "day12_input.txt") as f:
# with open(Path("2023") / "day12" / "day12_test.txt") as f:
    data = [parse_line(line) for line in f.read().split('\n')]
tot = 0
for springs, groups in data:
    # print(springs, groups)
    tot += calc(springs,groups,0,0,0,[])
print(tot)