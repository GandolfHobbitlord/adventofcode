from collections import deque

def step(cups):
    # print(cups)
    pickup = cups[1:4]
    # print('Pickup', pickup)
    dest = cups[0] -1
    new = [cups[0]] + cups[4:]
    # print(new)
    # print(dest)
    while dest not in new:
        dest -=1
        if dest <= 0:
            dest = max(cups)
    # print('destination', dest)
    ind = new.index(dest)
    # print('index', ind)
    new[ind+1:ind+1] = pickup
    return new[1:] + new[:1]

def score(cups):
    ind = cups.index(1)
    s = cups[ind+1:] + cups[:ind]
    return int("".join(map(str,s)))

def score2(cups):
    ind = cups.index(1)
    print(cups[ind+1],cups[ind+2])
    return cups[ind+1] * cups[ind+2]
def run_test():
    cups = list(map(int,'389125467'))
    for _ in range(10):
        cups = step(cups)
    # print(cups)
    assert score(cups) == 92658374

    cups = list(map(int,'389125467'))
    cups.extend([i for i in range(max(cups),1000001)])
    print(max(cups))
    for _ in range(10000000):
        cups = step(cups)
    print(score2(cups))

run_test()

# cups = list(map(int,'739862541'))
# for _ in range(100):
#     cups = step(cups)
# print(score(cups))