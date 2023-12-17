from pathlib import Path
import numpy as np
import re

def parse_line(line):
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

def hashify(inp):
    val = 0
    for char in inp:
        val += ord(char)
        val *= 17
        val = val % 256
    # print(val)
    return val
with open(Path("2023") / "day15" / "day15_input.txt") as f:
# with open(Path("2023") / "day15" / "day15_test.txt") as f:
    data = [line for line in f.read().split(',')]
    # data = [parse_line(line) for line in f.read().split('\n')]
assert hashify('HASH') == 52
assert hashify('rn=1') == 30
assert hashify('cm-') == 253
assert hashify('qp=3') == 97
assert hashify('cm=2') == 47
assert hashify('qp-') == 14
assert hashify('pc=4') == 180
assert hashify('ot=9') == 9
assert hashify('ab=5') == 197
assert hashify('pc-') == 48
assert hashify('pc=6') == 214
assert hashify('ot=7') == 231
def part1(data):
    print(sum([hashify(x) for x in data]))

part1(data)
