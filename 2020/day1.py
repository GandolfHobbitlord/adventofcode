import itertools
from pathlib import Path

def part1(input_list):
    for perm in itertools.permutations(input_list,2):
        if sum(perm) == 2020:
            return perm

def part2(input_list):
    for perm in itertools.permutations(input_list,3):
        if sum(perm) == 2020:
            return perm

with open(Path("2020") / "day1_input.txt") as f:
    numbers = [int(x) for x in f.read().splitlines()]

x,y = part1(numbers)
print(f'Par1: Numbers are {x} and {y}. Product is {x*y}')
x,y,z = part2(numbers)
print(f'Part2: Numbers are {x}, {y} and {z}. Product is {x*y*z}')