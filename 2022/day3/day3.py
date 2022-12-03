from pathlib import Path
from collections import Counter

score = {}
for i, l in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',1):
    score[l] = i

def part_1(data):
    ans = 0
    for line in data:
        p1 = line[len(line)//2:]
        p2 = line[:len(line)//2]
        intersec = Counter(p1) & Counter(p2)
        common_char = intersec.most_common(1)[0][0]
        ans += score[common_char]
    return ans

def part_2(data):
    ans = 0
    for p1, p2, p3 in zip(data[::3], data[1::3], data[2::3]):
        intersec = Counter(p1) & Counter(p2) & Counter(p3)
        common_char = intersec.most_common(1)[0][0]
        ans += score[common_char]
    return ans

with open(Path("2022") / "day3" / "day3_input.txt") as f:
    data = [x for x in f.read().splitlines()]

print(f"Answer part 1: {part_1(data)}")
print(f"Answer part 2: {part_2(data)}")