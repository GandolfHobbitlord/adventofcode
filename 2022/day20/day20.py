from pathlib import Path
from collections import deque
with open(Path("2022") / "day20" / "day20_input.txt") as f:
    key = [int(x) for x in f.read().splitlines()]
# key = [1, 2, -3, 3, -2, 0, 4]

nums = deque(enumerate(key))
original = nums.copy()
original_zero_index = key.index(0)

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


print(sum(get_grove_index(nums, original_zero_index)))
# print(sum(get_grove_index(nums)))

# print(numbers)