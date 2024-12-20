from pathlib import Path
import re
import functools

def parse_towles(line):
    return [i for i in re.findall(r'\w+', line)]


with open(Path("2024") / "day19" / "day19_input.txt") as f:
# with open(Path("2024") / "day19" / "day19_test.txt") as f:
    lines = [line for line in f.read().split('\n')]
    towels = set(parse_towles(lines[0]))
    patterns = lines[2:]

#Python felt like cheating today
@functools.cache
def parse2(pattern):
    if pattern == '':
        return 1
    possible =  [towl for towl in towels if pattern.startswith(towl)]
    res = 0
    for p in possible:
        s = pattern[len(p):]
        res += parse2(s)
    return res

ans = [parse2(pattern) for pattern in patterns]
ans1 =  sum([p != 0 for p in ans])
ans2 =  sum(ans)
print(f'anwers part 1: {ans1}')
print(f'anwers part 2: {ans2}')
