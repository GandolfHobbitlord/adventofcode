from pathlib import Path
import re

d = {'one': '1',
     'two': '2',
    'three':'3',
    'four': '4',
    'five': '5',
    'six':  '6',
    'seven': '7' ,
    'eight': '8',
    'nine':  '9' }
d = d | {str(x):str(x) for x in range(10)}

def parse_line(line,part2 = True):
    if part2:
        # TIL about lookaheads
        matches = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))',line)
    else:
        matches = re.findall(r'\d',line)
    return int(d[matches[0]] + d[matches[-1]])

with open(Path("2023") / "day1" / "day1_input.txt") as f:
    data = [x for x in f.read().splitlines()]

part1 = sum(parse_line(line, part2=False) for line in data)
part2 = sum(parse_line(line, part2=True) for line in data)

print(f'Answer Part 1: {part1}')
print(f'Answer Part 2: {part2}')
