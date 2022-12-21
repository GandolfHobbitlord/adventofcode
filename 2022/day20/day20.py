from pathlib import Path
from collections import deque
with open(Path("2022") / "day20" / "day20_input.txt") as f:
    data = [int(x) for x in f.read().splitlines()]

def mix(nums,repeats=1):
    original = nums.copy()
    for _ in range(repeats):
        for node in original:
            ind = nums.index(node)
            nums.rotate(-ind)
            popped_node = nums.popleft()
            nums.rotate(-popped_node[1])
            nums.appendleft(popped_node)

def get_grove_index(numbers, zero_index):
    ind = numbers.index((zero_index,0))
    return ([numbers[(ind + 1000) % len(numbers)][1],
    numbers[(ind + 2000) % len(numbers)][1],
    numbers[(ind + 3000) % len(numbers)][1]])

def part1(data):
    original_zero_index = data.index(0)
    nums = deque(enumerate(data))
    mix(nums)
    print(sum(get_grove_index(nums, original_zero_index)))

def part2(data):
    decrypt = 811589153
    original_zero_index = data.index(0)
    nums = deque((i,val*decrypt) for i, val in enumerate(data))
    mix(nums,10)
    print(sum(get_grove_index(nums, original_zero_index)))

part2(data)
