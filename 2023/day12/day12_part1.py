from pathlib import Path
import re
from itertools import combinations

def parse_line(line):
    springs, groups = line.split(' ')
    groups = [int(x) for x in re.findall(r'\d+',groups)]
    print(springs,groups)
    return springs, groups

def get_groups(springs):
    groups = []
    curr = 0
    if '?' in springs:
        raise RuntimeError('no ? allowed')

    for s in springs:
        if s == '#':
            curr += 1
        elif s == '.' and curr != 0:
            groups.append(curr)
            curr = 0
    if curr != 0:
        groups.append(curr)

    return groups

assert get_groups('#.#.###') == [1,1,3]
assert get_groups('.#...#....###.') ==  [1,1,3]
assert get_groups('.#.###.#.######') ==  [1,3,1,6]
assert get_groups('####.#...#...') ==  [4,1,1]
assert get_groups('#....######..#####.') ==  [1,6,5]
assert get_groups('.###.##....#') ==  [3,2,1]

def get_possible(springs):
    questions = [i for i, letter in enumerate(springs) if letter == '?']
    for i in range(len(questions)+1):
        for broken in combinations(questions,i):
            s = list(springs)
            for q in questions:
                if q in broken:
                    s[q] = '.'
                else:
                    s[q] = '#'
            # print(s)
            tmp = get_groups(s)
            # print(tmp)
            yield tmp

# print(get_possible('???.###'))
with open(Path("2023") / "day12" / "day12_input.txt") as f:
# with open(Path("2023") / "day12" / "day12_test.txt") as f:
    data = [parse_line(line) for line in f.read().split('\n')]
tot = 0
for springs, groups in data:
     tot += len([g for g in get_possible(springs) if g == groups])
print(tot)