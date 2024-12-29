from pathlib import Path
from collections import defaultdict

with open(Path("2024") / "day22" / "day22_input.txt") as f:
    data = [int(line) for line in f.read().split('\n')]

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
    if p1:
        return res
    else:
        return final

assert mix(42,15) == 37
assert prune(100000000) == 16113920
assert secret_calc(123) == 15887950
assert secret_calc(123,2) == 16495136
assert secret_calc(1,2000) == 8685429
assert secret_calc(10,2000) == 4700978
assert secret_calc(100,2000) == 15273692
assert secret_calc(2024,2000) == 8667524

def part1(data):
    print(sum([secret_calc(d,2000) for d in data]))

def get_seq(d):
    res = {}
    sec = [d%10] + secret_calc(d,2000,p1=False)
    diffs = [b-a for a,b in zip(sec,sec[1:])]
    for i in range(4,len(sec)):
        k = tuple(diffs[i-4:i])
        if k not in res:
            v = sec[i]
            res[k] = v
    return res

def part2(data):
    resd = defaultdict(int)
    for d in data:
        turnd= get_seq(d)
        for k,v in turnd.items():
            resd[k] += v
    print(max(resd.values()))

part1(data)
part2(data)

