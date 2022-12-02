from pathlib import Path
import re

def parse_line(line):
    m = re.match(r'(\w) (\w)', line)
    return m.groups()

# rock paper sic
score = {'X': 1, 'Y': 2, 'Z': 3}
elf = {'A': 1, 'B': 2, 'C': 3}

with open(Path("2022") / "day2" / "day2_input.txt") as f:
    data = [parse_line(x) for x in f.read().splitlines()]

def part1(data):
    tot = 0
    for p1, p2 in data:
        if score[p2] - elf[p1] == 0:
            tot +=3
        elif score[p2] - elf[p1] == 1 or p2 == 'X' and p1 == 'C':
            tot += 6
        else:
            tot += 0
        tot += score[p2]
    return tot

def part2(data):
    tot = 0
    for p1,p2 in data:
        if p2 == 'X':
            ind = elf[p1]
            if ind -1 > 0:
                tot += (ind -1)
            else:
                tot+= 3
        elif p2 == 'Y':
            tot+= elf[p1]
            tot+= 3
        elif p2 == 'Z':
            ind = elf[p1]
            if ind +1 > 3:
                tot += 1
            else:
                tot += (1+ind)
            tot +=6
    return tot

print(f"Answer part 1: {part1(data)}")
print(f"Answer part 2: {part2(data)}")
