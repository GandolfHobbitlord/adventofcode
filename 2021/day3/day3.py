from pathlib import Path

def to_bin(bin):
    x = [pow(2,i) if x == 1 else 0 for i, x in enumerate(reversed(bin))]
    return sum(x)

def part1(data):
    types = zip(*data)
    ans = [1 if x.count('1') > x.count('0') else 0 for x in types]
    ans0 = to_bin(ans)
    ans1 = to_bin([0 if x else 1 for x in ans])
    return ans0*ans1

def most_common(lis, index):
    x = [line[index] for line in lis]
    if x.count('1') >= x.count('0'):
        return '1'
    else:
        return '0'

def least_common(lis, index):
    if most_common(lis, index) == '1':
        return '0'
    else:
        return '1'

def get_support_rating(data, criteria):
    keep = data.copy()
    for i in range(len(data[0])):
        common = criteria(keep, i)
        keep = [line for line in keep if line[i] == common]
        if len(keep) == 1:
            return to_bin([int(i) for i in keep[0]])

def get_oxygen(data):
   return get_support_rating(data, most_common)

def get_co2(data):
    return get_support_rating(data, least_common)

def part2(data):
    ox = get_oxygen(data)
    co2 = get_co2(data)
    return co2 * ox

with open(Path("2021") / "day3" / "day3_input.txt") as f:
   data = [line for line in f.read().splitlines()]

print(f'Answer part1 {part1(data)}')
print(f'Answer part2 {part2(data)}')