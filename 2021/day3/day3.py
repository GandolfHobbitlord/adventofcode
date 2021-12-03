from pathlib import Path
import re

def parse_line(line):
    m = re.match(r'(\w+) (\d+)', line)
    dir, distance = m.groups()
    return dir, int(distance)

def run_tests():
    with open(Path("2021") / "day3" / "day3_test.txt") as f:
        pass

def to_bin(bin):
    x = [pow(2,i) if x == 1 else 0 for i, x in enumerate(reversed(bin))]
    print(x)
    return sum(x)

def part1(data):
    types = zip(*data)
    ans = [1 if x.count('1') > x.count('0') else 0 for x in types]
    ans0 = to_bin(ans)
    print(ans0)
    ans1 = [0 if x else 1 for x in ans]
    ans1 = to_bin(ans1)
    print(ans1)
    print(ans0*ans1)

def most_common(lis, index):
    print(lis)
    x = [line[index] for line in lis]
    print(x.count('1'))
    print(x.count('0'))
    if x.count('1') >= x.count('0'):
        return '1'
    else:
        return '0'

def least_common(lis, index):
    if most_common(lis, index) == '1':
        return '0'
    else:
        return '1'

def get_co2(data):
    keep = data.copy()
    for i in range(len(data[0])):
        common = least_common(keep, i)
        keep = [line for line in keep if line[i] == common]
        if len(keep) == 1:
            print(f"done with co2 {keep}")
            return [int(i) for i in keep[0]]

def get_oxygen(data):
    keep = data.copy()
    for i in range(len(data[0])):
        common = most_common(keep, i)
        keep = [line for line in keep if line[i] == common]
        if len(keep) == 1:
            print(f"done with oxygen {keep}")
            return [int(i) for i in keep[0]]

def part2(data):
    keep = data.copy()
    ox = get_oxygen(data)
    print(ox)
    ans0 = to_bin(ox)
    co2 = get_co2(data)
    ans1 = to_bin(co2)
    print(co2)
    print(to_bin(co2))
    print(ans1 * ans0)


with open(Path("2021") / "day3" / "day3_input.txt") as f:
   data = [line for line in f.read().splitlines()]
part2(data)
# part1(data)