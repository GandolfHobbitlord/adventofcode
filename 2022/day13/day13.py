import re
from pathlib import Path
import functools

def search(left, right):
    for l, r in zip(left,right):
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return 1
            elif l > r:
                return -1
        elif isinstance(l, list) and isinstance(r, list):
            val = search(l,r)
            if val != 0:
                return val
        elif isinstance(l, int) and isinstance(r, list):
            val = search([l],r)
            if val != 0:
                return val
        elif isinstance(l, list) and isinstance(r, int):
            val = search(l,[r])
            if val != 0:
                return val
        else:
            print("ERROR")
    if len(left) < len(right):
        return 1
    elif len(left) > len(right):
        return -1
    return 0

def pair_eval(pair):
    left, right = pair.splitlines()
    print(left, right)
    left = eval(left)
    right = eval(right)
    return search(left,right)
with open(Path("2022") / "day13" / "day13_input.txt") as f:
    data = [x for x in f.read().split('\n\n')]

print(sum([i for i,pair in enumerate(data,1) if 1 == pair_eval(pair)]))
new_data = []

for pair in data:
    new_data.extend(pair.splitlines())

inserts = []
results = [search(eval(p1),eval(p2)) for p1, p2 in zip(new_data, new_data[1:])]

def compare(left, right):
    return search(eval(left),eval(right))

new_data.extend(['[[2]]','[[6]]'])
new_data.sort(key=functools.cmp_to_key(compare),reverse=True)
print((new_data.index('[[2]]')+1) * (new_data.index('[[6]]')+1))