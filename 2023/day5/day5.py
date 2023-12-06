from pathlib import Path
import re
from collections import defaultdict
from collections import Counter
import numpy as np
from itertools import chain


def parse_map(map):
    print(map)
    range_list = []
    for line in map.split('\n')[1:]:
        print(line)
        dest, origin, ran = [int(x) for x in re.match(r'(\d+) (\d+) (\d+)', line).groups()]
        range_list.append((dest,origin,ran))
    return range_list
def get_conversion(curr,map):
    for dest, origin, ran in map:
        if curr >= origin and curr < origin + ran:
            return dest + curr - origin
    return curr
def get_seeds_p1(seed_line):
    return [int(x) for x in re.findall(r'\d+',seed_line)]

def get_seeds_p2(seed_line):
    r = []
    ss = list(([int(x) for x in re.findall(r'\d+',seed_line)]))
    for start, ran in zip(ss[::2], ss[1::2]):
        r.append(range(start,start+ran))
    return chain.from_iterable(r)
#     return
with open(Path("2023") / "day5" / "day5_input.txt") as f:
# with open(Path("2023") / "day5" / "day5_test.txt") as f:

    # data = [parse_line(line) for line in f.read().splitlines()]
    data = [line for line in f.read().split('\n\n')]

# seeds = get_seeds_p1(data[0])
seeds = get_seeds_p2(data[0])
print(seeds)
maps  = [parse_map(m) for m in data[1:]]
print(maps)
locations = []
min_location = 100000000000000000000
for s in seeds:
    curr = s
    for map in maps:
        n = get_conversion(curr,map)
        # print(f'{curr}->{n}')
        curr = n
    # locations.append(curr)
    min_location = min(min_location,curr)

print(min_location)
print(locations)
print(min(locations))