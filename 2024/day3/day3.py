from pathlib import Path
import re

def parse_line1(line):
    # [int(i) for i in re.findall(r'-?\d+', line)]
    # m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    # m = re.findall(r'(\d+)-(\d+) (\w): (\w+)', line)

    m = re.findall(r'mul\((\d+),(\d+)\)',line)
    return [(int(x), int(y)) for x ,y in m]

def parse_line2(l):
    enable = True
    line = l
    ans = 0
    while line:
        m = re.search(r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))",line)
        if m is None:
            break
        a,b, dont,do = m.groups()
        if dont:
            print("disable")
            enable = False
            ind = re.search(r"(don't\(\))",line).start()
        elif do:
            print("enable")
            enable = True
            ind = re.search(r"(do\(\))",line).start()
        elif a:
            print(f"mul {a} {b} {enable}")
            ind = re.search(r"mul\(\d+,\d+\)",line).start()
            if enable:
                ans += int(a) * int(b)
        line = line[ind+1:]
    print(ans)
        # line = line[ind+1:]
    # next_do = re.search(r"don't\(\)",line).start()
    # next_dont = re.search(r"do\(\)",line).start()
    # m = re.search(r'mul\((\d+),(\d+)\)',line)
    # ind = m.start()
    # a = next_do - ind
    # b = next_dont - ind
    # if a < b or m.start() :
    #     enabled
    # return [(int(x), int(y)) for x ,y in m]
with open(Path("2024") / "day3" / "day3_input.txt") as f:
# with open(Path("2024") / "day3" / "day3_test.txt") as f:
    data = f.read()
#     # data = [parse_line(line) for line in f.read().split('\n')]
# a =parse_line1(data)
# print(a)
# print( sum([x*y for x,y in a]))

# parse_line2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
parse_line2(data)
