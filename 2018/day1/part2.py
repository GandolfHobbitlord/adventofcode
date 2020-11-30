import itertools

f = open("input.txt")
nums = [int(line) for line in f.readlines()]
freq = 0
seen = set([0])
for num in itertools.cycle(nums):
    freq += num
    if freq in seen:
        print("Found duplicate:", freq)
        break
    else:
        seen.add(freq)