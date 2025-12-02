from pathlib import Path

with open(Path("2025") / "day2" / "day2_input.txt") as f:
# with open(Path("2025") / "day2" / "day2_test.txt") as f:
    data = [line for line in f.read().split(',')]
    # data = [parse_line(line) for line in f.read().split('\n')]

def part1(data):
    count = []
    for d in data:
        lo,hi = [int(d) for d in d.split('-')]
        for d in range(lo,hi+1):
            i = str(d)
            left = i[:len(i)//2]
            right = i[len(i)//2:]
            if left == right:
                count.append(d)
                # print(left, right)
                print(d)

def divide_str(s, i):
    left = 0
    right = i
    while right <= len(s):
        yield s[left:right]
        left +=i
        right += i

def part2(data):
    count = []
    for d in data:
        lo,hi = [int(d) for d in d.split('-')]
        for d in range(lo,hi+1):
            i = str(d)
            # print(i)
            for diviser in range(1,1+ len(i)//2):
                if len(i) % diviser != 0:
                    continue
                parts = list(divide_str(i,diviser))
                # print(parts)
                if len(set(parts)) == 1 and d not in count:
                    print(d)
                    count.append(d)
    print(sum(count))

part2(data)