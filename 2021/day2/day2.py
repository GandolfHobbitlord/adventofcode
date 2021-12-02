from pathlib import Path
import re

def parse_line(line):
    m = re.match(r'(\w+) (\d+)', line)
    dir, distance = m.groups()
    return dir, int(distance)

def part1(data):
    x = 0
    y = 0
    for dir, distance in data:
        if(dir == 'down'):
            y += distance
        if(dir == 'up'):
            y -= distance
        if(dir == 'forward'):
            x += distance
    return x*y

def part2(data):
    x = 0
    y = 0
    aim = 0
    for dir, distance in data:
        if(dir == 'down'):
            aim += distance
        if(dir == 'up'):
            aim -= distance
        if(dir == 'forward'):
            x += distance
            y += distance*aim
    return x*y

with open(Path("2021") / "day2" / "day2_input.txt") as f:
   data = [parse_line(line) for line in f.read().splitlines()]

print(f'Answer part 1 {part1(data)}')
print(f'Answer part 2 {part2(data)}')
