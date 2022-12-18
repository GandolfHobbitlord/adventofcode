import re
from pathlib import Path
from tqdm import tqdm

def parse_line(line):
    return [int(x) for x in  re.findall(r'(-?\d+)', line)]

def manhattan_distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

with open(Path("2022") / "day15" / "day15_input.txt") as f:
    data = [parse_line(x) for x in f.read().splitlines()]

def part1(data):
    nop = set()
    beacons = set()
    tar = 2000000

    for line in data:
        sens_x, sens_y, beacon_x, beacon_y = line
        if beacon_y == tar:
            beacons.add(beacon_x)
        man_distance = manhattan_distance(sens_x,sens_y,beacon_x,beacon_y)
        targ_distance = abs(sens_y - tar)
        if man_distance >= targ_distance:
            for diffs in range(0, man_distance-targ_distance+1):
                nop.add(sens_x + diffs)
                nop.add(sens_x - diffs)

    nop = nop-beacons
    return len(nop)

def find_valid(invalid_ranges,maximal):
    invalid_ranges.sort()
    latest_end = 0
    for start, end in invalid_ranges:
        if start > latest_end + 1:
            return latest_end + 1
        latest_end = max(latest_end, end)
        if end >= maximal:
            return None

def part2(data):
    maximal = 4000000
    sensors =[]
    for line in data:
        sens_x, sens_y, beacon_x, beacon_y = line
        sensors.append(((sens_x,sens_y), manhattan_distance(sens_x,sens_y,beacon_x,beacon_y)))
    for y in tqdm(range(maximal)):
        invalid_ranges = []
        for sensor, distance in sensors:
            projection = distance - manhattan_distance(sensor[0],sensor[1],sensor[0],y)
            if projection >= 0:
                invalid_ranges.append((sensor[0] - projection, sensor[0] + projection))
        valid_x = find_valid(invalid_ranges,maximal)
        if valid_x:
            print(f"found valid x {valid_x=}, {y=}")
            return valid_x*4000000+y

print(f'Part 1 {part1(data)}')
print(f'Part 2 {part2(data)}')
