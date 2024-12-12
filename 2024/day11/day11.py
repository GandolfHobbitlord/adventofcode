data = [int(d) for d in "0 1 10 99 999".split(" ")]
data = [int(d) for d in "125 17".split(" ")]
data = [int(d) for d in "3935565 31753 437818 7697 5 38 0 123".split(" ")]


print(data)



def blink(stones):
    out = []
    for stone in stones:
        digits = len(str(stone))
        if stone == 0:
            out.append(1)
        elif digits % 2 == 0:
            out.append(int(str(stone)[:digits//2]))
            out.append(int(str(stone)[digits//2:]))
        else:
            out.append(stone*2024)
    return out

stones = data
for i in range(75):
    print(i)
    stones = blink(stones)
    # print(stones)
print(len(stones))