from pathlib import Path
import re

def part1(line):
    m = re.findall(r'mul\((\d+),(\d+)\)',line)
    return sum([(int(x) * int(y)) for x ,y in m])

def part2(line):
    enable = True
    ans = 0
    m = re.findall(r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))",line)
    for a,b, dont,do in m:
        if dont:
            enable = False
        elif do:
            enable = True
        elif a:
            if enable:
                ans += int(a) * int(b)
    return ans

with open(Path("2024") / "day3" / "day3_input.txt") as f:
# with open(Path("2024") / "day3" / "day3_test.txt") as f:
    data = f.read()

print(f'Answer 1: {part1(data)}')
print(f'Answer 2: {part2(data)}')
