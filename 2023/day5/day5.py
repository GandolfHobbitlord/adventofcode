from pathlib import Path
import re
from collections import defaultdict
from collections import Counter
import numpy as np


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

# def get_seeds_p2(seed_line):
#     ss = list(([int(x) for x in re.findall(r'\d+',seed_line)]))

#     print(ss)
#     exit()
#     return
with open(Path("2023") / "day5" / "day5_input.txt") as f:
# with open(Path("2023") / "day5" / "day5_test.txt") as f:

    # data = [parse_line(line) for line in f.read().splitlines()]
    data = [line for line in f.read().split('\n\n')]

# seeds = get_seeds_p1(data[0])
seeds = get_seeds_p1(data[0])
print(seeds)
maps  = [parse_map(m) for m in data[1:]]
print(maps)
locations = []
for s in seeds:
    curr = s
    for map in maps:
        n = get_conversion(curr,map)
        print(f'{curr}->{n}')
        curr = n
    locations.append(curr)
print(locations)
print(min(locations))
