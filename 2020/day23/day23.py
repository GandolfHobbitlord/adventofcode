
def play(cups, steps=10,part2=False):
    # This is a mess. circle is a dict abstracting a circular single linked list.
    # Each key holds the clockwise neighbor
    MAX_CUP = max(cups)
    circle = {}
    # print(cups)
    for i in range(len(cups)-1):
        circle[cups[i]] = cups[i+1]
    circle[cups[-1]] = cups[0]
    current_cup = cups[0]

    for _ in range(steps):
        picked_up = []
        next_cup = circle[current_cup]
        for _ in range(3):
            picked_up.append(next_cup)
            next_cup = circle[next_cup]
        circle[current_cup] = next_cup
        dest = current_cup -1
        while dest in picked_up or dest == 0:
            dest -=1
            if dest <= 0:
                dest = MAX_CUP
        circle[picked_up[-1]] = circle[dest]
        circle[dest] = picked_up[0]
        current_cup = next_cup
    if part2:
        return score2(circle)
    else:
        return score(circle)

def score(circle):
    val = circle[1]
    s = ""
    while val != 1:
        s = s + str(val)
        val = circle[val]
    return int(s)

def score2(circle):
    val = circle[1]
    val2 = circle[val]
    return val * val2

def run_test():
    cups = list(map(int,'389125467'))
    assert play(cups,10) == 92658374

    cups.extend([i for i in range(10,1000001)])
    assert play(cups,10000000,part2=True) == 149245887792

run_test()

cups = list(map(int,'739862541'))
print(f'Answer part 1: {play(cups,100)}')
cups.extend([i for i in range(10,1000001)])
print(f'Answer part 2: {play(cups,10000000,part2=True)}')
