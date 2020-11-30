f = open("input.txt")
nums = [int(line) for line in f.readlines()]
print(sum(nums))