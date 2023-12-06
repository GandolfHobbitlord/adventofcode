import numpy as np
# times =    [7,  15,   30]
# distances = [  9,  40,  200]

times = [40,81,77,72]
distances = [219,1012,1365,1089]

ans = []
for race_time, distance in zip(times, distances):
    x = np.array(range(race_time))
    traveled = x*(race_time-x)
    ans.append(np.sum(traveled>distance))
print(f'Answer Part 1: {np.prod(ans)}')

#Part 2, lets do some math i guess...
race_time = int(''.join(str(time) for time in times ))
distance = int(''.join(str(distance) for distance in distances))

lower, upper = sorted(np.roots([-1,race_time,-distance]))
lower = np.ceil(lower)
upper = np.floor(upper)
print(f'Answer part 2: {int(upper- lower + 1)}')