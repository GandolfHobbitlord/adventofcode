from pathlib import Path
import numpy as np
import re
from collections import defaultdict, Counter
point_dict = {'A' : 'a',  'K' : 'b',  'Q' : 'c',  'J' : 'd',  'T' : 'e',  '9' : 'f',  '8' : 'g',  '7' : 'h',  '6' : 'i',  '5' : 'j',  '4' : 'k',  '3' : 'l',  '2' : 'm', }
def hand_to_points(hand):
    point_str = ''
    for card in hand:
        point_str += point_dict[card]
    return point_str
def get_hand_value(hand):
    h = Counter(hand)
    most_common = h.most_common(1)[0]
    if most_common[1] == 5:
        print('five of a kind')
        return 'a', hand_to_points(hand)
    most_common, second_common = h.most_common(2)
    print(hand)
    if most_common[1] == 5:
        print('five of a kind')
        return 'a', hand_to_points(hand)
    elif most_common[1] == 4:
        print('five of a kind')
        return 'b', hand_to_points(hand)
    elif most_common[1] == 3 and second_common[1] ==2:
        print('full house')
        return 'c', hand_to_points(hand)
    elif most_common[1] == 3:
        print('three of a kind')
        return 'd', hand_to_points(hand)
    elif most_common[1] == 2 and second_common[1] ==2:
        print('two pairs')
        return 'e', hand_to_points(hand)
    elif most_common[1] == 2:
        print('1 pair')
        return 'f', hand_to_points(hand)

    else:
        print('high card')
        return 'g', hand_to_points(hand)

with open(Path("2023") / "day7" / "day7_input.txt") as f:
# with open(Path("2023") / "day7" / "day7_test.txt") as f:
    data = [line.split(' ') for line in f.read().split('\n')]
a = []
for hand, bid in data:
    a.append((get_hand_value(hand), bid))
prio = sorted(a, key=lambda element: (element[0], element[1]),reverse=True)

ans = 0
for i, (_, bid) in enumerate(prio,1):
    ans += int(bid)*i
    print(ans)

    