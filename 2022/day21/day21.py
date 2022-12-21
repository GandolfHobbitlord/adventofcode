import re
from pathlib import Path
import sympy
monkeys = {}
def parse_line(line):
    m = line.split()
    monkey = m[0][:-1]
    if len(m) == 2:
        monkeys[monkey] = int(m[1])
    else:
        monkeys[monkey] = m[1:]

    # m = re.match(r'(\d+),(\d+)', line)


with open(Path("2022") / "day21" / "day21_input.txt") as f:
# with open(Path("2022") / "day14" / "day14_test.txt") as f:
    data = [parse_line(x) for x in f.read().splitlines()]

def get_num(monkey):
    if monkey == 'humn':
        return "X"
    if isinstance(monkeys[monkey],int):
        return monkeys[monkey]
    else:
        val1 = get_num(monkeys[monkey][0])
        op = monkeys[monkey][1]
        if monkey == 'root':
            op = '-'
        val2 = get_num(monkeys[monkey][2])
        equation = '(' + str(val1)+str(op)+str(val2) + ')'
        # print(equation)
        if "X" not in equation:
            equation = eval(equation)
        monkeys[monkey] = equation
        return equation

expr = get_num('root')
print(expr)
from sympy.solvers import solve
from sympy import Symbol
X = Symbol('X')
print(solve(eval(expr),X))
