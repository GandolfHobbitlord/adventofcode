from pathlib import Path

def part_1(nums):
   print(sum([old < new for old, new in zip(nums, nums[1:])]))

def part_2(nums):
   increase = 0
   for i in range(3,len(num)):
      old = sum(num[i-3:i])
      new = sum(num[i-2:i+1])
      if old < new:
         increase += 1
   print(increase)

with open(Path("2021") / "day1" / "day1_input.txt") as f:
   num = [int(x) for x in f.read().splitlines()]

part_1(num)
part_2(num)