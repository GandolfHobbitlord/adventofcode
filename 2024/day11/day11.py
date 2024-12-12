# data = [int(d) for d in "0 1 10 99 999".split(" ")]
# data = [int(d) for d in "125 17".split(" ")]
data = [int(d) for d in "3935565 31753 437818 7697 5 38 0 123".split(" ")]
# part 1 solution
# def blink(stones):
#     out = []
#     for stone in stones:
#         digits = len(str(stone))
#         if stone == 0:
#             out.append(1)
#         elif digits % 2 == 0:
#             out.append(int(str(stone)[:digits//2]))
#             out.append(int(str(stone)[digits//2:]))
#         else:
#             out.append(stone*2024)
#     return out

cache = {}
def stone_blink(stone, blinks): # return number of stones
    if  blinks == 0:
        return 1
    digits = len(str(stone))
    if (stone,blinks) not in cache:
        if stone == 0:
                res = stone_blink(1, blinks-1)
        elif digits % 2 == 0:
                res =  stone_blink(int(str(stone)[:digits//2]),blinks-1)
                res += stone_blink(int(str(stone)[digits//2:]),blinks-1)
        else:
            res = stone_blink(stone*2024, blinks-1)
        cache[(stone,blinks)] = res
    return cache[(stone,blinks)]

stones = data
ans = []
for stone in stones:
    ans.append(stone_blink(stone,75))
print(ans)
print(sum(ans))