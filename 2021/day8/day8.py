import re
from pathlib import Path
from collections import defaultdict

def parse_line(line):
    output_nums = re.findall("\w+",line.split('|')[1])
    print(output_nums)
    return output_nums

def part1(data):
    ans = 0
    for line in data.splitlines():
        output = parse_line(line)
        for o in output:
            if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
                print(o, "is valid")
                ans +=1
    print(ans)

with open(Path("2021") / "day8" / "day8_input.txt") as f:
   data = f.read()

part1(data)