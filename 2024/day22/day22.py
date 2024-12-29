from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def parse_line(line):
    # [int(i) for i in re.findall(r'-?\d+', line)]
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

with open(Path("2024") / "day22" / "day22_input.txt") as f:
# with open(Path("2024") / "day22" / "day22_test.txt") as f:
    data = [int(line) for line in f.read().split('\n')]
    # data = [parse_line(line) for line in f.read().split('\n')]

# print(data)
def mix(s,o):
    return s^o

def prune(s):
    return s % 16777216

def secret_calc(s,steps=1,p1=True):
    res = s
    final = []
    for _ in range(steps):
        res = prune(mix(res*64,res))
        res = prune(mix(res // 32, res))
        res = prune(mix(res * 2048, res))
        final.append(res % 10)
        # print(res)
    if p1:
        return res
    else:
        return final

assert mix(42,15) == 37
assert prune(100000000) == 16113920
assert secret_calc(123) == 15887950
assert secret_calc(123,2) == 16495136
# secret_calc(123,10)

assert secret_calc(1,2000) == 8685429
assert secret_calc(10,2000) == 4700978
assert secret_calc(100,2000) == 15273692
assert secret_calc(2024,2000) == 8667524
def part1(data):
    print(sum([secret_calc(d,2000) for d in data]))
def part2(data):
    resd = defaultdict(int)
    for d in data:
        sec = [d%10] + secret_calc(d,2000,p1=False)
        diffs = [b-a for a,b in zip(sec,sec[1:])]
        for i in range(4,len(sec)):
            # print(diffs[i-4:i],sec[i])
            k = tuple(diffs[i-4:i])
            v = sec[i]
            resd[k] += v
        # print(sec)
        # print(diffs)
    print(max(resd.values()))
    print(sorted([(v,k)for k, v in resd.items()])[-1])

# part2([123])
part2([1,2,3,2024])
