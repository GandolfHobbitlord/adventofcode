from pathlib import Path
from collections import defaultdict

def hashify(inp):
    val = 0
    for char in inp:
        val += ord(char)
        val *= 17
        val %= 256
    return val

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

def calc_power(hashmap):
    tot_power= 0
    for box_nr, lenses in hashmap.items():
        # print(box_nr, lenses)
        for pos, (label, foc_len) in enumerate(lenses.items(),start=1):
            val = (box_nr+1) * pos * foc_len
            # print(label, val)
            tot_power += val
    return tot_power

def part1(data):
    return sum([hashify(x) for x in data])

# Hurray for dicts being insert ordered
def part2(data):
    hashmap = defaultdict(dict)
    for cmd in data:
        if '-' in cmd:
            label = cmd[:-1]
            box_nr = hashify(label)
            # print(label, hashify(label))
            box = hashmap[box_nr]
            if label in box:
                del box[label]
        elif '=' in cmd:
            label, val = cmd.split('=')
            box_nr = hashify(label)
            box = hashmap[box_nr]
            box[label] = int(val)
        else:
            raise RuntimeError('Uh oh')
        # print('After ' + cmd)
        # print(hashmap)
    return calc_power(hashmap)

with open(Path("2023") / "day15" / "day15_input.txt") as f:
# with open(Path("2023") / "day15" / "day15_test.txt") as f:
    data = [line for line in f.read().split(',')]

print(f'Answer part1: {part1(data)}')
print(f'Answer part2: {part2(data)}')