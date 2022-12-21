import re
from pathlib import Path
monkeys = {}
def parse_line(line):
    m = line.split()
    monkey = m[0][:-1]
    print(monkey)
    if len(m) == 2:
        monkeys[monkey] = int(m[1])
    else:
        monkeys[monkey] = m[1:]

    # m = re.match(r'(\d+),(\d+)', line)


with open(Path("2022") / "day21" / "day21_input.txt") as f:
# with open(Path("2022") / "day14" / "day14_test.txt") as f:
    data = [parse_line(x) for x in f.read().splitlines()]
print(monkeys)

def get_num(monkey):
    if isinstance(monkeys[monkey],int):
        return monkeys[monkey]
    else:
        val1 = get_num(monkeys[monkey][0])
        op = monkeys[monkey][1]
        val2 = get_num(monkeys[monkey][2])
        num = eval(str(val1)+str(op)+str(val2))
        monkeys[monkey] = num
        return num

print(get_num('root'))