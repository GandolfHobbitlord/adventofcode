import re
from pathlib import Path
from collections import Counter
def parse_line(line):
    m = re.match(r'(\w+) (\d+)', line)
    dir, distance = m.groups()
    return dir, int(distance)
score = {}
for i, l in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',1):
    score[l] = i
print(score)
with open(Path("2022") / "day3" / "day3_input.txt") as f:
    #data = [parse_line(x) for x in f.read().splitlines()]
    data = [x for x in f.read().splitlines()]
    l = list()
    for string in data:
        p1 = string[:len(string)//2]
        p2 = string[len(string)//2:]
        l.append((p1,p2))

ans = 0
for p1, p2 in l:
    c1 = Counter(p1)
    c2 = Counter(p2)
    c3 = c1 & c2
    f = c3.most_common(1)
    ans += score[f[0][0]]

print(ans)